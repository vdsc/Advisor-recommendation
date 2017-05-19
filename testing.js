

var genericGetRequest = function(URL, callback){
  var xhr = new XMLHttpRequest();
  xhr.onload = function(){
    if (this.status == 200){
      callback((this.response));
    }
  };
  xhr.open("GET", URL);
  xhr.send();
};

var jsonarray = []; //The word array retrieved from php

var txtinput="";

var inputBox = document.getElementById('input');

//https://prof-recommendation-system-vdsc.c9users.io/solr.php

function testing_app(response) {
    jsonarray = JSON.parse(response);
    for(var i in jsonarray)
    {
        document.getElementById("words").innerHTML += "research = " + jsonarray[i].raw + "<br />";
        document.getElementById("words").innerHTML += "name = " + jsonarray[i].name + "<br />";
        document.getElementById("words").innerHTML += "email = " + jsonarray[i].email + "<br />";
        document.getElementById("words").innerHTML += "site = " + jsonarray[i].site + "<br />";
        //document.getElementById("words").innerHTML += "id = " + jsonarray[i].id + "<br />";
        //document.getElementById("words").innerHTML += "version = " + jsonarray[i]._version + "<br />";
        console.log(jsonarray[i].raw);
        console.log(jsonarray[i].name);
        console.log(jsonarray[i].email);
        console.log(jsonarray[i].site);
        console.log(jsonarray[i].id);
        console.log(jsonarray[i]._version);
        document.getElementById("words").innerHTML += "<br />";
    }
    
   //console.log(jsonarray);
 
    
}

function init_app(response){
    genericGetRequest('https://prof-recommendation-system-vdsc.c9users.io/testing.json', testing_app)
}

function start_app(){
    genericGetRequest('https://prof-recommendation-system-vdsc.c9users.io/testing.php', init_app);
}


//for input text
document.getElementById("enter").addEventListener('click', function(){
  readbox();
  inputBox.value = '';
  txtinput = '';
});


inputBox.addEventListener('keyup',function(e){
    if(e.keyCode == 13) { //Enter keycode
        readbox();
        inputBox.value = '';
        txtinput = '';
   }else{
        txtinput = inputBox.value;
   }
});

function test_query_app(response){
    document.getElementById("words").innerHTML = '';
    genericGetRequest('https://prof-recommendation-system-vdsc.c9users.io/testing.json', testing_app)
}




function readbox()
{   
    var placeholder = txtinput;
    
    console.log(placeholder);
    console.log("yo yo yo");
    var url = "https://prof-recommendation-system-vdsc.c9users.io/testing.php?query="+txtinput;
    
    console.log(url);

    $.get(url, function(dump) {
        document.getElementById("words").innerHTML = '';
        $.getJSON('https://prof-recommendation-system-vdsc.c9users.io/testing.json', function(data) {

        for (var i = 0; i < data.length; i++)
        {
            document.getElementById("words").innerHTML += "<br />" + (i+1) + "<br />";
            document.getElementById("words").innerHTML += "research = " + data[i].raw + "<br />";
            document.getElementById("words").innerHTML += "name = " + data[i].name + "<br />";
            document.getElementById("words").innerHTML += "email = " + data[i].email + "<br />";
            document.getElementById("words").innerHTML += "site = " + data[i].site + "<br />";
            //document.getElementById("words").innerHTML += "id = " + data[i].id + "<br />";
            //document.getElementById("words").innerHTML += "version = " + data[i]._version + "<br />";
            console.log(data[i].raw);
            console.log(data[i].name);
            console.log(data[i].email);
            console.log(data[i].site);
            console.log(data[i].id);
            console.log(data[i]._version);
            document.getElementById("words").innerHTML += "<br />";
        }            
            // $.each(data.items, function(key, val) {
            //     document.getElementById("words").innerHTML += "raw = " + val.raw + "<br />";
            //     document.getElementById("words").innerHTML += "name = " + val.name + "<br />";
            //     document.getElementById("words").innerHTML += "email = " + val.email + "<br />";
            //     document.getElementById("words").innerHTML += "site = " + val.site + "<br />";
            //     document.getElementById("words").innerHTML += "id = " + val.id + "<br />";
            //     document.getElementById("words").innerHTML += "version = " + val._version + "<br />";
            //     console.log(val.raw);
            //     console.log(val.name);
            //     console.log(val.email);
            //     console.log(val.site);
            //     console.log(val.id);
            //     console.log(val._version);
            //     document.getElementById("words").innerHTML += "<br />";
                
            // });
          
        });
    });
    // genericGetRequest(url, test_query_app);
    
    
}
//to reset the text box on page reload
function init() {
    // Clear forms here
    inputBox.value = "";
    start_app();
}

window.onload = init;



