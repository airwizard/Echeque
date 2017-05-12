$(document).ready(function() {

    $("#unlock_btn").click(function() {
        $.ajax({
            cache: true,
            type: "post",
            data: {'password': $('#password').val()},
            url: "/transaction/unlock_account/",
            dataType: "json",
            error: function (request) {
                addAlert("Connection error");
            },
            success: function (data) {
                $('#myAlert').empty();
                if (data['message'] == "success") {
                    addInfo("Unlock account successfully.")
                } else {
                    addWarning(data['message']);
                }
            }
        });
    });

    $("#unlockAccount").click(function() {
        $('.ui.modal').modal('show');
    });





});

function getAccountBalance() {
    $.ajax({  
        cache: true,
        type:  "POST",
        url:  "/transaction/balance/",
        data: {},
        dataType:  "json",
        success: function(data) { 
            $('#myAlert').empty();
            $('#coinbase').empty();
            $('#deposit').empty();
            if (data['message'] == 'success') {
                //$('#watchBalance').hide();

                $('#init_region').hide();
                $('#addr_region').hide();
                $('#sign_echeque').show();

                var row = '<table class="ui celled table" style="width: 50%;"><tbody><tr><td><div class="ui ribbon label">Address</div></td><td>';
                row = row + data['address'];
                row = row + '</td></tr><tr><td><div class="ui ribbon label">Balance</div></td><td>';
                row = row + Number(data['balance']).toFixed(2);
                console.log(Number(data['balance']).toFixed(2));

                row = row + '</td></tr></tbody></table>';

                $('#coinbase').append(row);
            }
            else {
                addWarning(data['message']);
            }
        },
        error: function(request) {
            console.log(request);
        },
    }); 


}


//function watchBalance() {
//    var Web3 = require('web3');
//var web3 = new Web3();
//
//rpcport = localStorage.getItem('rpcport');
////web3.setProvider(new web3.providers.HttpProvider());
////default port is 8545
//
//
//console.log(JSON.stringify("http://localhost:"+rpcport));
//web3.setProvider(new web3.providers.HttpProvider(JSON.stringify("http://localhost:"+rpcport)));
//
//    console.log('11111');
//
//    var x = new web3.providers.HttpProvider(JSON.stringify("http://localhost:"+rpcport));
//    console.log(x);
//    console.log(web3.setProvider(x));
//
//    var coinbase = web3.eth.coinbase;
//    console.log(coinbase);
//    var originalBalance = web3.eth.getBalance(coinbase).toNumber();
//
//    console.log(originalBalance);
//    document.getElementById('coinbase').innerText = 'coinbase: ' + coinbase;
//    document.getElementById('original').innerText = ' original balance: ' + originalBalance + '    watching...';
//
//    web3.eth.filter('latest').watch(function() {
//        var currentBalance = web3.eth.getBalance(coinbase).toNumber();
//        document.getElementById("current").innerText = 'current: ' + currentBalance;
//        document.getElementById("diff").innerText = 'diff:    ' + (currentBalance - originalBalance);
//    });
//}