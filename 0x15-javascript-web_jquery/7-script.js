$.get('https://swapi.co/api/people/5/?format=json', function(data, textStatus)
{
    name = data.name;
    $('#character').text(name);
});
