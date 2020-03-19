// Select color input
var makeGridColor;

// Select size input

var makeGridHeight;
var makeGridWidth;

// When size is submitted by the user, call makeGrid()
$('#sizePicker').submit(function (event) {
    event.preventDefault();
    makeGridHeight = $('#inputHeight').val();
    makeGridWidth = $('#inputWidth').val();
    makeGridColor = $('colorPicker').val();
    makeGrid(makeGridHeight, makeGridWidth)
})


function makeGrid(makeGridHeight, makeGridWidth) {
    $('tr').remove();
    for (var i = 1; i <= makeGridHeight; i++) {
        $('#pixelCanvas').append('<tr id=table' + i + '></tr>');  
        for (var j = 1; j <= makeGridWidth; j++) {
            $('#table' + i).append('<td></td>');
        }
        $(this).click(function(event) {$(this).attr('style', 'background-color:' + makeGridColor().val);
    }

    }
}