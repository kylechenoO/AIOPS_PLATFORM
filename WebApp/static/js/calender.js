 $(function() {
	"use strict";
 	$('#calendar1').fullCalendar({
 		header: {
 			left: 'prev,next today',
 			center: 'title',
 			right: 'month,agendaWeek,agendaDay'
 		},
 		defaultDate: '2018-09-12',
 		navLinks: true, // can click day/week names to navigate views
 		selectable: true,
 		selectHelper: true,
 		select: function(start, end) {
 			var title = prompt('Event Title:');
 			var eventData;
 			if (title) {
 				eventData = {
 					title: title,
 					start: start,
 					end: end
 				};
 				$('#calendar1').fullCalendar('renderEvent', eventData, true); // stick? = true
 			}
 			$('#calendar1').fullCalendar('unselect');
 		},
 		editable: true,
 		eventLimit: true, // allow "more" link when too many events
 		events: [{
 			title: 'All Day Event',
 			start: '2018-08-01'
 		}, {
 			title: 'Long Event',
 			start: '2018-09-07',
 			end: '2018-08-10'
 		}, {
 			id: 999,
 			title: 'Repeating Event',
 			start: '2018-08-09T16:00:00'
 		}, {
 			id: 999,
 			title: 'Repeating Event',
 			start: '2018-08-16T16:00:00'
 		}, {
 			title: 'Conference',
 			start: '2018-08-11',
 			end: '2018-08-13'
 		}, {
 			title: 'Meeting',
 			start: '2018-08-12T10:30:00',
 			end: '2018-08-12T12:30:00'
 		}, {
 			title: 'Lunch',
 			start: '2018-08-12T12:00:00'
 		}, {
 			title: 'Meeting',
 			start: '2018-08-12T14:30:00'
 		}, {
 			title: 'Happy Hour',
 			start: '2018-08-12T17:30:00'
 		}, {
 			title: 'Dinner',
 			start: '2018-08-12T20:00:00'
 		}, {
 			title: 'Birthday Party',
 			start: '2018-08-13T07:00:00'
 		}, {
 			title: 'Click for Google',
 			url: 'http://google.com/',
 			start: '2018-08-28'
 		}]
 	});
	
	 // list type
	$('#calendar').fullCalendar({
 		header: {
 			left: 'prev,next today',
 			center: 'title',
 			right: 'listDay,listWeek,month'
 		},
 		// customize the button names,
 		// otherwise they'd all just say "list"
 		views: {
 			listDay: {
 				buttonText: 'list day'
 			},
 			listWeek: {
 				buttonText: 'list week'
 			}
 		},
 		defaultView: 'listWeek',
 		defaultDate: '2018-10-20',
 		navLinks: true, // can click day/week names to navigate views
 		editable: true,
 		eventLimit: true, // allow "more" link when too many events
 		events: [{
 			title: 'All Day Event',
 			start: '2018-10-19'
 		}, {
 			title: 'Long Event',
 			start: '2018-10-14',
 			end: '2018-10-10'
 		}, {
 			id: 999,
 			title: 'Repeating Event',
 			start: '2018-10-09T16:00:00'
 		}, {
 			id: 999,
 			title: 'Repeating Event',
 			start: '2018-10-16T16:00:00'
 		}, {
 			title: 'Conference',
 			start: '2018-10-11',
 			end: '2018-10-13'
 		}, {
 			title: 'All Day Event',
 			start: '2018-10-19'
 		}, {
 			title: 'All Day Event',
 			start: '2018-10-19'
 		}, {
 			title: 'All Day Event',
 			start: '2018-10-19'
 		}, {
 			title: 'Meeting',
 			start: '2018-09-12T10:30:00',
 			end: '2018-09-12T12:30:00'
 		}, {
 			title: 'Lunch',
 			start: '2018-09-12T12:00:00'
 		}, {
 			title: 'Meeting',
 			start: '2018-09-12T14:30:00'
 		}, ]
 	});
});
