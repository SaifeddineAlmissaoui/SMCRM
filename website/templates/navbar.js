// navbar.js

document.addEventListener('DOMContentLoaded', function () {
  var toggler = document.querySelector('.navbar-toggler');
  var collapse = document.querySelector('.navbar-collapse');

  toggler.addEventListener('click', function () {
    collapse.classList.toggle('show');
  });
});
