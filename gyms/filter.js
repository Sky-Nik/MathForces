var CURRENT_CATEGORY   = "all";
var CURRENT_GRADE      = "all";
var CURRENT_DIFFICULTY = "all";

var LOCAL_CATEGORY_NAMES_LOWERCASE = {
  "a": "алгебра",
  "c": "комбинаторика",
  "g": "геометрия",
  "n": "теория чисел",
  "o": "олимпиады",
  "m": "разнобой", // mash-up, mixture
};

var LOCAL_DIFFICULTY_NAMES_LOWERCASE = {
  "ve":  "оч. легко",
  "e":   "легко",
  "m":   "средне",
  "h":   "сложно",
  "vh":  "оч. сложно",
  "imo": "IMO™", // this ™ is a trademark symbol
};

function update_params(param_type, param_value) {
  // update CURRENT_x and FILTER_x
  if (param_type === "CATEGORY") {
    CURRENT_CATEGORY = param_value;
    if (CURRENT_CATEGORY === "all") {
      document.getElementById("FILTER_BY_CATEGORY_BUTTON").textContent = "Выбор по тематике";
    } else {
      document.getElementById("FILTER_BY_CATEGORY_BUTTON").textContent = "Тематика: " + LOCAL_CATEGORY_NAMES_LOWERCASE[CURRENT_CATEGORY];
    }
  } else if (param_type === "GRADE") {
    CURRENT_GRADE = param_value;
    if (CURRENT_GRADE === "all") {
      document.getElementById("FILTER_BY_GRADE_BUTTON").textContent = "Выбор по классу";
    } else {
      document.getElementById("FILTER_BY_GRADE_BUTTON").textContent = "Класс: " + CURRENT_GRADE;
    }
  } else if (param_type === "DIFFICULTY") {
    CURRENT_DIFFICULTY = param_value;
    if (CURRENT_DIFFICULTY === "all") {
      document.getElementById("FILTER_BY_DIFFICULTY_BUTTON").textContent = "Выбор по сложности";
    } else {
      document.getElementById("FILTER_BY_DIFFICULTY_BUTTON").textContent = "Сложность: " + LOCAL_DIFFICULTY_NAMES_LOWERCASE[CURRENT_DIFFICULTY];
    }
  }

  // update finder_items
  var elements = document.getElementsByClassName("finder_item");
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
  document.getElementById("classes_found").textContent = "Занятий: " + k;
  if (k === 0) {
    document.getElementById("finder_table").style.display = "none";
  } else {
    document.getElementById("finder_table").style.display = "table";
  }

};