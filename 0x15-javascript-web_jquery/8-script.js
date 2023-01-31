$(function () {
	$.ajax({
		type: "Get",
		url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
		success: function (info) {
			$.each(info.results, function (a, data){
				$('#list_movies').append("<li>" + data.title + "</li>")
			})
		}
	})
})
