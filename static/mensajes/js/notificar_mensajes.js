jQuery(document).ready(function(e) {
    var notificar_mensajes = function(e) {
        $.post(url_notificar_mensajes, function(data, status) {
            if ( data.length <= 0 ) {
                setTimeout(notificar_mensajes, 5000);
                return;
            }

            for ( var idx in data ) {
                // notifica
                var serieinfo = data[idx];
                $.bootstrapGrowl(serieinfo[0] + "<br>" + serieinfo[1] + "<br>" + serieinfo[2], {
                    type: 'info',
                    align: 'right',
                    stackup_spacing: 30
                });
            }

            setTimeout(notificar_mensajes, 5000);
        })
        .error(function(e) {
            setTimeout(notificar_mensajes, 10000);
        });
    }
    setTimeout(notificar_mensajes, 1);
});
