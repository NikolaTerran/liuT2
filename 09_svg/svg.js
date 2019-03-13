var pic = document.getElementById("vimage");
/*
var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
c.setAttribute("cx",0);
c.setAttribute("cy",0);
c.setAttribute("r", "100");
c.setAttribute("fill","red");
c.setAttribute("stroke","black");
*/
pic.addEventListener("click",draw);

var x0 = 10110;
var y0 = 10110;

function draw(event){
	var dot = document.createElementNS("http://www.w3.org/2000/svg","circle");
	dot.setAttribute("cx",event.offsetX);
	dot.setAttribute("cy",event.offsetY);
	dot.setAttribute("r",5);
	dot.setAttribute("fill","red");
	pic.appendChild(dot);
	if(x0 == 10110){
		x0 = event.offsetX;
		y0 = event.offsetY;
	}else{
		var line = document.createElementNS("http://www.w3.org/2000/svg","line");
		line.setAttribute("x1",x0);
		line.setAttribute("y1",y0);
		line.setAttribute("x2",event.offsetX);
		line.setAttribute("y2",event.offsetY);
		line.setAttribute("stroke","red");
		y0 = event.offsetY;
		x0 = event.offsetX;
		pic.appendChild(line);
	}
}

var b = document.getElementById("b");
b.addEventListener("click",clear);

function clear(event){
	while(pic.lastChild){
		pic.removeChild(pic.lastChild);
	}
}
//pic.appendChild(c);

