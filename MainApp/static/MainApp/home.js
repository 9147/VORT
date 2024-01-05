let myDropzone = new Dropzone("#mydrop", { 
    url: "/upload/",
    maxFilesize: 2,
    acceptedFites:'document/pdf',
    init: function () {
        this.on("complete", function (file){
         ele = document.createElement('div');
         ele.classList.add('inner-box');
            ele.innerHTML = "file Name: " +file.name+"<br/>" + JSON.parse(file.xhr.response).data;
            console.log(ele);
          document.getElementById('box').appendChild(ele);
        });
    }
});
