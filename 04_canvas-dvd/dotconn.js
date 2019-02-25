//Tianrun Liu

//SoftDev2 pd6

//K #03: They lock us in the tower whenever we get caught ...which is often

//2019-02-04    


//jmai3
//Jiajie mai

//global state variable
var color = "#000000";

// drawing state var
var dsize = 5;
var w = 50;
var h = 75;
var subtoggle = 0;

//saved line coordinates
var oldx, oldy;
var newx, newy;

// anime state var
var start_time = null;
var radius = 0.1;
var ani_state = 0;

//general selections
var red = document.getElementById("red");
var orange = document.getElementById("orange");
var yellow = document.getElementById("yellow");
var green = document.getElementById("green");
var cyan = document.getElementById("cyan");
var blue = document.getElementById("blue");
var purple = document.getElementById("purple");
var black = document.getElementById("black");
var white = document.getElementById("white");
//var red = document.getElementById("red");


//draw element selections
var c = document.getElementById("playground");
var la = document.getElementById("clear");
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


//anime element selection
var anime = document.getElementById("anime");
var starto = document.getElementById("ani_start");
var stop = document.getElementById("stop");
var dvd_button = document.getElementById("dvd");

var ani_con = anime.getContext("2d");



// event listening


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

starto.addEventListener("click",draw_circle);
stop.addEventListener("click", stop_ani);
dvd_button.addEventListener("click",function(){cur_x = Math.random() * 500;
cur_y = Math.random() * 500;dvd_ani();});


//https://stackoverflow.com/questions/256754/how-to-pass-arguments-to-addeventlistener-listener-function
red.addEventListener("click",function(){poison(1);});
orange.addEventListener("click",function(){poison(2);});
yellow.addEventListener("click",function(){poison(3);});
green.addEventListener("click",function(){poison(4);});
cyan.addEventListener("click",function(){poison(5);});
blue.addEventListener("click",function(){poison(6);});
purple.addEventListener("click",function(){poison(7);});
black.addEventListener("click",function(){poison(8);});
white.addEventListener("click",function(){poison(9);});





//click this link won't take you to youtube like default
youtube.addEventListener("click",function(event){event.preventDefault();
						 clear();});
//https://stackoverflow.com/questions/3234256/find-mouse-position-relative-to-element


//anime stuff
	
//
function foo(){
	console.log("foo");
}

var progress;
var id;

	//dvd stuff
	var x_move = 1;
	var y_move = 1;
	var cur_x = 200;
	var cur_y = 50;
	var border_x = 170;
	var border_y = 150;
	
	//https://stackoverflow.com/questions/23830471/convert-image-color-without-changing-its-transparent-background
	//var imageData=context.getImageData(0,0,canvas.width,canvas.height);
	//var data=imageData.data;
	
	
	function dvd_ani(){
		cancelAnimationFrame(id);
	    ani_con.clearRect(0,0,anime.height,anime.width);
		drawing = new Image();
		drawing.src = "image.png";
		if(cur_x + border_x >= anime.width){
			x_move = -1;
		}
		
		if(cur_x <= 0){
			x_move = 1;
		}
		
		if(cur_y + border_y >= anime.height){
			y_move = -1;
		}
		
		if(cur_y + 50 <= 0){
			y_move = 1;
		}
		
		ani_con.drawImage(drawing,cur_x,cur_y);
		cur_x += x_move;
		cur_y += y_move;
		id = requestAnimationFrame(dvd_ani);
	}

function poison(x){
	switch(x){
		case 1: color = "#FF0000";
		break; 	
		case 2: color = "#FFA500";
		break;
		case 3: color = "#FFFF00";
		break;
		case 4: color = "#008000";
		break;
		case 5: color = "#00FFFF";
		break;
		case 6: color = "#0000FF";
		break;
		case 7: color = "#800080";
		break;
		case 8: color = "#000000";
		break;
		case 9: color = "#FFFFFF";
		break;
		case 10:
		break;
		case 11:
		break;
	}
	return x;
}

function draw_circle(timestamp){
	cancelAnimationFrame(id);
	//console.log(timestamp);
	if(!start_time){
		start_time = timestamp;
	}
	progress = timestamp - start_time;
	ani_con.clearRect(0,0,anime.height,anime.width);
	ani_con.beginPath();
	try{
		ani_con.arc(anime.height/2,anime.width/2, radius , 0 , 2 * Math.PI);
		ani_con.stroke();
		ani_con.fillStyle = color;
		ani_con.fill();
	}catch{}
	if(radius >= (anime.width/2)){
		ani_state = 1;
		//radius += 0.1;
	}
	
	if(radius < 0){
		ani_state = 0;
	}
	
	if(ani_state == 1){
		radius -= 0.5;
	}else{
		radius += 0.5;
	}
	
	   id = requestAnimationFrame(draw_circle);
}

function stop_ani(){
	cancelAnimationFrame(id);
}


//////////////////////////////////////////////////////
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
		ctx.fillStyle = color;
		ctx.fill();
		if(typeof oldx == 'undefined'){
			oldx = x;
			oldy = y;
			console.log(oldx + ":" + oldy);
		}else{
			ctx.beginPath();
			newx = x;
			newy = y;
			ctx.moveTo(oldx,oldy);
			ctx.lineTo(newx,newy);
			ctx.strokeStyle = color;
			ctx.stroke();
			oldx = x;
			oldy = y;
			console.log(oldx + ":" + oldy + ":" + newx + ":" + newy);
		}
		
	}
	if(
	//r.value == 1 || 
	subtoggle == 1){
		ctx.fillRect(x,y,w,h);
	}
}

function clear(){
	ctx.clearRect(0,0,c.height,c.width);
	oldx = 'undefined';
	oldy = 'undefined';
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
