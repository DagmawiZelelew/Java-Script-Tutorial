let timeoutID;
function timer(){
timeoutID = setTimeout(function(){
    window.alert("HEYYY BUDDYYY!");
    console.log("started")
},3000)}

function stop(){
    clearTimeout(timeoutID)
    console.log("Cancelled")
}

