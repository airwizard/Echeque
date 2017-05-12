$(document).ready(function() {
    setInterval('load_table()', 1000);
//load_table();
});


function load_table() {

    $.ajax({
        cache: true,
        type: "post",
        url: "/trans_list/",
        dataType: "json",
        error: function (request) {
            addAlert("Connection error");
        },
        success: function (data) {

            $('#trans_tbody').empty();
            $('#myAlert').empty();
            if (data['message'] == "success") {

                addTable(data['data']);


            } else {
                addWarning(data['message']);
            }
        }
    });



}

function addTable(data) {
    var row="";
    for (var i = 0; i < data.length; i++) {
        row += "<tr>";

        row += "<td>"+ data[i][0] + "</td>";

        row += "<td>"+ data[i][1] + "</td>";

        row += "<td>"+ data[i][2] + "</td>";


        if (data[i][3] == true) {
            row += '<td class="positive"><i class="icon checkmark"></i> Approved </td>'
        } else {
            row += '<td class="negative"><i class="icon close"></i> Proceeding </td>'
        }


        row += "</tr>";
    }
    $('#trans_tbody').append(row);
}


function addWarning(msg) {
    $('#myAlert').empty();
    var row = '<div class="ui warning message"><i class="close icon"></i><div class="header">Warning! </div>';
    row = row + msg;
    row = row + '</div>'
    $('#myAlert').append(row);
}

function addInfo(msg) {
    $('#myAlert').empty();
    var row = '<div class="ui info message"><i class="close icon"></i><div class="header">Info </div>';
    row = row + msg;
    row = row + '</div>'
    $('#myAlert').append(row);
}