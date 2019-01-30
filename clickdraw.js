//jmai3
//Jiajie mai

var c = document.getElementById("slate");
var la = document.getElementById("ok");
var ctx = c.getContext("2d");

c.addEventListener("click", draw);
la.addEventListener("click",clear);

function draw(){
	var x = event.clientX;
	var y = event.clientY;
	console.log(x + ":" +  y);
	ctx.fillRect(x,y,50,75);
}

function clear(){
	ctx.clearRect(0,0,c.height,c.width);
}

//window.onload = console.log(c);
//window.onload = console.log(ctx);
//ctx.fillStyle = "#000000";
//ctx.fillRect = "100,100,50,200";
