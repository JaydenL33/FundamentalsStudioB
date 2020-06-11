import React, { Component } from 'react';
import * as d3 from 'd3';

export default class BarChart extends Component {

    componentDidMount () {
        this.drawBarChart();
    }
    shouldComponentUpdate () {
        return false;
    }

    drawBarChart()  {

        var svg = d3.select(this.refs.canvas)
            var margin = {top: 10, right: 30, bottom: 20, left: 50},
            width = 460 - margin.left - margin.right,
            height = 400 - margin.top - margin.bottom;

        var g = svg.append("g").attr("transform", "translate(" + margin.left + "," + margin.top + ")");

        // The Scale between the groups.
        var x0 = d3.scaleBand()
        .rangeRound([0, width])
        .paddingInner(0.1);

        // The scale for spacing each group's bar:
        var x1 = d3.scaleBand()
        .padding(0.05);

        var y = d3.scaleLinear()
        .rangeRound([height, 0]);

        var z = d3.scaleOrdinal()
        .range(["#a05d56", "#d0743c", "#ff8c00"]);


        d3.csv("data/CDR.csv", function(d, i, columns) {
            for (var i = 1, n = columns.length; i < n; ++i) d[columns[i]] = +d[columns[i]];
            return d;
        }).then(function(data) {
            console.log(data);
            var keys = data.columns.slice(1);
            console.log("Keys is " + keys)
            x0.domain(data.map(function(d) { return d.State; }));
            x1.domain(keys).rangeRound([0, x0.bandwidth()]);
            y.domain([0, d3.max(data, function(d) { return d3.max(keys, function(key) { return d[key]; }); })]).nice();
            g.append("g")
                .selectAll("g")
                .data(data)
                .enter().append("g")
                .attr("class","bar")
                .attr("transform", function(d) { return "translate(" + x0(d.State) + ",0)"; })
                .selectAll("rect")
                .data(function(d) { return keys.map(function(key) { return {key: key, value: d[key]}; }); })
                .enter().append("rect")
                .attr("x", function(d) { return x1(d.key); })
                .attr("y", function(d) { return y(d.value); })
                .attr("width", x1.bandwidth())
                .attr("height", function(d) { return height - y(d.value); })
                .attr("fill", function(d) { return z(d.key); });
            g.append("g")
                .attr("class", "axis")
                .attr("transform", "translate(0," + height + ")")
                .call(d3.axisBottom(x0));
            g.append("g")
                .attr("class", "y axis")
                .call(d3.axisLeft(y).ticks(null, "s"))
                .append("text")
                .attr("x", 2)
                .attr("y", y(y.ticks().pop()) + 0.5)
                .attr("dy", "0.32em")
                .attr("fill", "#000")
                .attr("font-weight", "bold")
                .attr("text-anchor", "start")
                .text("Population");
                var legend = g.append("g")
                .attr("font-family", "sans-serif")
                .attr("font-size", 10)
                .attr("text-anchor", "end")
                .selectAll("g")
                .data(keys.slice().reverse())
                .enter().append("g")
                .attr("transform", function(d, i) { return "translate(0," + i * 20 + ")"; });
    
            legend.append("rect")
                .attr("x", width - 17)
                .attr("width", 15)
                .attr("height", 15)
                .attr("fill", z)
                .attr("stroke", z)
                .attr("stroke-width",2);
    
            legend.append("text")
                .attr("x", width - 24)
                .attr("y", 9.5)
                .attr("dy", "0.32em")
                .text(function(d) { return d; });
                }
            )
        }

    render() {
        return (
            <svg className="line-container" width={"600"} height={"600"} ref={this.props.ref} />
        )
    }
}

BarChart.defaultProps = {
    ref: "canvas"
}

// .append("svg")
// .attr("width", canvasWidth)
// .attr("height", canvasHeight)
// .style("border", "1px solid black")
// svgCanvas.selectAll("rect")
// .data(data).enter()
//     .append("rect")
//     .attr("width", 40)
//     .attr("height", (datapoint) => datapoint * scale)
//     .attr("fill", "orange")
//     .attr("x", (datapoint, iteration) => iteration * 45)
//     .attr("y", (datapoint) => canvasHeight - datapoint * scale)

// console.log(data);
// // List of subgroups = header of the csv files = soil condition here
// var subgroups = data;
// // List of groups = species here = value of the first column called group -> I show them on the X axis
// var countries = d3.map(data, function(d){return(d.Country)}).keys()

// // Add X axis
// var x = d3.scaleBand()
//     .domain(countries)
//     .range([0, canvasWidth])
//     .padding([0.2])
// svgCanvas.append("g")
//     .attr("transform", "translate(0," + canvasHeight + ")")
//     .call(d3.axisBottom(x).tickSizeOuter(0));

// // Add Y axis
// var y = d3.scaleLinear()
//     .domain([0, 5500000])
//     .range([ canvasHeight, 0 ]);
// svgCanvas.append("g")
//     .call(d3.axisLeft(y));

// // color palette = one color per subgroup
// var color = d3.scaleOrdinal()
//     .domain(subgroups)
//     .range(['#e41a1c','#377eb8','#4daf4a'])

// //stack the data? --> stack per subgroup
// var stackedData = d3.stack()
//     .keys(subgroups)
//     (data)

// // Show the bars
// svgCanvas.append("g")
//     .selectAll("g")
//     // Enter in the stack data = loop key per key = group per group
//     .data(stackedData)
//     .enter().append("g")
//     .attr("fill", function(d) { return color(d.key); })
//     .selectAll("rect")
//     // enter a second time = loop subgroup per subgroup to add all rectangles
//     .data(function(d) { return d; })
//     .enter().append("rect")
//         .attr("x", function(d) { return x(d.data.Country); })
//         .attr("y", function(d) { return y(d[1]); })
//         .attr("canvasHeight", function(d) { return y(d[0]) - y(d[1]); })
//         .attr("canvasWidth",x.bandwidth())