$(document).on("ready",function(){
	$("#contenido").fadeOut();
})

function pruebame(){
	$.ajax({
		url: "/mensajes/pruebame/",
		beforeSend:  function(){
			$("#contenedor").html("probado");
		},
		type: "post",
		data: "op=1",
		success: function(data){
			alert(data);
		}
	})
}

function eliminarSerie(serie){
	$("#cp_modal .modal-header").html("<h1>Eliminar "+serie+"</h1>");
	$("#cp_modal .modal-body").html("<p class='lead'>ATENCIÓN:</br>Está apunto de eliminar la serie <i>"+serie+"</i><br>Seguro que desea continuar??</p>");
	$("#cp_modal .modal-footer").html("<button onclick='$(\"#cp_modal\").modal(\"hide\")' class='btn btn-info'>Cancelar</button><button onclick='eliminar()' class='btn btn-danger'>Eliminar</button>");
	$("#cp_modal").modal("show");
}

function eliminar(){
	slug = $("#inp_slug_serie").val();
	$.ajax({
		url: 	"/series/"+slug+"/eliminar/",
		type: 	"post",
		data: 	"slug_serie="+slug,
		success: function(data){
			$("#cp_modal").modal("hide");
			window.location.href="/";
		}
	})
}
