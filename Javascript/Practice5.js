let time = document.getElementById("clock")
function updateClock(){
    const curr = new Date();
    const hours = curr.getHours().toString().padStart(2,0);
    const minutes = curr.getMinutes().toString().padStart(2,0);
    const seconds = curr.getSeconds().toString().padStart(2,0); 
    time.textContent = `${hours} : ${minutes} : ${seconds}`
     

}
updateClock();
setInterval(updateClock,1000);

