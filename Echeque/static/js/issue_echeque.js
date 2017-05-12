$(document).ready(function() {

    $("#issue_btn").click(function() {
        $.ajax({
            cache: true,
            type: "post",
            data: {'from_addr': $('#from_addr').val(),'amount': $('#amount').val(),'payee_name': $('#payee_name').val()},
            url: '/transaction/issue_echeque/',
            dataType: "json",
            error: function (request) {
                addAlert("Connection error");
            },
            success: function (data) {
                $('#myAlert').empty();
                $('#myAlert').empty();
                if (data['message'] == 'success') {
                    console.log(data);
                    addInfo('The number of your Echeque is ' + JSON.stringify(data['echeque_no']) + '.');
                } else {
                    addWarning(data['message']);
                    console.log(data);
                }
            }
        });

    });

});

