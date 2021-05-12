$(document).ready(function () {
  $.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', function (json) {
    $('DIV#hello').text(json.hello);
  });
});
