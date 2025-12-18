function changeText(){
    document.getElementById("message").innerText = "Text changed"
}

function changeColor(){
    document.getElementById("message").style.color = "red"
}

function showText(){
    let name = document.getElementById("name").value;
    document.getElementById("title").innerText = "Hello, "+ name
}