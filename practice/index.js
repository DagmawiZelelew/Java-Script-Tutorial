const input = document.getElementById("userinput");
const submit = document.getElementById("submitbutton");
const checkboxcf = document.getElementById("checkboxcf");
const checkboxfc = document.getElementById("checkboxfc");
const text = document.getElementById("text")
let temp;

// ----------------------------------------------
function f1(){
submit.onclick = function(){
    const value = Number(input.value)
    if(isNaN(value)){
        text.textContent = "Please, Enter a valid number";
        return;

    }
    if(checkboxcf.checked){
        temp = input.value*1.8 + 32;
        text.textContent = `The answer is ${temp.toFixed(1)} F⁰`;
    }
        else if( checkboxfc.checked) {
        temp = (input.value -32) /1.8;
        text.textContent = `The answer is ${temp.toFixed(1)} C⁰`;
    }
    else{
        text.textContent = "Please, Select a conversion.";
    }
}
}
f1();
