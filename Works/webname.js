//<p id = "demo"></p>//
//<button type = "button" onclick="func()">Next</button>//
//function func(){

  //document.getElementById("GWC").src = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/GWC_logo_2016_.png/1200px-GWC_logo_2016_.png";

//

//document["GWC"].src = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/GWC_logo_2016_.png/1200px-GWC_logo_2016_.png"//

//function func(){

//<document.getElementById("GWC").src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/GWC_logo_2016_.png/1200px-GWC_logo_2016_.png"> </button>

//<img src= "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/GWC_logo_2016_.png/1200px-GWC_logo_2016_.png" Id = "GWC">


var slideIndex = 1;
showDivs(slideIndex);

function plusDivs(n) {
  showDivs(slideIndex += n);
}

function showDivs(n) {
  var i;
  var x = document.getElementsByClassName("mySlides");
  if (n > x.length) {slideIndex = 1}
  if (n < 1) {slideIndex = x.length} ;
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  x[slideIndex-1].style.display = "block";
}
