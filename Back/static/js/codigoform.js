$(function(){
   //sacar los mensajes de error
    $("errorusername").hide();
	$("erroremail").hide();
	$("errorfecha") .hide();
	$("errortelefono").hide();
	$("errorregion").hide();
	$("errorciudad").hide();
	$("errorcasa").hide();

    
    //variables que indican valor de estado validacion
	var error_username = false;
	var rut = rut;
	var error_email = false;
	var error_telefono = false;
	var error_region = false;
	var error_casa = false;
	var error_ciudad = false;
	var error_fecha = false;

	//definir los check y asociarlos con la clase
	$("#fechanacimiento").focusout(function() {

		check_fecha();
		
	});

	$("#TipoDeCasa").focusout(function() {

		check_casa();
		
	});


	$("#Región").focusout(function() {

		check_region();
		
	});

	$("#ciudad").focusout(function() {

		check_ciudad();
		
	});

	$("#rut").focusout(function() {

		check_rut();
		
	});

    $("#nombreUsuario").focusout(function() {

		check_username();
		
	});

	$("#email").focusout(function() {

		check_email();
		
	});

	$("#telefono").focusout(function() {

		check_telefono();
		
	});


	// llamar a las funciones asociarlas con las las clases e id y crear la funcion
	function check_ciudad() {

		if($("#ciudad option:selected").val() == 0) {
    		$("#errorciudad").html("Seleccione una categoria");
			$("#errorciudad").show();
			error_ciudad = true;
		} else {
			$("#errorciudad").hide();
			error_ciudad = false;
		}
	}
	

	function check_region() {

		//funcion para obligar la eleccion de una opcion valida
		if($("#Región option:selected").val() == 0) {
    		$("#errorregion").html("Seleccione una categoria");
			$("#errorregion").show();
			error_region = true;
		} else {
			$("#errorregion").hide();
			error_region = false;
		}
	}
	

	function check_fecha() {

		var patron=new RegExp("^(19|20)+([0-9]{2})([-])([0-9]{1,2})([-])([0-9]{1,2})$");
		
		var fecha = "2001"; //valor asignado a la fecha para comparar
  
		if ((patron.test($("#fechanacimiento").val())) && ($("#fechanacimiento").val() < fecha)) {
			  $("#errorfecha").hide();
		} else {
				 $("#errorfecha").html("Debe ingresar una fecha valida");
			  $("#errorfecha").show();
			  error_fecha = true;
		}
		//si la fecha de nacimiento es menor a fecha(2001) entonces estaria bien y si no se ingresaria el error
	  }
	

	function check_casa() {

		//funcion para obligar la eleccion de una opcion valida
		if($("#TipoDeCasa option:selected").val() == 0) {
    		$("#errorcasa").html("Seleccione una categoria");
			$("#errorcasa").show();
			error_casa = true;
		} else {
			$("#errorcasa").hide();
			error_casa = false;
		}
	}
	

	function check_telefono() {

	// funcion para definir el largo de caracteres para ingresar el numero (length)
		var telefono_length = $("#telefono").val().length;
		
		if(telefono_length < 9 || telefono_length >9) {
			$("#errortelefono").html("debe ingresar un numero valido");
			$("#errortelefono").show();
			error_telefono = true;
			
		} else {
			$("#errortelefono").hide();
		}
	}

	function check_username() {
		// funcion para definir el largo del nombre 
		var username_length = $("#nombreUsuario").val().length;
		
		if(username_length < 5 || username_length > 20) {
			$("#errorusername").html("debe tener entre 5 y 20 caracteres");
			$("#errorusername").show();
			error_username = true;
		} else {
			$("#errorusername").hide();
		}
	
	}

	function check_rut() {
		// funcion para definir el largo del rut
		var rut_length = $("#rut").val().length ;
		
		if(rut_length < 9 || rut_length > 11) {
			$("#errorrut").html("debe ingresar un rut valido");
			$("#errorrut").show();
			error_rut = true;
			
		} else {
			$("#errorrut").hide();
		}
	
	}


	function check_email() {

		var pattern = new RegExp(/^[+a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/i);// define los caracteres validos para escribir el correo electronico 
	
		if(pattern.test($("#email").val())) {
			$("#erroremail").hide();
		} else {
			$("#erroremail").html("Direccion inválida");
			$("#erroremail").show();
			error_email = true;
		}
	
	}

	//funcion para retornar el error al recibir los error = true
	$("#registration_form").submit(function() {
											
		error_username = false;
		error_rut = false;
		error_email = false;
		error_telefono = false;
		error_region = false;
		error_casa = false;
		error_ciudad = false;
		error_fecha = false;



		check_username();									
		check_email();
		check_telefono();
		check_region();
		check_ciudad();
		check_casa();
		check_fecha();
		check_rut();
		
		

		//arrogar el mensaje de error si se encuentra valido
		if(error_username == false && error_email == false && error_telefono == false && error_email == false && error_region == false && error_casa == false && error_ciudad == false && error_fecha == false) {
			return true;
		} else {
			return false;	
		}

	});


});

