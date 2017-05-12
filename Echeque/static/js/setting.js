$(document).ready(function() {
    //console.log(message);
    $('.ui.form').form({
        fields: {
            old_pwd: {
                identifier: 'old_pwd',
                rules: [{
                    type: 'empty',
                    prompt: 'Please enter your old password'
                },
                {
                    type: 'length[6]',
                    prompt: 'Your old password must be at least 6 characters'
                }]
            },
            new_pwd: {
                identifier: 'new_pwd',
                rules: [{
                    type: 'empty',
                    prompt: 'Please enter your new password'
                },
                {
                    type: 'length[6]',
                    prompt: 'Your new password must be at least 6 characters'
                }]
            },
            repeat_pwd: {
                identifier: 'repeat_pwd',
                rules: [{
                    type: 'empty',
                    prompt: 'Please repeat your password'
                },
                {
                    type: 'length[6]',
                    prompt: 'Your repeat password must be at least 6 characters'
                }]
            }
        },
        onSuccess: function(e) {
            console.log('111');
            e.preventDefault();
        }

    }).api({
        url: '/setting/',
        method: 'POST',
        // arbitrary POST/GET same across all requests
        data: {},
        // modify data PER element in callback
        beforeSend: function(settings) {
            // cancel request if no id
            settings["data"]["old_pwd"] = SHA256($("#old_pwd").val());
            settings["data"]["new_pwd"] = SHA256($("#new_pwd").val());
            settings["data"]["repeat_pwd"] = SHA256($("#repeat_pwd").val());

            return settings;
        },
        onSuccess: function(data) {
            $('#myAlert').empty();
            console.log('------------');
            if (data['message'] == 'success') {
                console.log(data);
                addInfo('New password applied!');


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