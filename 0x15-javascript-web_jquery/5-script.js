$(document).ready(() => {
  $('DIV#add_item').click(() => {
    $('UL.my_list').append('<li>item</li>');
  });
});
