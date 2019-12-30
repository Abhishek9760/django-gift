$(document).ready(function() {
  var arrNumbers = [[29,30,31,43,53,54,55,67,77,78,79],
                [29,30,31,43,53,54,55,65,77,78,79],
                [29,30,42,54,66,78]]
  var columns = 12;
  var rows = 10;
  var $square = '<div class="square"><div class="sqrInside"></div></div>';
  var counter = 0;
  for (var r = 1; r < rows + 1; r++) {
    for (var c = 1; c < columns + 1; c++) {
      counter++
      // var $square = '<div class="square" id=sqr"' + (counter) + '"><div class="sqrInside"></div></div>';
      var $square = '<div class="square" id=sqrCont"' + (counter) + '"><div class="sqrInside"  id="sqr' + counter + '"></div></div>'; //' + counter + '
      $($square).appendTo('div#allSquares');

    }
  }

  var numero = 0;

  function rotateSqr() {
    if (numero >= arrNumbers.length) {
      numero = 0;
    }

    console.log(arrNumbers[numero]);
    var arrDrawNumber = arrNumbers[numero];

    for(var block = 26; block < 94; block++){
      $('#sqr' + block).removeClass('sqrRotate');
    }


    for(var num = 0; num < arrDrawNumber.length; num++){
      console.log("numero: " + arrDrawNumber[num]);
      $('#sqr' + arrDrawNumber[num]).addClass('sqrRotate');
    }

    // $('#sqr30').toggleClass('sqrRotate');
    // $('#sqr31').toggleClass('sqrRotate');
    // $('#sqr43').toggleClass('sqrRotate');
    // $('#sqr53').toggleClass('sqrRotate sqrYellowToOrange');
    // $('#sqr54').toggleClass('sqrRotate sqrYellowToOrange');
    // $('#sqr55').toggleClass('sqrRotate sqrYellowToOrange');
    // $('#sqr67').toggleClass('sqrRotate');
    // $('#sqr77').toggleClass('sqrRotate sqrOrangeToPurple');
    // $('#sqr78').toggleClass('sqrRotate sqrOrangeToPurple');
    // $('#sqr79').toggleClass('sqrRotate sqrOrangeToPurple');

    numero++;

    setTimeout(function() {
      rotateSqr();
    }, 2500)
  }

  rotateSqr();

});