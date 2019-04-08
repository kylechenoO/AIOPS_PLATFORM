// Dismiss function
	$("[data-dismiss]").each(function(e) {
		var me = $(this),
				target = me.data('dismiss');

		me.on("click", function(e) {
			$(target).fadeOut(function(e) {
				$(target).remove();
			});
			return false;
		});
	});