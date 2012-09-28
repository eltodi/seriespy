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