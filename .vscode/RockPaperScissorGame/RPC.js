const rock = document.getElementById("rock");
const paper = document.getElementById("paper");
const scissor = document.getElementById("scissor");
const arr= ["rock","paper","scissor"];
let result= document.getElementById("result");
let ai;
const restart = document.getElementById("restart");
let woncount = 0;
let lostcount=0;
let drawcount=0;
const end = document.getElementById("end");
let won = document.getElementById("won");
let draw = document.getElementById("draw");
let lost = document.getElementById("lost");
let gameover = false;

//---------------------------------------------------------------
function restartGame(){
    woncount = 0;
    lostcount = 0;
    drawcount = 0;

    gameover = false;

    result.textContent = "Game restarted! Choose Rock, Paper, or Scissors.";

    rock.disabled = false;
    paper.disabled = false;
    scissor.disabled = false;

    won.textContent = "";
    draw.textContent = "";
    lost.textContent = "";
}
restart.onclick = function(){
    restartGame();
}



rock.onclick = function(){
    if(gameover) return;

    
ai =arr[ Math.floor(Math.random()*arr.length)];
if(ai === "paper"){
    result.textContent = `You lost! I chose 📄 Paper`;
     lostcount++;
}
else if (ai === "rock"){
    result.textContent = `Thats a tie!  also chose 🪨 Rock`;
    drawcount++;
}
else{
    result.textContent = `You Won! I chose ✂️ Scissors`;
    woncount++;
}
checkwinner();

}
//-------------------------------------------------------

paper.onclick = function(){
    if(gameover) return;
    ai =arr[ Math.floor(Math.random()*arr.length)];
if(ai === "scissor"){
    result.textContent = `You lost! I chose ✂️ Scissors`;
    lostcount++;
}
else if (ai === "paper"){
    result.textContent = `Thats a tie! I also chose 📄 Paper `;
    drawcount++;
}
else{
    result.textContent = `You Won! I chose 🪨 Rock `;
    woncount++;

}
checkwinner();

}
// -----------------------------------------------------------------

scissor.onclick = function(){
    if(gameover) return;
    ai =arr[ Math.floor(Math.random()*arr.length)];
if(ai === "rock"){
    result.textContent = `You lost! I chose 🪨 Rock`;
    lostcount++;
}
else if (ai === "scissor"){
    result.textContent = `Thats a tie! I chose ✂️ Scissors`;
    drawcount++;
}
else{
    result.textContent = `You Won! I chose 📄 Paper `;
    woncount++;

}
checkwinner();
}

end.onclick = function(){
    won.textContent = woncount;
    draw.textContent = drawcount;
    lost.textContent = lostcount;
}
function checkwinner(){
if(woncount===5){
    result.textContent = `You reached 5! You won!!! Congrats!`
    gameover= true;


}
else if(lostcount===5){
    result.textContent = `I won! Lets pay again!`
    gameover = true;
}
}
