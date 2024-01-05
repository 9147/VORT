
// Function to GET csrftoken from Cookie
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');




function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

// Function to set Request Header with `CSRFTOKEN`
function setRequestHeader(){
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
}


function login(){
    console.log("login");
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    var data = {
        username: username,
        password: password,
    };
    console.log(data);

    setRequestHeader();

    $.ajax({
        dataType: 'json',
        type: 'POST',
        url: "/signin/",
        data: data,
        success: function (data) {
            console.log("Success:", data);
            window.location.href = "../";
        },
        error: function (jqXHR, textStatus, errorThrown) {
            var container_login=document.getElementById("container_login");
//            console.log(container_login);
            container_login.classList.add("shake");
            setTimeout(function(){
                container_login.classList.remove("shake");
            }, 500);

        }
    });

}