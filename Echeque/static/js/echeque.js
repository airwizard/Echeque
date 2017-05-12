$(document).ready(function() {

    showTrans();




});

function showTrans() {
    $('#addr_tbody').empty();
    $.ajax({
        cache: true,
        type: "post",
        url: "/transaction/echeque_list/",
        dataType: "json",
        async: true,
        error: function (request) {
            addAlert("Connection error");
        },
        success: function (data) {
            if (data['message'] == 'success') {
                console.log(data['data']);

                addTable(data['data']);


            } else {
                addWarning(data['message']);
                console.log(data);
            }
        }
    });
}

function addTable(data) {
    $('#trans_tbody').empty();
    var row="";
    for (var i = 0; i < data.length; i++) {
        row += "<tr>";

        row += "<td>"+"<a href='/transaction/echeque?trans_hash=" + data[i][0] + "'>" + data[i][0] + "</a></td>";

        row += "<td>"+ data[i][1] + "</td>";


        if (data[i][2] > 0) {
            row += '<td class="positive">' + data[i][2] + '</td>';
        } else if(data[i][2] < 0) {
            row += '<td class="negative">' + data[i][2] + '</td>';
        } else {
            row += '<td>' +data[i][2] + '</td>';
        }

        if (data[i][3] == true) {
            row += '<td class="positive"><i class="icon checkmark"></i> Approved </td>'
        } else {
            row += '<td class="negative"><i class="icon close"></i> Proceeding </td>'
        }


        row += "</tr>";
    }
    $('#trans_tbody').append(row);
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