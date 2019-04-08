$(function() {
    $("#range_01").ionRangeSlider();

    $("#range_02").ionRangeSlider({
        min: 1000,
        max: 10000,
        from: 1500
    });

    $("#range_03").ionRangeSlider({
        type: "double",
        grid: true,
        min: 1,
        max: 1500,
        from: 500,
        to: 1000,
        prefix: "$"
    });
	
	$("#range_04").ionRangeSlider({
		 type: "double",
        grid: true,
        min: -500,
        max: 2000,
        from: -800,
        to: 900
	});

    $("#range_05").ionRangeSlider({
        type: "double",
        grid: true,
        min: -2000,
        max: 2000,
        from: -600,
        to: 800,
        step: 300
    });

    $("#range_06").ionRangeSlider({
        grid: true,
        from: 2,
        values: ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    });

    $("#range_07").ionRangeSlider({
        grid: true,
        min: 10000,
        max: 10000000,
        from: 200000,
        step: 10000,
        prettify_enabled: true
    });

    $("#range_08").ionRangeSlider({
        min: 1000,
        max: 2000,
        from: 1200,
        disable: true
    });
});