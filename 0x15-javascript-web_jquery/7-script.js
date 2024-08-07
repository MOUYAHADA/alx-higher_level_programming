$(document).ready(() => {
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json')
    .then((data) => {
      $('DIV#character').text(data.name);
    });
});
