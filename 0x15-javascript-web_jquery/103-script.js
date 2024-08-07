$(document).ready(() => {
  const fetchHello = () => {
    const lang = $('INPUT#language_code').val();
    $.get(`https://hellosalut.stefanbohacek.dev/?lang=${lang}`)
      .then(({ hello }) => {
        $('DIV#hello').html(hello);
      });
  };

  $('INPUT#btn_translate').click(() => {
    fetchHello();
  });
  $('INPUT#language_code').on('keydown', (e) => {
    if (e.key === 'Enter') {
      fetchHello();
    }
  });
});
