$(document).ready(function() {
    $('#echeque_no').change(function() {
	//	Get_Columns_Data($(this).val());
		echeque_no = $(this).val();
		$.ajax({
            cache: true,
            type: "get",
            data: {'echeque_no': echeque_no},
            url: "/transaction/get_echeque_amount/",
            dataType: "json",
            error: function (request) {
                addAlert("Connection error");
            },
            success: function (data) {
                $('#myAlert').empty();
                if (data['message'] == "success") {
                    $('#amount').val(data['amount']);
                } else {
                    addWarning(data['message']);
                }
            }
        });

	});

    $("#transfer_btn").click(function() {
        $.ajax({
            cache: true,
            type: "post",
            data: {'echeque_no': $('#echeque_no').val(), 'to_addr': $('#to_addr').val()},
            url: "/transaction/transfer_echeque/",
            dataType: "json",
            error: function (request) {
                addAlert("Connection error");
            },
            success: function (data) {
                $('#myAlert').empty();
                if (data['message'] == 'success') {
                    console.log(data);
                    addInfo('Transfer is successful!');

                } else {
                    addWarning(data['message']);
                    console.log(data);
                }
            }
        });

    });

});

