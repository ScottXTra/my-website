function test(){
    console.log('Hello World');
}

function addNumbers(){
    var a = document.getElementById("box1").value;
    var b = document.getElementById("box2").value;
    var c = document.getElementById("box3");
    c.value = Number(a) + Number(b);
    return c.value;
}