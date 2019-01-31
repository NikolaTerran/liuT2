//jmai3
//Jiajie mai

var c = document.getElementById("slate");
var la = document.getElementById("ok");
var ctx = c.getContext("2d");

var d = document.getElementById("dot");
var r = document.getElementById("rect");

c.addEventListener("click", draw);
la.addEventListener("click",clear);

d.addEventListener("click",changed);
r.addEventListener("click",changer);

//https://stackoverflow.com/questions/3234256/find-mouse-position-relative-to-element

function draw(e){
		var x = e.pageX - c.offsetLeft - 10; //event.clientX;
		var y = e.pageY - c.offsetTop - 10; //event.clientY;
		console.log(e.pageX + ":" + c.offsetX);
	if(d.value == 1){
		//began tracing the circle
		ctx.beginPath();
ctx.arc(x, y, 5, 0, 2 * Math.PI);
ctx.fill();
	}
	if(r.value == 1){
		ctx.fillRect(x,y,50,75);
	}
}

function clear(){
	ctx.clearRect(0,0,c.height,c.width);
}

function changed(){
	d.setAttribute("style","background-color:red");
	d.setAttribute("value",1);
	r.setAttribute("style","background-color:white");
	r.setAttribute("value",0);
}

function changer(){
	r.setAttribute("style","background-color:red");
	r.setAttribute("value",1);
	d.setAttribute("style","background-color:white");
	d.setAttribute("value",0);
}

//window.onload = console.log(c);
//window.onload = console.log(ctx);
//ctx.fillStyle = "#000000";
//ctx.fillRect = "100,100,50,200";
