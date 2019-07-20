function compile_filters() {
  document.getElementById("problems_found").textContent = "Задач: " + (document.getElementsByTagName('tr').length - 1);
};