$(function() {
	'use strict';
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
	/*----Chart1----*/
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
	/*----Chart2----*/
	var options2 = {
		chart: {
			type: 'line',
			width:'100%',
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
	/*----Chart3----*/
	var options3 = {
		chart: {
			type: 'line',
			width: '100%',
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
	/*----Chart4----*/
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
});