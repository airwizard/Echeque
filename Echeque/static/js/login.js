$(document).ready(function() {
    //console.log(message);
    $('.ui.form').form({
        fields: {
            email: {
                identifier: 'email',
                rules: [{
                    type: 'empty',
                    prompt: 'Please enter your e-mail'
                },
                {
                    type: 'email',
                    prompt: 'Please enter a valid e-mail'
                }]
            },
            password: {
                identifier: 'password',
                rules: [{
                    type: 'empty',
                    prompt: 'Please enter your password'
                },
                {
                    type: 'length[6]',
                    prompt: 'Your password must be at least 6 characters'
                }]
            }
        },
        onSuccess: function(e) {
            e.preventDefault();
        }

    }).api({
        url: '/login/',
        method: 'POST',
        // arbitrary POST/GET same across all requests
        data: {},
        // modify data PER element in callback
        beforeSend: function(settings) {
            // cancel request if no id
            settings["data"]["email"] = $("#email").val();
            settings["data"]["password"] = SHA256($("#password").val());

            return settings;
        },
        onSuccess: function(data) {
            console.log('------------');
            if (data['message'] == 'success') {
                console.log(data);
                localStorage.setItem('user_id', data['user_id']);
                localStorage.setItem('username', data['username']);
                window.location = '/index/';

            }

        }
    });

});