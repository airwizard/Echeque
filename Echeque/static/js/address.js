$(document).ready(function() {

    showTable();
    $('#addAddress').click(function(event) {
         $('.ui.modal').modal('show');
	});

    $('#add_address_btn').click(function(event){
        $.ajax({
            cache: true,
            type: "post",
            data: {'email': $('#email').val()},
            url: "/transaction/address/",
            dataType: "json",
            async: true,
            error: function (request) {
                addAlert("Connection error");
            },
            success: function (data) {
                $('#myAlert').empty();
                if (data['message'] == 'success') {
                    addRow(JSON.parse(data['data']));
                } else {
                    addWarning(data['message']);
                }
            }
        });
    });
});

function showTable() {
    $('#addr_tbody').empty();
    $.ajax({
        cache: true,
        type: "post",
        url: "/address_book/",
        dataType: "json",
        async: true,
        error: function (request) {
            addAlert("Connection error");
        },
        success: function (data) {
            if (data['message'] == 'success') {
                addTable(JSON.parse(data['data']));
            } else {
                addWarning(data['message']);
            }
        }
    });
}

function addTable(data) {
    $('#addr_tbody').empty();
    var row="";
    for (var i = 0; i < data.length; i++) {
        row += "<tr>";
        for (var j = 0; j < data[i].length; j++) {
            row += "<td>" + data[i][j] + "</td>";
        }
        row += "</tr>";
    }
    $('#addr_tbody').append(row);
}

function addRow(data) {
    var row="<tr>";
    for (var j = 0; j < data.length; j++) {
        row += "<td>" + data[j] + "</td>";
    }
    row += "</tr>";
    $('#addr_tbody').append(row);
}