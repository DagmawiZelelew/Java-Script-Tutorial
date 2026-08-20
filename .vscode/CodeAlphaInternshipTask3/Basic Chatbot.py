
def get_response(user_input):
    """Return a predefined reply based on user input."""
    user_input = user_input.lower().strip()

    if user_input == "hello" or user_input == "hi":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "what is your name" or user_input == "who are you":
        return "I'm a simple chatbot created in Python!"
    elif user_input == "what can you do":
        return "I can chat with you about simple things. Try asking how I am!"
    elif user_input == "thank you" or user_input == "thanks":
        return "You're welcome!"
    elif user_input == "help":
        return "You can say things like: hello, how are you, what is your name, thanks, or bye."
    elif user_input == "who created you":
        return "I was created as a simple Python project!"
    elif user_input == "what time is it":
        return "Sorry, I can't check the time yet — but I'm working on it!"
    elif user_input == "tell me a joke":
        return "Why don't programmers like nature? It has too many bugs!"
    elif user_input == "bye" or user_input == "goodbye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that. Type 'help' to see what I can do."

def chatbot():
    """Run the chatbot loop until the user says bye."""
    print("Chatbot: Hi! Type 'help' to see what I can do, or 'bye' to exit.")

    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Chatbot:", response)

        if user_input.lower().strip() in ("bye", "goodbye"):
            break

if __name__ == "__main__":
    chatbot()