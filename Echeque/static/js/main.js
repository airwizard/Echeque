$(document).ready(function() {
		if (localStorage.getItem('username') != "undefined") {
         //$('#welcome_region').
         document.getElementById('welcome_region').innerHTML = 'Welcome, ' + localStorage.getItem('username');
    } else {
         document.getElementById('welcome_region').innerHTML = 'Welcome';
    }

    // fix menu when passed
    $('.ui.labeled.icon.sidebar').sidebar('toggle');
    $('#menu_list').click(function(event) {
         $('.ui.labeled.icon.sidebar').sidebar('toggle');
		});

});

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


