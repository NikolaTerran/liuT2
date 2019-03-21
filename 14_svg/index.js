				function init(){
					var body = d3.select("body");
					var div = body.append("div");
						div.html("https://stackoverflow.com/questions/18972460/d3-bar-graph-example-not-working-locally/18973278#18973278");
					d3.select("body")
					    .style("color", "green")
					    .style("background-color", "black");

					var data = [4, 8, 15, 16, 23, 42];

					var width = 420,
					    barHeight = 20;

					var x = d3.scaleLinear()
					    .range([0, width]);

					var chart = d3.select(".chart")
					    .attr("width", width);

					d3.tsv("index.tsv", function(error,data) {
					  console.log("hello");
					  
					  x.domain([0, d3.max(data, function(d) { return d.value; })]);

					  chart.attr("height", barHeight * data.length);

					  
					  var bar = chart.selectAll("g")
					      .data(data)
					    .enter().append("g")
					      .attr("transform", function(d, i) { return "translate(0," + i * barHeight + ")"; });

					  bar.append("rect")
					      .attr("width", function(d) { return x(d.value); })
					      .attr("height", barHeight - 1);

					  bar.append("text")
					      .attr("x", function(d) { return x(d.value) - 3; })
					      .attr("y", barHeight / 2)
					      .attr("dy", ".35em")
					      .text(function(d) { return d.value; });
					
					});
					
					function type(d) {
					  d.value = +d.value; // coerce to number
					  return d;
					}
					
					
				}
				
				window.onload = init();


  
				 