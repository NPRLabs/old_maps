
function fullscreenit(element) {
  if(element.requestFullscreen) {
  console.log('1')
    element.requestFullscreen();
  } else if(element.mozRequestFullScreen) {
  console.log('2')
    element.mozRequestFullScreen();
  } else if(element.webkitRequestFullscreen) {
  console.log('3')
    element.webkitRequestFullscreen();
  }
}

function unfullscreenit(element) {
  if(document.exitFullscreen) {
  console.log('1')
    document.exitFullscreen();
  } else if(document.mozCancelFullScreen) {
  console.log('2')
    document.mozCancelFullScreen();
  } else if(document.webkitExitFullscreen) {
  console.log('32')
    document.webkitExitFullscreen();
  }
}

//deal with am and fm switch 
$(function() {           

    $('#fsbtn').on('click', function() {
      console.log('asdfasdfadsf')
      if($(this).val() == "go"){   
        fullscreenit(document.documentElement);
        $(this).val("exit");
        $(this).text("Exit Fullscreen");
      } else  {
        unfullscreenit(document.documentElement);
        $(this).val("go");
        $(this).text("Go Fullscreen");
      }
    });
})
