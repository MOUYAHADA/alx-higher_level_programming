$(document).ready(() => {
  $('INPUT#btn_translate').click(() => {
    const lang = $('INPUT#language_code').val();
    $.get(`https://hellosalut.stefanbohacek.dev/?lang=${lang}`)
      .then(({ hello }) => {
        $('DIV#hello').html(hello);
      });
  });
});
