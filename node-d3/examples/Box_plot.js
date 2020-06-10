const D3Node = require('../src')
const fs = require('fs')
const d3 = require('d3')
const csvString = fs.readFileSync('examples/data/CTY_SCAT.csv', 'UTF-8').toString()

const styles = `
.bar rect {
  fill: steelblue;
}

.bar text {
  fill: #fff;
  font: 10px sans-serif;
}`

var options = {
  svgStyles: styles,
  d3Module: d3
}

var d3n = new D3Node(options)

//Start D3 code
// set the dimensions and margins of the graph
var margin = {top: 10, right: 30, bottom: 30, left: 60},
    width = 1000 - margin.left - margin.right,
    height = 400 - margin.top - margin.bottom;

const svgWidth = width + margin.left + margin.right
const svgHeight = height + margin.top + margin.bottom

// append the svg object to the body of the page
var svg = d3n.createSVG(svgWidth, svgHeight)
  .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform",
          "translate(" + margin.left + "," + margin.top + ")");

//Read the data
var data = d3.csvParse(csvString);

  // Add X axis
  var x = d3.scaleLinear()
    .domain([0, 200000])
    .range([ 0, width ]);
  svg.append("g")
    .attr("transform", "translate(0," + height + ")")
    .call(d3.axisBottom(x));

  // Add Y axis
  var y = d3.scaleLinear()
    .domain([0, 400000])
    .range([ height, 0]);
  svg.append("g")
    .call(d3.axisLeft(y));

  // Color scale: give me a specie name, I return a color
  var color = d3.scaleOrdinal()
    .domain(["China", "United Kingdom", "United States" ])
    .range([ "#440154ff", "#21908dff", "#fde725ff"])


  // Highlight the specie that is hovered
  var highlight = function(d){

    selected_specie = d.Species

    d3.selectAll(".dot")
      .transition()
      .duration(200)
      .style("fill", "lightgrey")
      .attr("r", 3)

    d3.selectAll("." + selected_specie)
      .transition()
      .duration(200)
      .style("fill", color(selected_specie))
      .attr("r", 7)
  }

  // Highlight the specie that is hovered
  var doNotHighlight = function(){
    d3.selectAll(".dot")
      .transition()
      .duration(200)
      .style("fill", "lightgrey")
      .attr("r", 5 )
  }

  // Add dots
  svg.append('g')
    .selectAll("dot")
    .data(data)
    .enter()
    .append("circle")
      .attr("class", function (d) { return "dot " + d.Species } )
      .attr("cx", function (d) { return x(d.Sepal_Width); } )
      .attr("cy", function (d) { return y(d.Sepal_Length); } )
      .attr("r", 5)
      .style("fill", function (d) { return color(d.Species) } )
    .on("mouseover", highlight)
    .on("mouseleave", doNotHighlight )


// create output files
require('./lib/output')('Scatter_plot', d3n)
