$(document).ready(function () {
    $('form').on('submit', function (event) {
        event.preventDefault();

        var formData = new FormData($('form')[0]);

        $.ajax({
            xhr: function () {
                var xhr = new windows.XMLHttpRequest();
                xhr.upload.addEventListener('progress', function (e) {
                    if (e.lengthComputalbe) {
                        console.log('Bytes loaded:' + e.loaded);
                        console.log('Totle Size:' + e.total);
                        console.log('Percentage Uploaded:' + (e.loaded / e.total));

                        var percent = Math.round((e.loaded / e.total) * 100);
                        $('#progressBar').attr("aria-valuenow", percent).css("width", percent + '%').text(percent + '%');
                    }
                })
                return xhr;
            },
            type: 'POST',
            url: '/upload',
            data: formData,
            processData: false,
            contentType: false,
            success: function () {
                alert('File uploaded!');
            }
        });
    });
});
