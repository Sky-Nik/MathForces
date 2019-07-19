var CURRENT_CATEGORY   = "all";
var CURRENT_GRADE      = "all";
var CURRENT_DIFFICULTY = "all";

var LOCAL_CATEGORY_NAMES_LOWERCASE = {
  "a": "алгебра",
  "c": "комбінаторика",
  "g": "геометрія",
  "n": "теорія чисел",
  "o": "олімпіади",
  "m": "різнобій", // mash-up, mixture
};

var LOCAL_DIFFICULTY_NAMES_LOWERCASE = {
  "ve":  "дуже легко",
  "e":   "легко",
  "m":   "середнє",
  "h":   "складно",
  "vh":  "дуже складно",
  "imo": "IMO™", // this ™ is a trademark symbol
};

function update_params(param_type, param_value) {
  // update CURRENT_x and FILTER_x
  if (param_type === "CATEGORY") {
    CURRENT_CATEGORY = param_value;
    if (CURRENT_CATEGORY === "all") {
      document.getElementById("FILTER_BY_CATEGORY_BUTTON").textContent = "Вибір за тематикою";
    } else {
      document.getElementById("FILTER_BY_CATEGORY_BUTTON").textContent = "Тематика: " + LOCAL_CATEGORY_NAMES_LOWERCASE[CURRENT_CATEGORY];
    }
  } else if (param_type === "GRADE") {
    CURRENT_GRADE = param_value;
    if (CURRENT_GRADE === "all") {
      document.getElementById("FILTER_BY_GRADE_BUTTON").textContent = "Вибір за класом";
    } else {
      document.getElementById("FILTER_BY_GRADE_BUTTON").textContent = "Клас: " + CURRENT_GRADE;
    }
  } else if (param_type === "DIFFICULTY") {
    CURRENT_DIFFICULTY = param_value;
    if (CURRENT_DIFFICULTY === "all") {
      document.getElementById("FILTER_BY_DIFFICULTY_BUTTON").textContent = "Вибір за складністю";
    } else {
      document.getElementById("FILTER_BY_DIFFICULTY_BUTTON").textContent = "Складність: " + LOCAL_DIFFICULTY_NAMES_LOWERCASE[CURRENT_DIFFICULTY];
    }
  }

  // update gym_items
  var elements = document.getElementsByClassName("gym_item");
  alert('DEBUG: ' + elements.length);
  var k = 0; // matches counter
  for (var i = 0; i < elements.length; ++i) {
    if ((CURRENT_CATEGORY   === "all" || elements[i].getAttribute('_cat')   === CURRENT_CATEGORY) &&
        (CURRENT_GRADE      === "all" || elements[i].getAttribute('_grade') === CURRENT_GRADE) &&
        (CURRENT_DIFFICULTY === "all" || elements[i].getAttribute('_diff')  === CURRENT_DIFFICULTY)) {
      elements[i].style.display = "table-row";
      
      if (k++ & 1) { // zebra table
        elements[i].style.background = "#f2f2f2";
      } else {
        elements[i].style.background = "white";
      }

    } else {
      elements[i].style.display = "none";
    }
  }

  // hide table if no problemsets found
  document.getElementById("classes_found").textContent = "Занять: " + k;
  if (k === 0) {
    document.getElementById("gyms_table").style.display = "none";
  } else {
    document.getElementById("gyms_table").style.display = "table";
  }
};

var LOCAL_CATEGORY_NAMES_UPPERCASE = {
  "a":   "Алгебра",
  "c":   "Комбінаторика",
  "g":   "Геометрія",
  "n":   "Теорія чисел",
  "o":   "Олімпіади",
  "m":   "Різнобій",
  "all": "Всі",
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
  "ve":  "Дуже легко",
  "e":   "Легко",
  "m":   "Середнє",
  "h":   "Складно",
  "vh":  "Дуже складно",
  "imo": "IMO™", // this ™ is a trademark symbol
  "all": "Всі",
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

  document.getElementById("classes_found").textContent = "Занятий: " + document.getElementsByClassName("gym_item").length;
};