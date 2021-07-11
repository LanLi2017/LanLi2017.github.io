var Chart = {
    display: function (csv_p, country) {

        var margin = {top: 10, right: 30, bottom: 30, left: 80},
            width = 600 - margin.left - margin.right,
            height = 500 - margin.top - margin.bottom;

        var svg = d3.select("#my_dataviz")
            .html("")
            .append("svg")
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
            .append("g")
            .attr("transform",
                "translate(" + margin.left + "," + margin.top + ")");
        var parseDate = d3.timeParse('%m/%d/%Y');
        var dateFormat = d3.utcFormat('%m/%d');
        //"transpose_ds/who_covid_19_China_transpose.csv"
        d3.csv(csv_p,

            function (d) {
                return {date: parseDate(d.date), value: d.value}
            },

            function (data) {
                // Add X axis --> it is a date format
                var x = d3.scaleTime()
                    .domain(d3.extent(data, function (d) {
                        return d.date;
                    }))
                    .range([0, width]);
                svg.append("g")
                    .attr("transform", "translate(0," + height + ")")
                    .call(d3.axisBottom(x).tickFormat(dateFormat));

                // Add Y axis
                var y = d3.scaleLinear()
                    .domain([0, d3.max(data, function (d) {
                        return +d.value;
                    })])
                    .range([height, 0]);
                svg.append("g")
                    .call(d3.axisLeft(y));

                // Add the line
                svg.append("path")
                    .datum(data)
                    .attr("fill", "none")
                    .attr("stroke", "steelblue")
                    .attr("stroke-width", 1.5)
                    .attr("d", d3.line()
                        .x(function (d) {
                            return x(d.date)
                        })
                        .y(function (d) {
                            return y(d.value)
                        })
                    );
                // add labels
                svg.append('text')
                    .attr('transform', 'translate(' + (width / 2.5) + ',' + (height + margin.bottom) + ')')
                    .text('Date of Year 2020');

                svg.append('text')
                    .attr('transform', 'rotate(-90)')
                    .attr('dx', '-15em')
                    .attr('dy', '-3.5em')
                    .text('Number of Confirmed Cases');

            });
        drawAnnotation(country);

        function drawAnnotation(country) {
            var highlight="";
            var x = 20;
            var y = 40;
            if(country === 'China'){
                highlight = "The confirmed cases break out on 01/28";
                x = 10;
                y = 450;
            }
            else if (country === 'US'){
                highlight = "The confirmed cases break out on 03/15";
                x = 40;
                y = 450;

            }

            else if (country === 'Turkey'){
                highlight =  "The confirmed cases break out happened on 03/18";
                x = 60;
                y = 450;
            }

            else if (country === "Haiti"){
                highlight = "The confirmed cases break out around 05/05";
                x = 120;
                y = 450;
            }

          var annotation = svg.append('g');
          annotation.append('text')
            .attr('x', x)
            .attr('y', y)
            .classed('annotation', true)
            .text(highlight);
          // annotation.append('rect')
          //   .attr('x', 60)
          //   .attr('y', 380)
          //   .attr('width', 400)
          //   .attr('height', 20)
          //   .classed('annotation', true);
    }

    }
}

