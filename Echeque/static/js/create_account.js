$(document).ready(function() {

    $("#createAccount").click(function() {
        $('.ui.modal').modal('show');
    });

    $("#create_account_btn").click(function() {
        $.ajax({
            cache: true,
            type: "post",
            data: {'password': $('#password').val()},
            url: "/create_account/",
            dataType: "json",
            error: function (request) {
                addAlert("Connection error");
            },
            success: function (data) {
                $('#myAlert').empty();
                if (data['message'] == "success") {
                    addInfo("Create account successfully.")
                } else {
                    addWarning(data['message']);
                }
            }
        });

    });

});

