$(document).ready(() => {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json')
    .then(({ results: movies }) => {
      movies.forEach((movie) => {
        $('UL#list_movies').append(`<li>${movie.title}</li>`);
      });
    });
});
