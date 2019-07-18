var LOCAL_CATEGORY_NAMES_UPPERCASE = {
  "a":   "Алгебра",
  "c":   "Комбинаторика",
  "g":   "Геометрия",
  "n":   "Теория чисел",
  "o":   "Олимпиады",
  "m":   "Разнобой",
  "all": "Все",
};

var LOCAL_GRADE_NAMES_UPPERCASE = {
  "6":   "6",
  "7":   "7",
  "8":   "8",
  "9":   "9",
  "10":  "10",
  "11":  "11",
  "all": "Все",
};

var LOCAL_DIFFICULTY_NAMES_UPPERCASE = {
  "ve":  "Оч. легко",
  "e":   "Легко",
  "m":   "Средне",
  "h":   "Сложно",
  "vh":  "Оч. сложно",
  "imo": "IMO™", // this ™ is a trademark symbol
  "all": "Все",
};

function compile_filters() {
  var s = "";
  for (var key in LOCAL_CATEGORY_NAMES_UPPERCASE) {
    s += '<p onclick="update_params(\'CATEGORY\', \'' + key + '\');">' + LOCAL_CATEGORY_NAMES_UPPERCASE[key] + '</p>';
  }
  document.getElementById("FILTER_BY_CATEGORY").innerHTML += '<div class="dropdown-content">' + s + '</div>';

  s = "";
  for (var key in LOCAL_GRADE_NAMES_UPPERCASE) {
    s += '<p onclick="update_params(\'GRADE\', \'' + key + '\');">' + LOCAL_GRADE_NAMES_UPPERCASE[key] + '</p>';
  }
  document.getElementById("FILTER_BY_GRADE").innerHTML += '<div class="dropdown-content">' + s + '</div>';

  s = "";
  for (var key in LOCAL_DIFFICULTY_NAMES_UPPERCASE) {
    s += '<p onclick="update_params(\'DIFFICULTY\', \'' + key + '\');">' + LOCAL_DIFFICULTY_NAMES_UPPERCASE[key] + '</p>';
  }
  document.getElementById("FILTER_BY_DIFFICULTY").innerHTML += '<div class="dropdown-content">' + s + '</div>';
};

function compile_classes_found() {
  document.getElementById("classes_found").textContent = "Занятий: " + document.getElementsByClassName("finder_item").length;
};

LOCAL_MONTH_NAMES = {
  "1":  "января",
  "2":  "февраля",
  "3":  "марта",
  "4":  "апреля",
  "5":  "мая",
  "6":  "июня",
  "7":  "июля",
  "8":  "августа",
  "9":  "сентября",
  "10": "октября",
  "11": "ноября",
  "12": "декабря",
};

SOURCE_NAMES = {
  "khamovniki": "Кружки в Хамовниках",
};

function compile_finder_items() {
  var elements = document.getElementsByClassName("finder_item");
  for (var i = 0; i < elements.length; ++i) {
    // unpacking
    var cat        = LOCAL_CATEGORY_NAMES_UPPERCASE[elements[i].getAttribute('_cat')];
    var source     = elements[i].getAttribute('_source');
    var grade      = elements[i].getAttribute('_grade');
    var link       = elements[i].getAttribute('_link');
    var topic      = elements[i].getAttribute('_topic');
    var _id        = elements[i].getAttribute('id');
    var date_parts = elements[i].getAttribute('_date').split('.', 3);
    var date       = date_parts[0] + ' ' + LOCAL_MONTH_NAMES[date_parts[1]] + ' ' + date_parts[2] + '&nbsp;г.';
    var diff       = LOCAL_DIFFICULTY_NAMES_UPPERCASE[elements[i].getAttribute('_diff')];

    var s = '<td>' + SOURCE_NAMES[source] + '</td><td>' + cat + '</td><td>' + topic + ': <a href="' + source + '/' + grade + '/' + link + '.pdf">[pdf]</a>, <a href="' + _id + '_t.html">[web]</a>';
    if (elements[i].hasAttribute('_num_probs')) {
      var num_probs = elements[i].getAttribute('_num_probs');
      s += ', <span style="color: gray; font-size: smaller;">' + num_probs + '&nbsp;задач';
      if (num_probs === "1") {
        s += 'а';
      } else if (num_probs === "2" || num_probs === "3" || num_probs === "4") {
        s += 'и';
      }
      s += '</span>';
    }
    elements[i].innerHTML = s + '</td><td>' + date + '</td><td>' + grade + '</td><td>' + diff + '</td>';
  }
};