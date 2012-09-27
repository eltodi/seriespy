jQuery(document).ready(function(e) {
    var notificar_descarga_episodios = function(e) {
        $.post(url_notificar_descarga_episodios, function(data, status) {
            if ( data.length <= 0 ) {
                setTimeout(notificar_descarga_episodios, 5000);
                return;
            }

            for ( var idx in data ) {
                // notifica
                var serieinfo = data[idx];
                $.bootstrapGrowl(serieinfo[0] + "<br>" + serieinfo[1] + ": " + serieinfo[2] + "<br> descargado", {
                    type: 'info',
                    align: 'right',
                    stackup_spacing: 30
                });
            }

            setTimeout(notificar_descarga_episodios, 5000);
        })
        .error(function(e) {
            setTimeout(notificar_descarga_episodios, 10000);
        });
    }
    setTimeout(notificar_descarga_episodios, 1);
});
