$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (json) {
  for (object of json.results) {
    let tag = '<li>' + object.title + '</li>'
    $('UL#list_movies').append(tag);
  };
});
