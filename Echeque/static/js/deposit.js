$(document).ready(function() {
    $('.ui.form').form({
        on: 'blur',
        fields: {
            bankName: {
                identifier: 'bankName',
                rules: [{
                    type: 'empty',
                    prompt: 'Please select a dropdown value'
                }]
            },
            amount: {
                identifier: 'amount',
                rules: [{
                    type: 'empty',
                    prompt: 'Please enter a value'
                },
                {
                    type   : 'number',
                    prompt : 'Please enter a valid number'
                }]
            }
        },
        onSuccess: function(e) {
            e.preventDefault();
        }
    }).api({
        url: '/transaction/deposit/',
        method: 'POST',
        // arbitrary POST/GET same across all requests
        data: {},
        // modify data PER element in callback
        beforeSend: function(deposit) {
            // cancel request if no id
            deposit["data"]["bankName"] = $("#bankName").val();
            deposit["data"]["amount"] = $("#amount").val();

            return deposit;
        },
        onSuccess: function(data) {
            $('#myAlert').empty();
            console.log('------------');
            if (data['message'] == 'success') {
                console.log(data);
                addInfo('Transactions being processed.');


            } else {
                addWarning(data['message']);
                console.log(data);
            }

        },
        onError: function(request) {
            console.log(JSON.stringify(request));
        }
    });
});