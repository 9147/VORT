function submitData(){
    var hash = document.getElementById("hash").value;
    var data = {
        hash: hash,
    };
    console.log(data);

    setRequestHeader();

    $.ajax({
        dataType: 'json',
        type: 'POST',
        url: "/gethash/",
        data: data,
        success: function (data) {
            console.log("Success:", data);
            alert("Success");
            window.location.href = "../addhash";
        },
        error: function (jqXHR, textStatus, errorThrown) {
//            console.log(container_login);
            alert("Error"+errorThrown);

        }
    });
}