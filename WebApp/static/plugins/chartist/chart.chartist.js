$(function() {
	/************ LINE CHART 1 ***************/
	var line1 = new Chartist.Line('#chartLine1', {
		labels: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],
		series: [
			[16, 14, 12, 10, 8, 4, 2]
		]
	}, {
		plugins: [
			Chartist.plugins.tooltip()
		]
	}, {
		high: 40,
		axisY: {
			onlyInteger: true
		},
		fullWidth: true,
		chartPadding: {
			bottom: 0,
			left: 0
		},
		
	});
	/*********** LINE CHART 2 ******************/
	var line2 = new Chartist.Line('#chartLine2', {
		labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
		series: [
			[12, 9, 7, 8, 5],
			[2, 1, 5, 7, 3],
			[1, 3, 4, 5, 6]
		]
	}, {
		plugins: [
			Chartist.plugins.tooltip()
		]
	}, {
		high: 30,
		axisY: {
			onlyInteger: true
		},
		fullWidth: true,
		chartPadding: {
			bottom: 0,
			left: 0
		}
	});
	/*********************** AREA CHART 1 *********************/
	var area1 = new Chartist.Line('#chartArea1', {
		labels: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],
		series: [
			[6, 3, 2, 3, 4, 8, 6, 2, 7, 5, 3]
		]
	}, {
		plugins: [
			Chartist.plugins.tooltip()
		]
	}, {
		high: 40,
		low: 0,
		axisY: {
			onlyInteger: true
		},
		showArea: true,
		fullWidth: true,
		chartPadding: {
			bottom: 0,
			left: 0
		}
	});
	var area2 = new Chartist.Line('#chartArea2', {
		labels: [1, 2, 3, 4, 5, 6, 7, 8],
		series: [
			[5, 9, 7, 8, 5, 3, 5, 4],
			[10, 15, 10, 20, 18, 11, 16, 18]
		]
	}, {
		plugins: [
			Chartist.plugins.tooltip()
		]
	}, {
		high: 30,
		low: 0,
		axisY: {
			onlyInteger: true
		},
		showArea: true,
		fullWidth: true,
		chartPadding: {
			bottom: 0,
			left: 0
		}
	});
	
	/********************* BAR CHART ****************/
	var bar1 = new Chartist.Bar('#chartBar1', {
		labels: [0, 1, 2, 3, 4, 5, 6, 7],
		series: [
			[10, 5, 9, 16, 4, 12, 4, 3]
		]
	}, {
		plugins: [
			Chartist.plugins.tooltip()
		]
	}, {
		high: 40,
		low: 0,
		axisY: {
			onlyInteger: true
		},
		showArea: true,
		fullWidth: true,
		chartPadding: {
			bottom: 0,
			left: 0
		}
	});
	var bar2 = new Chartist.Bar('#chartBar2', {
		labels: [1, 2, 3, 4, 5, 6, 7, 8],
		series: [
			[5, 9, 7, 8, 5, 3, 5, 4],
			[10, 15, 10, 20, 18, 11, 16, 18]
		]
	}, {
		plugins: [
			Chartist.plugins.tooltip()
		]
	}, {
		high: 30,
		low: 0,
		axisY: {
			onlyInteger: true
		},
		showArea: true,
		fullWidth: true,
		chartPadding: {
			bottom: 0,
			left: 0
		}
	});
	
	/********************* HORIZONTAL BARS CHART ****************/
	var bar3 = new Chartist.Bar('#chartBar3', {
		labels: ['Sun', 'Mon', 'Tus', 'Wed', 'Thu', 'Fri', 'Sat'],
		series: [
			[5, 9, 7, 8, 5, 3, 5]
		]
	}, {
		plugins: [
			Chartist.plugins.tooltip()
		]
	}, {
		high: 20,
		low: 0,
		axisY: {
			onlyInteger: true
		},
		horizontalBars: true,
		showArea: true,
		fullWidth: true,
		chartPadding: {
			bottom: 0,
			left: 40
		}
	});
	var bar4 = new Chartist.Bar('#chartBar4', {
		labels: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
		series: [
			[5, 9, 7, 8, 5, 3, 5],
			[10, 15, 10, 20, 18, 11, 16]
		]
	}, {
		plugins: [
			Chartist.plugins.tooltip()
		]
	}, {
		high: 30,
		low: 0,
		axisY: {
			onlyInteger: true
		},
		horizontalBars: true,
		showArea: true,
		fullWidth: true,
		chartPadding: {
			bottom: 0,
			left: 40
		}
	});
	
	/***************** STACKED BAR CHARTS ********************/
	var bar5 = new Chartist.Bar('#chartBar5', {
		labels: ['P1', 'P2', 'P3', 'P4'],
		series: [
			[12000, 5000, 2000, 17000],
			[9000, 16000, 3000, 8000],
			[11000, 7000, 6000, 4000]
		]
	}, {
		plugins: [
			Chartist.plugins.tooltip()
		]
	}, {
		stackBars: true,
		axisY: {
			labelInterpolationFnc: function(value) {
				return (value / 2000) + 'k';
			}
		}
	}).on('draw', function(data) {
		if (data.type === 'bar') {
			data.element.attr({
				style: 'stroke-width: 30px'
			});
		}
	});
	var bar6 = new Chartist.Bar('#chartBar6', {
		labels: ['Q1', 'Q2', 'Q3', 'Q4'],
		series: [
			[800000, 1200000, 1400000, 1300000],
			[200000, 400000, 500000, 300000],
			[100000, 200000, 400000, 600000]
		]
	}, {
		plugins: [
			Chartist.plugins.tooltip()
		]
	}, {
		stackBars: true,
		horizontalBars: true,
		axisX: {
			labelInterpolationFnc: function(value) {
				return (value / 1000) + 'k';
			}
		},
		chartPadding: {
			bottom: 0,
			left: 0,
			right: 40
		}
	}).on('draw', function(data) {
		if (data.type === 'bar') {
			data.element.attr({
				style: 'stroke-width: 30px'
			});
		}
	});
	
	/********************* PIE CHART *********************/
	new Chartist.Pie('#chartPie1', {
		labels: ['2015', '2016', '2017', '2018'],
		series: [10, 30, 40]
	}, {
		plugins: [
			Chartist.plugins.tooltip()
		]
	});
	
	/**************** PIE CHART 2 *******************/
	new Chartist.Pie('#chartPie2', {
		labels: ['2015', '2016', '2017', '2018'],
		series: [20, 10, 30, 40]
	}, {
		plugins: [
			Chartist.plugins.tooltip()
		]
	});
	
	/**************** DONUT CHARTS ****************/
	var donut1 = new Chartist.Pie('#chartDonut1', {
		series: [20, 10, 30]
	}, {
		plugins: [
			Chartist.plugins.tooltip()
		]
	}, {
		donut: true,
		donutWidth: 60,
		donutSolid: true,
		startAngle: 270,
		showLabel: true
	});
	var donut2 = new Chartist.Pie('#chartDonut2', {
		series: [20, 10, 30, 40, 25]
	}, {
		plugins: [
			Chartist.plugins.tooltip()
		]
	}, {
		donut: true,
		donutWidth: 60,
		donutSolid: true,
		startAngle: 270,
		showLabel: true
	});
});