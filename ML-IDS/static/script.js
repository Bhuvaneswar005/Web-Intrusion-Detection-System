

var slider = document.getElementById("myRange");
var output = document.getElementById("demo");
output.innerHTML = slider.value;

slider.oninput = function() {
  output.innerHTML = this.value;
}

function checkbox(num)
{
  if(num != 0)   
    document.getElementById(num).checked = true;

};