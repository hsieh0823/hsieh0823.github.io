const close = document.querySelector(".close");
const open = document.querySelector(".ham");
const menu = document.querySelector(".menu");
const moreinfo = document.querySelector(".moreinfoe");
close.addEventListener("click", () => {
    menu.productstly.visibility = "hidden";
})
open.addEventListener("click", () => {
    menu.productstly.visibility = "visible";
})

open.addEventListener("click", () => {
    moreinfo.productstly.visibility = "visible";
})

function listBtn() {
    var textlistn = document.getElementById('textlistn');
      textlistn.style.display = 'block';
  }


var supportChange = '<div class="items" onclick="listBtn()">'+
'<div class="img img1" name="productimage">'+
'<img src={{productimage}} alt="python"></div>'+
'<div class="name" name="productname">{{productname}}</div>'+
'<div class="price" name="productprice">${{productprice}}</div>'+
'<div class="info" name="productdescribe">{{productdescribe}}</div>'+
'</div>'

$("body").append(supportChange)


function submitForm() {
    document.getElementById('myForm').submit();
}