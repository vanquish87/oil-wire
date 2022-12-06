
$("#id_saswellname").change(function () {
    var url = $("#userAccountSetupForm").attr("data-rigs-url");  // get the url of the `load_cities` view
    var wellId = $(this).val();  // get the selected country ID from the HTML input

    $.ajax({                       // initialize an AJAX request
        url: url,                    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
        data: {
        'saswellname': wellId       // add the country id to the GET parameters
        },
        success: function (data) {   // `data` is the return of the `load_cities` view function
        $("#id_sasrigname").html(data);  // replace the contents of the city input with the data that came from the server
        }
    });

});