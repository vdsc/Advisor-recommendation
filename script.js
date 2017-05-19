

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

function init_app(response){
    jsonarray = response;
    for(var i in jsonarray)
    {
     console.log(jsonarray[i])
     
        }
    
   //console.log(jsonarray);
 
    
    document.getElementById("words").innerHTML = jsonarray;
}

function start_app(){
    genericGetRequest('https://prof-recommendation-system-vdsc.c9users.io/solr.php', init_app);
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

function readbox()
{   
    var placeholder = txtinput;
    
    console.log(placeholder);
    console.log("yo yo yo");
    
}
//to reset the text box on page reload
function init() {
    // Clear forms here
    inputBox.value = "";
    start_app();
}

window.onload = init;



