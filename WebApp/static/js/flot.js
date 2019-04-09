/*----PlaceHolder1----*/
$(function() {
	var sin = [],
		cos = [];
	for (var i = 0; i < 14; i += 0.1) {
		sin.push([i, Math.sin(i)]);
		cos.push([i, Math.cos(i)]);
	}
	plot = $.plot("#placeholder1", [{
		data: sin
	}, {
		data: cos
	}], {
		series: {
			lines: {
				show: true
			}
		},
		lines: {
			show: true,
			fill: true,
			fillColor: {
				colors: [{
					opacity: 0.9
				}, {
					opacity: 0.9
				}]
			}
		},
		crosshair: {
			mode: "x"
		},
		grid: {
			hoverable: false,
			autoHighlight: false,
			borderColor: "#e9e2e6",
			verticalLines: false,
			horizontalLines: false
		},
		colors: ['#f47b25', '#5d61bf'],
		yaxis: {
			min: -1.2,
			max: 1.2,
			tickLength: 0
		},
		xaxis: {
			tickLength: 0
		}
	});
	
	/*----PlaceHolder2----*/
	var sin = [],
		cos = [];
	for (var i = 0; i < 14; i += 0.5) {
		sin.push([i, Math.sin(i)]);
		cos.push([i, Math.cos(i)]);
	}
	var plot = $.plot("#placeholder2", [{
		data: sin,
		label: "data1"
	}, {
		data: cos,
		label: "data2"
	}], {
		series: {
			lines: {
				show: true
			},
			points: {
				show: true
			}
		},
		grid: {
			hoverable: true,
			clickable: true,
			borderColor: "#e9e2e6",
			verticalLines: false,
			horizontalLines: false
		},
		colors: ['#f47b25', '#5d61bf'],
		yaxis: {
			min: -1.2,
			max: 1.2,
			tickLength: 0
		},
		xaxis: {
			tickLength: 0
		}
	});
	
	/*----PlaceHolder1----*/
	var d1 = [];
	for (var i = 0; i <= 10; i += 1) {
		d1.push([i, parseInt(Math.random() * 30)]);
	}
	var d2 = [];
	for (var i = 0; i <= 10; i += 1) {
		d2.push([i, parseInt(Math.random() * 30)]);
	}
	var d3 = [];
	for (var i = 0; i <= 10; i += 1) {
		d3.push([i, parseInt(Math.random() * 30)]);
	}
	var stack = 0,
		bars = true,
		lines = false,
		steps = false;

	function plotWithOptions() {
		$.plot("#placeholder6", [d1, d2, d3], {
			series: {
				stack: stack,
				lines: {
					show: lines,
					fill: true,
					steps: steps
				},
				bars: {
					show: bars,
					barWidth: 0.8
				}
			},
			grid: {
				borderColor: "#e9e2e6",
			},
			colors: ['#f47b25', '#5d61bf', '#3ebaef'],
			yaxis: {
				tickLength: 0
			},
			xaxis: {
				tickLength: 0,
				show: false
			}
		});
	}
	plotWithOptions();
	$(".stackControls button").click(function(e) {
		e.preventDefault();
		stack = $(this).text() == "With stacking" ? true : null;
		plotWithOptions();
	});
	$(".graphControls button").click(function(e) {
		e.preventDefault();
		bars = $(this).text().indexOf("Bars") != -1;
		lines = $(this).text().indexOf("Lines") != -1;
		steps = $(this).text().indexOf("steps") != -1;
		plotWithOptions();
	});
	
	/*----PlaceHolder----*/
	var data = [],
		series = Math.floor(Math.random() * 4) + 3;
	for (var i = 0; i < series; i++) {
		data[i] = {
			label: "Series" + (i + 1),
			data: Math.floor(Math.random() * 100) + 1
		}
	}
	var placeholder = $("#placeholder");
	placeholder.unbind();
	$("#title").text("Default pie chart");
	$("#description").text("The default pie chart with no options set.");
	$.plot(placeholder, data, {
		series: {
			pie: {
				show: true
			}
		},
		colors: ['#f47b25', '#5d61bf', '#3ebaef', '#31c92e', '#1891f2', '#583a96'],
	});
});


// A custom label formatter used by several of the plots
function labelFormatter(label, series) {
	return "<div style='font-size:8pt; text-align:center; padding:2px; color:white;'>" + label + "<br/>" + Math.round(series.percent) + "%</div>";
}
//
function setCode(lines) {
	$("#code").text(lines.join("\n"));
}