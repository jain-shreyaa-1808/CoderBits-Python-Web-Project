$(document).ready(function(){
    console.log("loaded");

    $(document).on("submit", "#register-form", function (e) {
        e.preventDefault();


        var form = $('#register-form').serialize(); //get the form data

        //send an ajax request over to the route /postregisteration
        $.ajax({
            url: '/postregistration',
            type: 'POST',
            data: form,
            success: function (response) {
                console.log(response);
                window.location.href="/";

            }
        });
    });
    $(document).on("submit","#login-form",function(e){
        e.preventDefault();

        var form =$(this).serialize();
        $.ajax({
            url: '/check-login',
            type: 'POST',
            data: form,
            success: function(res){
                if (res == "error"){
                    alert("Incorrect Password");
                }else{
                    console.log("Logged in as",res);
                    window.location.href ="/";
                }
            }

        });
    });
});