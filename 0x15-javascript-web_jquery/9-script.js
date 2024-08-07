$(document).ready(() => {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(({ hello }) => {
      $('DIV#hello').text(hello);
    });
});
