$(function() {
	'use strict';
	
	/*----LineChart----*/
	var line = new Morris.Line({
		element: 'line-chart',
		resize: true,
		data: [{
			y: '2011 Q1',
			item1: 2666
		}, {
			y: '2011 Q2',
			item1: 2778
		}, {
			y: '2011 Q3',
			item1: 4912
		}, {
			y: '2011 Q4',
			item1: 3767
		}, {
			y: '2012 Q1',
			item1: 6810
		}, {
			y: '2012 Q2',
			item1: 5670
		}, {
			y: '2012 Q3',
			item1: 4820
		}, {
			y: '2012 Q4',
			item1: 15073
		}, {
			y: '2013 Q1',
			item1: 10687
		}, {
			y: '2013 Q2',
			item1: 8432
		}],
		xkey: 'y',
		ykeys: ['item1'],
		labels: ['Item 1'],
		lineColors: ['#5d61bf'],
		hideHover: 'auto'
	});
	
	/*----DonutChart----*/
	var donut = new Morris.Donut({
		element: 'sales-chart',
		resize: true,
		colors: ['#f47b25', '#5d61bf', '#3ebaef'],
		data: [{
			label: "Product A",
			value: 12
		}, {
			label: "Product B",
			value: 30
		}, {
			label: "Product C",
			value: 20
		}],
		hideHover: 'auto'
	});
	
	/*----BarChart----*/
	var options = {
		chart: {
			height: 350,
			type: 'bar',
		},
		plotOptions: {
			bar: {
				horizontal: false,
				endingShape: 'rounded',
				columnWidth: '55%',
			},
		},
		dataLabels: {
			enabled: false
		},
		stroke: {
			show: true,
			width: 2,
			colors: ['transparent']
		},
		colors: ['#f47b25', '#5d61bf', '#3ebaef'],
		series: [{
			name: 'Net Profit',
			data: [44, 55, 57, 56, 61, 58, 63, 60, 66]
		}, {
			name: 'Revenue',
			data: [76, 85, 101, 98, 87, 105, 91, 114, 94]
		}, {
			name: 'Free Cash Flow',
			data: [35, 41, 36, 26, 45, 48, 52, 53, 41]
		}],
		xaxis: {
			categories: ['Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
		},
		yaxis: {
			title: {
				text: '$ (thousands)'
			}
		},
		fill: {
			opacity: 1
		},
		tooltip: {
			y: {
				formatter: function(val) {
					return "$ " + val + " thousands"
				}
			}
		}
	}
	var chart = new ApexCharts(document.querySelector("#barchart"), options);
	chart.render();
});