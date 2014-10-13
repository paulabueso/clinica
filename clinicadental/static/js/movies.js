/**
 * Created by paulabueso on 9/30/14.
 */
$(document).ready(function() {
	$('#getMovie').on('click', function () {
		var movie = $('input').val();
		var my_url = "http://api.rottentomatoes.com/api/public/v1.0/movies.json?apikey=83ypn5vn7fbdhfnh4uxa2jta&q=" + movie + "&page_limit=1";
		console.log(my_url);
		$.ajax({
		    url: my_url,
		    type: "GET",
		    dataType: "jsonp",
		    success: function(data) {
		    	var cast = data.movies[0].abridged_cast;
		    	console.log(data)
		    	$('#dispMovie').append("<p>Title: "+data.movies[0].title+"</p>")
		    	$('#dispMovie').append("<p>Synopsis: "+data.movies[0].synopsis+"</p>")
		    	for (i = 0; i < cast.length; i++){
		    		$('#dispMovie').append("<p>Actor: "+cast[i].name+" Charater: "+cast[i].characters+"</p>")
		    	}
		    	$('#dispMovie').append("<img src="+data.movies[0].posters.original+">")
	    	}
		});
	});
});