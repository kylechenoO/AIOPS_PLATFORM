$(function() {
	
	//Initialize Select2 Elements
	$('.select2').select2()
	
	//Datemask dd/mm/yyyy
	$('#datemask').inputmask('dd/mm/yyyy', {
		'placeholder': 'dd/mm/yyyy'
	})
	
	//Datemask2 mm/dd/yyyy
	$('#datemask2').inputmask('mm/dd/yyyy', {
		'placeholder': 'mm/dd/yyyy'
	})
	
	//Money Euro
	$('[data-mask]').inputmask()
	
	//Date range picker
	$('#reservation').daterangepicker()
	
	//Date range picker with time picker
	$('#reservationtime').daterangepicker({
		timePicker: true,
		timePickerIncrement: 30,
		format: 'MM/DD/YYYY h:mm A'
	})
	
	//Date range as a button
	$('#daterange-btn').daterangepicker({
		ranges: {
			'Today': [moment(), moment()],
			'Yesterday': [moment().subtract(1, 'days'), moment().subtract(1, 'days')],
			'Last 7 Days': [moment().subtract(6, 'days'), moment()],
			'Last 30 Days': [moment().subtract(29, 'days'), moment()],
			'This Month': [moment().startOf('month'), moment().endOf('month')],
			'Last Month': [moment().subtract(1, 'month').startOf('month'), moment().subtract(1, 'month').endOf('month')]
		},
		startDate: moment().subtract(29, 'days'),
		endDate: moment()
	}, function(start, end) {
		$('#daterange-btn span').html(start.format('MMMM D, YYYY') + ' - ' + end.format('MMMM D, YYYY'))
	})
	
	//Date picker
	$('#datepicker').datepicker({
		autoclose: true
	})
	
	//iCheck for checkbox and radio inputs
	$('input[type="checkbox"].minimal, input[type="radio"].minimal').iCheck({
		checkboxClass: 'icheckbox_minimal-purple',
		radioClass: 'iradio_minimal-purple'
	})
	
	//purple color scheme for iCheck
	$('input[type="checkbox"].minimal-purple, input[type="radio"].minimal-purple').iCheck({
		checkboxClass: 'icheckbox_minimal-purple',
		radioClass: 'iradio_minimal-purple'
	})
	
	//Flat purple color scheme for iCheck
	$('input[type="checkbox"].flat-purple, input[type="radio"].flat-purple').iCheck({
		checkboxClass: 'icheckbox_flat-purple',
		radioClass: 'iradio_flat-purple'
	})
	
	//Colorpicker
	$('.my-colorpicker1').colorpicker()
	
	//color picker with addon
	$('.my-colorpicker2').colorpicker()
	
	//Timepicker
	$('.timepicker').timepicker({
		showInputs: false
	})
})