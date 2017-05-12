$(document).ready(function() {
    $('.ui.form').form({
        fields: {
            username: {
                identifier: 'username',
                rules: [{
                    type: 'empty',
                    prompt: 'Please enter a username'
                },
                ]
            },
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
            },
            repassword: {
                identifier: 'repassword',
                rules: [{
                    type: 'empty',
                    prompt: 'Please enter your repeat password'
                },
                {
                    type: 'length[6]',
                    prompt: 'Your repeat password must be at least 6 characters'
                }]
            }
        },
        onSuccess: function(e) {
            e.preventDefault();
        }

    }).api({
        url: '/regist/',
        method: 'POST',
        // arbitrary POST/GET same across all requests
        data: {},
        // modify data PER element in callback
        beforeSend: function(settings) {
            // cancel request if no id
            settings["data"]["username"] = $("#username").val();
            settings["data"]["email"] = $("#email").val();
            settings["data"]["password"] = SHA256($("#password").val());
            settings["data"]["repassword"] = SHA256($("#repassword").val());

            // if( !$(this).data('id') ) {
            // return false;
            // }
            // settings.data.userID = $(this).data('id');
            //console.log(JSON.stringify(settings));
            return settings;
        },
        onSuccess: function(data) {
            console.log(JSON.stringify(data));
            console.log('------------');
            if (data['message'] == 'success') {
                window.location = '/login/';

            }

        }
    });

});
