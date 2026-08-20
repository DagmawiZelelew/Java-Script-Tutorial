"""
Camera Tones
============
Captures live video from your webcam and applies different "media tone"
color-grading presets in real time (like Instagram/photo-app filters):

    warm       - golden, sunset-like warmth
    cool       - blue, crisp, cinematic cold tone
    vintage    - faded, sepia-leaning retro look
    sepia      - classic monochrome brown
    bw         - black & white (with contrast boost)
    vibrant    - punchy saturated colors
    cinematic  - teal & orange film-style grade
    none       - raw camera feed, no filter

Controls (press while the video window is focused):
    1-8   switch tone preset (see order above)
    s     save a snapshot of the current frame to ./snapshots/
    q/ESC quit

Requirements:
    pip install opencv-python numpy
"""

import cv2
import numpy as np
import os
import time

# --------------------------------------------------------------------------
# Tone / color-grading functions
# --------------------------------------------------------------------------

def _apply_curve(channel, curve):
    """Map an 8-bit channel through a 256-entry lookup table."""
    return cv2.LUT(channel, curve)


def _build_curve(points):
    """
    Build a smooth 256-value lookup table from a few (x, y) control points
    using linear interpolation. points must include x=0 and x=255.
    """
    points = sorted(points)
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    curve = np.interp(np.arange(256), xs, ys).astype(np.uint8)
    return curve


def tone_none(frame):
    return frame


def tone_warm(frame):
    b, g, r = cv2.split(frame)
    r = _apply_curve(r, _build_curve([(0, 0), (128, 150), (255, 255)]))
    b = _apply_curve(b, _build_curve([(0, 0), (128, 90), (255, 200)]))
    frame = cv2.merge((b, g, r))
    # slight brightness/saturation lift
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV).astype(np.float32)
    hsv[:, :, 1] = np.clip(hsv[:, :, 1] * 1.15, 0, 255)
    return cv2.cvtColor(hsv.astype(np.uint8), cv2.COLOR_HSV2BGR)


def tone_cool(frame):
    b, g, r = cv2.split(frame)
    b = _apply_curve(b, _build_curve([(0, 0), (128, 150), (255, 255)]))
    r = _apply_curve(r, _build_curve([(0, 0), (128, 90), (255, 200)]))
    frame = cv2.merge((b, g, r))
    return frame


def tone_vintage(frame):
    # desaturate slightly, add sepia-ish tint, lower contrast, add vignette
    faded = cv2.convertScaleAbs(frame, alpha=0.85, beta=15)
    hsv = cv2.cvtColor(faded, cv2.COLOR_BGR2HSV).astype(np.float32)
    hsv[:, :, 1] = np.clip(hsv[:, :, 1] * 0.6, 0, 255)
    faded = cv2.cvtColor(hsv.astype(np.uint8), cv2.COLOR_HSV2BGR)

    sepia_kernel = np.array([[0.131, 0.534, 0.272],
                              [0.168, 0.686, 0.349],
                              [0.189, 0.769, 0.393]])
    sepia = cv2.transform(faded, sepia_kernel)
    sepia = np.clip(sepia, 0, 255).astype(np.uint8)
    result = cv2.addWeighted(faded, 0.5, sepia, 0.5, 0)
    return _vignette(result)


def tone_sepia(frame):
    sepia_kernel = np.array([[0.131, 0.534, 0.272],
                              [0.168, 0.686, 0.349],
                              [0.189, 0.769, 0.393]])
    sepia = cv2.transform(frame, sepia_kernel)
    return np.clip(sepia, 0, 255).astype(np.uint8)


def tone_bw(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = _apply_curve(gray, _build_curve([(0, 0), (90, 60), (170, 200), (255, 255)]))
    return cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)


def tone_vibrant(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV).astype(np.float32)
    hsv[:, :, 1] = np.clip(hsv[:, :, 1] * 1.5, 0, 255)
    hsv[:, :, 2] = np.clip(hsv[:, :, 2] * 1.05, 0, 255)
    frame = cv2.cvtColor(hsv.astype(np.uint8), cv2.COLOR_HSV2BGR)
    return cv2.convertScaleAbs(frame, alpha=1.1, beta=0)


def tone_cinematic(frame):
    # teal shadows, orange highlights - a common film-style grade
    b, g, r = cv2.split(frame.astype(np.float32))
    luma = (0.299 * r + 0.587 * g + 0.114 * b) / 255.0

    shadow_mask = np.clip(1.0 - luma, 0, 1)
    highlight_mask = np.clip(luma, 0, 1)

    # push shadows toward teal (boost blue/green, reduce red)
    b += shadow_mask * 20
    g += shadow_mask * 10
    r -= shadow_mask * 10

    # push highlights toward orange (boost red, reduce blue)
    r += highlight_mask * 18
    b -= highlight_mask * 12

    frame = cv2.merge((b, g, r))
    frame = np.clip(frame, 0, 255).astype(np.uint8)
    return cv2.convertScaleAbs(frame, alpha=1.08, beta=-5)


def _vignette(frame):
    rows, cols = frame.shape[:2]
    kernel_x = cv2.getGaussianKernel(cols, cols * 0.6)
    kernel_y = cv2.getGaussianKernel(rows, rows * 0.6)
    kernel = kernel_y * kernel_x.T
    mask = kernel / kernel.max()
    result = frame.copy().astype(np.float32)
    for c in range(3):
        result[:, :, c] *= mask
    return np.clip(result, 0, 255).astype(np.uint8)


TONES = [
    ("none", tone_none),
    ("warm", tone_warm),
    ("cool", tone_cool),
    ("vintage", tone_vintage),
    ("sepia", tone_sepia),
    ("bw", tone_bw),
    ("vibrant", tone_vibrant),
    ("cinematic", tone_cinematic),
]

# --------------------------------------------------------------------------
# Main loop
# --------------------------------------------------------------------------

def main(camera_index=0):
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        print(f"Could not open camera at index {camera_index}. "
              f"Try a different index (0, 1, 2...) or check camera permissions.")
        return

    os.makedirs("snapshots", exist_ok=True)
    tone_idx = 0
    window_name = "Camera Tones  (1-8 = tone, s = save, q = quit)"

    print("Camera Tones running.")
    print("Keys: 1-8 switch tone, s = save snapshot, q/ESC = quit")
    for i, (name, _) in enumerate(TONES, start=1):
        print(f"  {i}: {name}")

    while True:
        ok, frame = cap.read()
        if not ok:
            print("Failed to read frame from camera.")
            break

        frame = cv2.flip(frame, 1)  # mirror for a natural selfie view
        name, tone_fn = TONES[tone_idx]
        toned = tone_fn(frame)

        label = f"Tone: {name}"
        cv2.putText(toned, label, (15, 30), cv2.FONT_HERSHEY_SIMPLEX,
                    0.8, (0, 0, 0), 4, cv2.LINE_AA)
        cv2.putText(toned, label, (15, 30), cv2.FONT_HERSHEY_SIMPLEX,
                    0.8, (255, 255, 255), 2, cv2.LINE_AA)

        cv2.imshow(window_name, toned)
        key = cv2.waitKey(1) & 0xFF

        if key in (ord('q'), 27):  # q or ESC
            break
        elif ord('1') <= key <= ord('8'):
            idx = key - ord('1')
            if idx < len(TONES):
                tone_idx = idx
                print(f"Switched to tone: {TONES[tone_idx][0]}")
        elif key == ord('s'):
            filename = f"snapshots/{name}_{int(time.time())}.png"
            cv2.imwrite(filename, toned)
            print(f"Saved {filename}")

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()