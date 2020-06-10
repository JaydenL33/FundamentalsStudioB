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
        const canvasHeight = 400
        const canvasWidth = 600
        const scale = 20
        const svgCanvas = d3.select(this.refs.canvas);

        d3.csv("https://raw.githubusercontent.com/holtzy/D3-graph-gallery/master/DATA/data_stacked.csv", function(data) {
        // List of subgroups = header of the csv files = soil condition here
        var subgroups = data.columns.slice(1)

        // List of groups = species here = value of the first column called group -> I show them on the X axis
        var countries = d3.map(data, function(d){return(d.Country)}).keys()

        // Add X axis
        var x = d3.scaleBand()
            .domain(countries)
            .range([0, canvasWidth])
            .padding([0.2])
        svgCanvas.append("g")
            .attr("transform", "translate(0," + canvasHeight + ")")
            .call(d3.axisBottom(x).tickSizeOuter(0));

        // Add Y axis
        var y = d3.scaleLinear()
            .domain([0, 5500000])
            .range([ canvasHeight, 0 ]);
        svgCanvas.append("g")
            .call(d3.axisLeft(y));

        // color palette = one color per subgroup
        var color = d3.scaleOrdinal()
            .domain(subgroups)
            .range(['#e41a1c','#377eb8','#4daf4a'])

        //stack the data? --> stack per subgroup
        var stackedData = d3.stack()
            .keys(subgroups)
            (data)

        // Show the bars
        svgCanvas.append("g")
            .selectAll("g")
            // Enter in the stack data = loop key per key = group per group
            .data(stackedData)
            .enter().append("g")
            .attr("fill", function(d) { return color(d.key); })
            .selectAll("rect")
            // enter a second time = loop subgroup per subgroup to add all rectangles
            .data(function(d) { return d; })
            .enter().append("rect")
                .attr("x", function(d) { return x(d.data.Country); })
                .attr("y", function(d) { return y(d[1]); })
                .attr("canvasHeight", function(d) { return y(d[0]) - y(d[1]); })
                .attr("canvasWidth",x.bandwidth())
            })
        }

    render() {
        return (
            <div className="line-container" ref={this.props.ref} />
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