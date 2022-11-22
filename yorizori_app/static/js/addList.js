
// Create a "close" button and append it to each list item
var myNodelist = document.getElementsByClassName("sourceList");
var i;
for (i = 0; i < myNodelist.length; i++) {
var span = document.createElement("SPAN");
var txt = document.createTextNode("\u00D7");
span.className = "close";
span.appendChild(txt);
myNodelist[i].appendChild(span);
}

// Click on a close button to hide the current list item
var close = document.getElementsByClassName("close");
var i;
for (i = 0; i < close.length; i++) {
close[i].onclick = function() {
    var div = this.parentElement;
    div.style.display = "none";
}
}

// Add a "checked" symbol when clicking on a list item
var list = document.querySelector('ul');
list.addEventListener('click', function(ev) {
if (ev.target.calssName === 'sourceList') {
    ev.target.classList.toggle('checked');
}
}, false);

// Create a new list item when clicking on the "Add" button
var s=[];
function newElement() {
    var li = document.createElement("li");
    var inputValue = document.getElementById("myInput").value;
    s.push(inputValue)
    console.log(s)
    var t = document.createTextNode(inputValue);
    li.appendChild(t);
    if (inputValue === '') {
    alert("You must write something!");
    } else {
    document.getElementById("myUL").appendChild(li);
    }
    document.getElementById("myInput").value = "";


    var span = document.createElement("SPAN");
    var txt = document.createTextNode("\u00D7");
    span.className = "close";
    li.className = "sourceList";
    span.appendChild(txt);
    li.appendChild(span);

    for (i = 0; i < close.length; i++) {
    close[i].onclick = function() {
        var div = this.parentElement;
        div.style.display = "none";
    }
    }
}

//csrf token
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

function search() {    
    $.ajax({
        url: '/addSource/',
        type: 'POST',
        data: {
            "mylist": JSON.stringify(s),
            'csrfmiddlewaretoken': csrftoken,
        },
        success: function (data) {
            // window.document.location = "/search/";
            window.location.href = "/search/";
            // location.replace("/search/");
        }
    })
}