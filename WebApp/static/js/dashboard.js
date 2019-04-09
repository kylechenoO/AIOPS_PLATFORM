$(function() {
	'use strict';
	
	
	/*----eCharts----*/
	var echartBar = echarts.init(document.getElementById('index'), {
		color: ['#f47b25', '#5d61bf'],
		categoryAxis: {
			axisLine: {
				lineStyle: {
					color: '#ececff'
				}
			},
			splitLine: {
				lineStyle: {
					color: ['#ececff']
				}
			}
		},
		grid: {
			x: 40,
			y: 20,
			x2: 40,
			y2: 20
		},
		valueAxis: {
			axisLine: {
				lineStyle: {
					color: '#ececff'
				}
			},
			splitArea: {
				show: true,
				areaStyle: {
					color: ['rgba(255,255,255,0.1)']
				}
			},
			splitLine: {
				lineStyle: {
					color: ['#ececff']
				}
			}
		},
		
	});
	
	echartBar.setOption({
		tooltip: {
			trigger: 'axis'
		},
		legend: {
			data: ['New Account', 'Expansion Account']
		},
		toolbox: {
			show: false
		},
		calculable: false,
		xAxis: [{
			type: 'category',
			data: ['Jan', 'Feb', 'March', 'April', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
		}],
		yAxis: [{
			type: 'value'
		}],
		series: [{
			name: 'New Accounts',
			type: 'bar',
			data: [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0],
			markPoint: {
				data: [{
					type: 'max',
					name: ''
				}, {
					type: 'min',
					name: ''
				}]
			},
			markLine: {
				data: [{
					type: 'average',
					name: ''
				}]
			}
		}, {
			name: 'Expansion Accounts',
			type: 'bar',
			data: [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8,],
			markPoint: {
				data: [{
					name: 'New Accounts',
					value: 182.2,
					xAxis: 7,
					yAxis: 183,
				}, {
					name: 'Expansion Accounts',
					value: 2.3,
					xAxis: 11,
					yAxis: 3
				}]
			},
			markLine: {
				data: [{
					type: 'average',
					name: ''
				}]
			}
		}]
	});
	
	window.Apex = {
		stroke: {
			width: 3
		},
		markers: {
			size: 0
		},
		tooltip: {
			fixed: {
				enabled: true,
			}
		}
	};
	var options1 = {
		chart: {
			type: 'line',
			width: '100%',
			height: 45,
			sparkline: {
				enabled: true
			}
		},
		stroke: {
			colors: '#f47b25',
		},
		series: [{
			data: [25, 66, 41, 89, 63, 25, 44, 12, 36, 9, 54]
		}],
		tooltip: {
			fixed: {
				enabled: false
			},
			x: {
				show: false
			},
			y: {
				title: {
					formatter: function(seriesName) {
						return ''
					}
				}
			},
			marker: {
				show: false
			}
		}
	}
	var options2 = {
		chart: {
			type: 'line',
			width: '100%',
			height: 45,
			sparkline: {
				enabled: true
			}
		},
		stroke: {
			colors: '#5d61bf',
		},
		series: [{
			data: [12, 14, 2, 47, 42, 15, 47, 75, 65, 19, 14]
		}],
		tooltip: {
			fixed: {
				enabled: false
			},
			x: {
				show: false
			},
			y: {
				title: {
					formatter: function(seriesName) {
						return ''
					}
				}
			},
			marker: {
				show: false
			}
		}
	}
	var options3 = {
		chart: {
			type: 'line',
			width:'100%',
			height: 45,
			sparkline: {
				enabled: true
			}
		},
		stroke: {
			colors: '#31c92e',
		},
		series: [{
			data: [47, 45, 74, 14, 56, 74, 14, 11, 7, 39, 82]
		}],
		tooltip: {
			fixed: {
				enabled: false
			},
			x: {
				show: false
			},
			y: {
				title: {
					formatter: function(seriesName) {
						return ''
					}
				}
			},
			marker: {
				show: false
			}
		}
	}
	var options4 = {
		chart: {
			type: 'line',
			width: '100%',
			height: 45,
			sparkline: {
				enabled: true
			}
		},
		stroke: {
			colors: '#3ebaef',
		},
		series: [{
			data: [15, 75, 47, 65, 14, 2, 41, 54, 4, 27, 15]
		}],
		tooltip: {
			fixed: {
				enabled: false
			},
			x: {
				show: false
			},
			y: {
				title: {
					formatter: function(seriesName) {
						return ''
					}
				}
			},
			marker: {
				show: false
			}
		}
	}
	new ApexCharts(document.querySelector("#chart1"), options1).render();
	new ApexCharts(document.querySelector("#chart2"), options2).render();
	new ApexCharts(document.querySelector("#chart3"), options3).render();
	new ApexCharts(document.querySelector("#chart4"), options4).render();
	
	
	var bar = new Morris.Bar({
 		element: 'bar-chart',
 		resize: true,
 		data: [{
 			y: 'Jan',
 			a: 50,
 			b: 90
 		}, {
 			y: 'Feb',
 			a: 95,
 			b: 65
 		}, {
 			y: 'Mar',
 			a: 50,
 			b: 40
 		}, {
 			y: 'Apr',
 			a: 75,
 			b: 65
 		}, {
 			y: 'May',
 			a: 50,
 			b: 40
 		}, {
 			y: 'Jun',
 			a: 75,
 			b: 65
 		}, {
 			y: 'Jul',
 			a: 100,
 			b: 90
 		}],
 		barColors: ['#f47b25', '#5d61bf'],
 		xkey: 'y',
 		ykeys: ['a', 'b'],
 		labels: ['Front end projects', 'Backend projects'],
 		hideHover: 'auto'
 	});
	/*----DonutChart----*/
	var donut = new Morris.Donut({
		element: 'sales-chart',
		resize: true,
		colors: ['#f47b25', '#5d61bf', '#3ebaef'],
		data: [{
			label: "2018",
			value: 5522
		}, {
			label: "2017",
			value: 3310
		}, {
			label: "2016",
			value: 2250
		}],
		hideHover: 'auto'
	});
	
});


