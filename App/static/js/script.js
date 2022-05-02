/* ----------------------------------------------
# All the scripts here will extends to all pages
----------------------------------------------- */

// 1) Script to validate all inputs
// the function to validate email
function validateEmail(email) {
	var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
	return regex.test(email);
}
// the function to validate every field
function validateAll() {

	var name = $('#name').val();
	var phone = $('#phone').val();
	var email = $('#email').val();
	var age = $('#age').val();
	var gender = $('#gender').val();
	var diagnosis = $('#diagnosis').val();
	
	// swal is the special tag from SweetAlert
	if (name == ''){
		swal("Opss ! ", "Name field cannot be empty.", "error");
		return false;
	}
	// Script to give the message that Last name is required. Force user to put the last name
	else if (name.split(' ').length < 2){
		swal("Opss ! ", "The Surname is required.", "info");
		return false;
	}
	// function not to allow the name field be UPPERCASE.
	else if (name == name.toUpperCase()){
		swal("Opss ! ", "Name field cannot be UPPERCASE.", "info");
		// below the string to clear the input
		$('#name').val('');
		return false;
	}
	else if (phone == ''){
		swal("Opss ! ", "Phone field cannot be empty.", "error");
		return false;
	}
	else if (email == ''){
		swal("Opss ! ", "Email field cannot be empty.", "error");
		return false;
	}
	else if (!(validateEmail(email))){
		swal("Opss ! ", "Put a valid email address.", "error");
		return false;
	}
	else if (age == ''){
		swal("Opss ! ", "Age field cannot be empty.", "error");
		return false;
	}
	/*else if (age > 130){
		swal("Denied ! ", "The maximum value is 130 years.", "error");
		$('age').val("");
		return false;
	}*/
	else if (gender == ''){
		swal("Opss ! ", "Gender field cannot be empty.", "error");
		return false;
	}
	else if (diagnosis == ''){
		swal("Opss ! ", "Diagnosis field cannot be empty.", "error");
		return false;
	}
	else{
		return true;
	}
}
$('.btn-add').bind("click", validateAll);

// 2) Script (Name field) only latter is allowed
$(document).ready(function() {
	// in order to type only letters inside the name field
	jQuery('input[name="name"]').keyup(function(){
		var letter = jQuery(this).val();
		var allow = letter.replace(/[^a-zA-Z _]/g, '');
		jQuery(this).val(allow);
	});
	// Prevent starting with space for every field
	$("input").on("keypress", function(e) {
		if (e.which === 32 && ! this.value.length)
		e.preventDefault();
	});
});

// 3) Script to make the first letter always capitalized
$("#name").keyup(function(){
	var txt = $(this).val();
	$(this).val(txt.replace(/^(.)|\s(.)/g, function($1){
		return $1.toUpperCase();
	}));
});

// 4) Script to make email lowercase only
$(document).ready(function(){
	$('#email').keyup(function (){
		this.value = this.value.toLowerCase();
	});
});

// 5) Script to accept only numbers in the age field
$('#age').keyup(function(){
	if (!/^[0-9]*$/.test(this.value)) {
		this.value = this.value.split(/[^0-9]/).join('');
	}
});

// 6) Phone mask
$(document).ready(function(){
	$('#phone').inputmask('(999)999-9999', {"onincomplete": function() {
		$("#phone").val("");
		swal("Opss !", "Incomplete phone number. Please review carefully.", "error");
		return false;
	}});
});

// 7) If input Age has number greater than 120. Create auto clear option
$(document).ready(function(){
	$("#age").keyup(function(){
		var age = $("#age").val();
		if (age > 130) {
			swal("Denied ! ", "The maximum value is 130 years.", "error");
			$("#age").val("");
			return false;
		}
	});
});

// 8) Prevent start the age with 0
$("#age").on('input', function(){
	if (/^0/.test(this.value)) {
		this.value = this.value.replace(/^0/, '');
	}
});

// 9) Allow to put only First and Surname
$(document).ready(function(){
	$("#name").keyup(function(){
		var name = $('#name').val();
		if (name.split(' ').length == 3) {
			swal("Opss ! ", "First and Surname only.", "info")
			$("#name").val("");
			return false;
		}
	});
});

// 10) Script to set Time running in realtime
setInterval(function(){
	var date = new Date();
	$('#clock').html(
		(date.getHours() < 10 ? '0' : '') + date.getHours() + ":" + (date.getMinutes() < 10 ? "0" : '') + date.getMinutes() + ":" + (date.getSeconds() < 10 ? "0" : '') + date.getSeconds()
	);
}, 500);

// 11) IF no patients, show a message
var verify = $('#check-table').length;
if (verify == 0) {
	$("#no-data").text('No patient found');
}

// 12) Close offcanvas (sidebar) when a button is clicke
$(document).ready(function() {
	jQuery('#offcanvasRight, .offcanvas-body a').click(function(){
		console.log($(this).attr('href'));
		jQuery('.offcanvas').offcanvas('hide');
	});
});
