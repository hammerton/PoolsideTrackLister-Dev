$(document).ready(function() {
// On document ready, display first page
function firstPage() {
    Dajaxice.ListTracks.pagination(
        Dajax.process,
        {
            'text': $('#searchForTrack').val(),
            'p':{{ 1 }}
        }
    )
}

firstPage();

$('#searchForTrack').keyup(function () {
    Dajaxice.ListTracks.pagination(
        Dajax.process,
        {
            'text': $('#searchForTrack').val(),
            'p':{{ 1 }}
        }
    )
});

// $(document).ready(function () {
//     $('button.btn.clearbutton').click(function () {
//         $('#searchForTrack').val('');
//         firstPage();
//     });
// });
});