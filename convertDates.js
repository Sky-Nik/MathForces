function convertDates() {
  var elements = document.getElementsByClassName('human-readable-date');
  for (var i = 0; i < elements.length; ++i) {
    var elDate = new Date(elements[i].getAttribute('date'));
    var one_day = 1000 * 60 * 60 * 24;
    var date1_ms = elDate.getTime();
    var date2_ms = Date.now();
    var difference_ms = date2_ms - date1_ms;
    var daysPassed = Math.round(difference_ms/one_day);
    // alert(daysPassed);
    if (daysPassed === 0) {
      elements[i].textContent = "сьогодні";
    } else if (daysPassed === 1) {
      elements[i].textContent = "вчора";
    } else if (daysPassed === 2 || daysPassed == 3 || daysPassed === 4) {
      elements[i].textContent = daysPassed + "дні тому";
    } else if (daysPassed === 5 || daysPassed == 6) {
      elements[i].textContent = daysPassed + "днів тому";
    } else if (daysPassed < 13) {
      elements[i].textContent = "тиждень тому";
    } else if (daysPassed < 30) {
      elements[i].textContent = Math.round(daysPassed / 7) + "тижні тому";
    } else {
      elements[i].textContent = "місяць тому чи давніше";
    }
  }
}