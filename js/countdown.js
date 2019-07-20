var countDownDate = new Date("Sept 1, 2019 10:00:00").getTime();

var x = setInterval(function() {
  var now = new Date().getTime();
    
  var distance = countDownDate - now;
    
  var days = Math.floor(distance / (1000 * 60 * 60 * 24));
  if (days > 2) {
    document.getElementById("before-contest-countdown").innerHTML = days + " дні";
  } else {
    var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)).toString();
    if (hours.length == 1) {
      hours = "0" + hours;
    }
    var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60)).toString();
    if (minutes.length == 1) {
      minutes = "0" + minutes;
    }
    var seconds = Math.floor((distance % (1000 * 60)) / 1000).toString();
    if (seconds.length == 1) {
      seconds = "0" + seconds;
    }
      
    document.getElementById("before-contest-countdown").innerHTML = days + " дні " + hours + ":"
    + minutes + ":" + seconds;
      
    if (distance < 0) {
      clearInterval(x);
      document.getElementById("before-contest-countdown").innerHTML = "Змагання іде";
    }
  }
}, 1000);
