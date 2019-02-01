//jmai3
//Jiajie mai

var dsize = 5;
var w = 50;
var h = 75;
var subtoggle = 0;

var c = document.getElementById("slate");
var la = document.getElementById("ok");
var ctx = c.getContext("2d");

var d = document.getElementById("dot");
var r = document.getElementById("rect");

var di = document.getElementById("dota");
var dd = document.getElementById("dotm");

var wi = document.getElementById("wa");
var wd = document.getElementById("wm");

var hi = document.getElementById("ha");
var hd = document.getElementById("hm");

var dget = document.getElementById("dsize");
var rget = document.getElementById("rectsize");

var youtube = document.getElementById("prevent");
var toggle = document.getElementById("switch");

toggle.addEventListener("click", rect_dot);

c.addEventListener("click", draw);
la.addEventListener("click",clear);

//d.addEventListener("click",changed);
//r.addEventListener("click",changer);

di.addEventListener("click",dsizeu);
dd.addEventListener("click",dsized);

wi.addEventListener("click",wsizeu);
wd.addEventListener("click",wsized);

hi.addEventListener("click",hsizeu);
hd.addEventListener("click",hsized);

//click this link won't take you to youtube like default
youtube.addEventListener("click",function(event){event.preventDefault();
						 clear();});
//https://stackoverflow.com/questions/3234256/find-mouse-position-relative-to-element

function rect_dot(e){
	
	if(subtoggle == 1){
		subtoggle = 0;
	}else{
		subtoggle = 1;
	}
}

function dsizeu(e){
	dsize += 1;
	var text = "dotsize: " + dsize;
	dget.innerHTML = text;
}

function dsized(e){
	dsize -= 1;
	var text = "dotsize: " + dsize;
	dget.innerHTML = text;
}

function wsizeu(e){
	w += 1;
	var text = "rectangle size: " + w + " x " + h;
	rget.innerHTML = text;
}

function wsized(e){
	w -= 1;
	var text = "rectangle size: " + w + " x " + h;
	rget.innerHTML = text;
}

function hsizeu(e){
	h += 1;
	var text = "rectangle size: " + w + " x " + h;
	rget.innerHTML = text;
}

function hsized(e){
	h -= 1;
	var text = "rectangle size: " + w + " x " + h;
	rget.innerHTML = text;
}

function draw(e){
		//relate to the left edge of the div(canvas) (border counted)
		var x = e.offsetX; //event.clientX;
		//relate to the top edge of the div(canvas) (border counted)
		var y = e.offsetY; //event.clientY;
		console.log(di);
	if(
	//d.value == 1 || 
	subtoggle == 0){
		//began tracing the circle
		ctx.beginPath();
ctx.arc(x, y, dsize, 0, 2 * Math.PI);
ctx.fill();
	}
	if(
	//r.value == 1 || 
	subtoggle == 1){
		ctx.fillRect(x,y,w,h);
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
