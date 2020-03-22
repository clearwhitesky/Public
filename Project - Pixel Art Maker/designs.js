// Select color input
// embedded in clickColor Function

// Select size input
var makeGridHeight;
var makeGridWidth;


// When size is submitted by the user, call makeGrid()
$('#sizePicker').submit(function (event) {
    event.preventDefault();
    makeGridHeight = $('#inputHeight').val();
    makeGridWidth = $('#inputWidth').val();
    makeGrid(makeGridHeight, makeGridWidth)
    clickColor();
})

function makeGrid(makeGridHeight, makeGridWidth) {
    $('tr').remove();
    for (var i = 1; i <= makeGridHeight; i++) {
        $('#pixelCanvas').append('<tr id=table' + i + '></tr>');  
        for (var j = 1; j <= makeGridWidth; j++) {
            $('#table' + i).append('<td></td>');
        }
    }
}

// Add color to cell
function clickColor() {
    $('td').click( event => {
        let makeGridColor = $('#colorPicker').val();
        $(event.currentTarget).css("background-color", makeGridColor)
    });
};