// on page load...
moveProgressBar();
// on browser resize...
$(window).resize(function() {
  moveProgressBar();
});

// SIGNATURE PROGRESS
function moveProgressBar() {
  console.log("moveProgressBar");
  var getPercent = ($('.progress-wrap').data('progress-percent') / 100);
  var getProgressWrapWidth = $('.progress-wrap').width();
  var progressTotal = getPercent * getProgressWrapWidth;
  var animationLength = 2500;

  // on page load, animate percentage bar to data percentage length
  // .stop() used to prevent animation queueing
  $('.progress-bar').stop().animate({
    left: progressTotal
  }, animationLength);
}

// run when the body get loaded
function handleLoadEvent(){
    document.getElementById('snap').addEventListener('click',hahameixie);
}

//the function is called when user asked the robot if he is happy
function sendAnnotationRequest()
{
  /*This is the URL of the image to be annotated*/
  var annImgURL = getUserFaceUrl(); // url of the image to be annotated
  
  /*This is the URL for the web service request, including the key of your app as a parameter*/
  var url ="127.0.0.1";
  
  /*The is the request that will be sent as JSON*/
  var request = {
  };
  ajaxRequest("POST", url, handleResponse, JSON.stringify(request));
}

//when google api response we parse the text and process
function handleResponse() {
  if (successfulRequest(this)) {
    var response = JSON.parse(this.responseText);
    console.log(response)
  }
}