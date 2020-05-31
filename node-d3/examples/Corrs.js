const D3Node = require('../src')
const fs = require('fs')
const d3 = require('d3')
const csvString = fs.readFileSync('examples/data/Corr.csv', 'UTF-8').toString()

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

// Graph dimension
var margin = {top: 20, right: 20, bottom: 20, left: 20},
    width = 430 - margin.left - margin.right,
    height = 430 - margin.top - margin.bottom
    const svgWidth = width + margin.left + margin.right
    const svgHeight = height + margin.top + margin.bottom
// Create the svg area
var svg = d3n.createSVG(svgWidth, svgHeight)
  .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");


var data = d3.csvParse(csvString); 
var rows = d3.csvParse(csvString); 
  // Going from wide to long format
  var data = [];
  rows.forEach(function(d) {
    var x = d[""];
    delete d[""];
    for (prop in d) {
      var y = prop,
        value = d[prop];
      data.push({
        x: x,
        y: y,
        value: +value
      });
    }
  });

  // List of all variables and number of them
  var domain = d3.set(data.map(function(d) { return d.x })).values()
  var num = Math.sqrt(data.length)

  // Create a color scale
  var color = d3.scaleLinear()
    .domain([-1, 0, 1])
    .range(["#B22222", "#fff", "#000080"]);

  // Create a size scale for bubbles on top right. Watch out: must be a rootscale!
  var size = d3.scaleSqrt()
    .domain([0, 1])
    .range([0, 9]);

  // X scale
  var x = d3.scalePoint()
    .range([0, width])
    .domain(domain)

  // Y scale
  var y = d3.scalePoint()
    .range([0, height])
    .domain(domain)

  // Create one 'g' element for each cell of the correlogram
  var cor = svg.selectAll(".cor")
    .data(data)
    .enter()
    .append("g")
      .attr("class", "cor")
      .attr("transform", function(d) {
        return "translate(" + x(d.x) + "," + y(d.y) + ")";
      });

  // Low left part + Diagonal: Add the text with specific color
  cor
    .filter(function(d){
      var ypos = domain.indexOf(d.y);
      var xpos = domain.indexOf(d.x);
      return xpos <= ypos;
    })
    .append("text")
      .attr("y", 5)
      .text(function(d) {
        if (d.x === d.y) {
          return d.x;
        } else {
          return d.value.toFixed(2);
        }
      })
      .style("font-size", 11)
      .style("text-align", "center")
      .style("fill", function(d){
        if (d.x === d.y) {
          return "#000";
        } else {
          return color(d.value);
        }
      });


  // Up right part: add circles
  cor
    .filter(function(d){
      var ypos = domain.indexOf(d.y);
      var xpos = domain.indexOf(d.x);
      return xpos > ypos;
    })
    .append("circle")
      .attr("r", function(d){ return size(Math.abs(d.value)) })
      .style("fill", function(d){
        if (d.x === d.y) {
          return "#000";
        } else {
          return color(d.value);
        }
      })
      .style("opacity", 0.8)



// create output files
require('./lib/output')('Corr_plot', d3n)
