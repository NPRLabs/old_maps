
function attemptFullscreen(element) {
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

function leaveFullscreen(element) {
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
//requires jquery and a specific button id
$(function() {           
    $('#fsbtn').on('click', function() {
      console.log('asdfasdfadsf')
      if($(this).val() == "go"){   
        attemptFullscreen(document.documentElement);
        $(this).val("exit");
        $(this).text("Exit Fullscreen");
      } else  {
        leaveFullscreen(document.documentElement);
        $(this).val("go");
        $(this).text("Go Fullscreen");
      }
    });
})
