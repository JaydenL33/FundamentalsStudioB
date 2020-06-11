Popular / AboutGerardo Perez’s Block 6bafeb64181d87750dbdba78f8678715
Updated October 9, 2018
Grouped Bar Chart Toggle Series, update for d3v5

Open
forked from flacoman91's block: Grouped Bar Chart Toggle Series, update for d3v5

index.html#
<!DOCTYPE html>
<style>

    .axis .domain {
        display: none;
    }

</style>
<svg width="960" height="500"></svg>
<script src="https://d3js.org/d3.v5.min.js"></script>
<script>

    var svg = d3.select("svg"),
        margin = {top: 20, right: 20, bottom: 30, left: 40},
        width = +svg.attr("width") - margin.left - margin.right,
        height = +svg.attr("height") - margin.top - margin.bottom,
        g = svg.append("g").attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    // The scale spacing the groups:
    var x0 = d3.scaleBand()
        .rangeRound([0, width])
        .paddingInner(0.1);

    // The scale for spacing each group's bar:
    var x1 = d3.scaleBand()
        .padding(0.05);

    var y = d3.scaleLinear()
        .rangeRound([height, 0]);

    var z = d3.scaleOrdinal()
        .range(["#98abc5", "#8a89a6", "#7b6888", "#6b486b", "#a05d56", "#d0743c", "#ff8c00"]);

    d3.csv("data.csv", function(d, i, columns) {
        for (var i = 1, n = columns.length; i < n; ++i) d[columns[i]] = +d[columns[i]];
        return d;
    }).then(function(data) {
        console.log(data);

        var keys = data.columns.slice(1);

        console.log('keys');
        console.log(keys);
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
            .attr("stroke-width",2)
            .on("click",function(d) { update(d) });

        legend.append("text")
            .attr("x", width - 24)
            .attr("y", 9.5)
            .attr("dy", "0.32em")
            .text(function(d) { return d; });

        var filtered = [];

        ////
        //// Update and transition on click:
        ////

        function update(d) {

            //
            // Update the array to filter the chart by:
            //

            // add the clicked key if not included:
            if (filtered.indexOf(d) == -1) {
                filtered.push(d);
                // if all bars are un-checked, reset:
                if(filtered.length == keys.length) filtered = [];
            }
            // otherwise remove it:
            else {
                filtered.splice(filtered.indexOf(d), 1);
            }

            //
            // Update the scales for each group(/states)'s items:
            //
            var newKeys = [];
            keys.forEach(function(d) {
                if (filtered.indexOf(d) == -1 ) {
                    newKeys.push(d);
                }
            })
            x1.domain(newKeys).rangeRound([0, x0.bandwidth()]);
            y.domain([0, d3.max(data, function(d) { return d3.max(keys, function(key) { if (filtered.indexOf(key) == -1) return d[key]; }); })]).nice();

            // update the y axis:
            svg.select(".y")
                .transition()
                .call(d3.axisLeft(y).ticks(null, "s"))
                .duration(500);


            //
            // Filter out the bands that need to be hidden:
            //
            var bars = svg.selectAll(".bar").selectAll("rect")
                .data(function(d) { return keys.map(function(key) { return {key: key, value: d[key]}; }); })

            bars.filter(function(d) {
                    return filtered.indexOf(d.key) > -1;
                })
                .transition()
                .attr("x", function(d) {
                    return (+d3.select(this).attr("x")) + (+d3.select(this).attr("width"))/2;
                })
                .attr("height",0)
                .attr("width",0)
                .attr("y", function(d) { return height; })
                .duration(500);

            //
            // Adjust the remaining bars:
            //
            bars.filter(function(d) {
                    return filtered.indexOf(d.key) == -1;
                })
                .transition()
                .attr("x", function(d) { return x1(d.key); })
                .attr("y", function(d) { return y(d.value); })
                .attr("height", function(d) { return height - y(d.value); })
                .attr("width", x1.bandwidth())
                .attr("fill", function(d) { return z(d.key); })
                .duration(500);


            // update legend:
            legend.selectAll("rect")
                .transition()
                .attr("fill",function(d) {
                    if (filtered.length) {
                        if (filtered.indexOf(d) == -1) {
                            return z(d);
                        }
                        else {
                            return "white";
                        }
                    }
                    else {
                        return z(d);
                    }
                })
                .duration(100);


        }

    });

</script>
data.csv#
State,Under 5 Years,5 to 13 Years,14 to 17 Years,18 to 24 Years,25 to 44 Years,45 to 64 Years,65 Years and Over
CA,2704659,4499890,2159981,3853788,10604510,8819342,4114496
TX,2027307,3277946,1420518,2454721,7017731,5656528,2472223
NY,1208495,2141490,1058031,1999120,5355235,5120254,2607672
FL,1140516,1938695,925060,1607297,4782119,4746856,3187797
IL,894368,1558919,725973,1311479,3596343,3239173,1575308
PA,737462,1345341,679201,1203944,3157759,3414001,1910571
LICENSE#
Released under the The MIT License.