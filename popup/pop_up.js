var target = document.querySelectorAll('.btn_open');
console.log("target", target);
var btnPopClose = document.querySelectorAll('.pop_wrap .btn_close');
console.log("btnPopClose", btnPopClose);
var targetID;
console.log("targetID", targetID);

// 팝업 열기
for(var i = 0; i < target.length; i++){
  target[i].addEventListener('click', function(){
    targetID = this.getAttribute('href');
    document.querySelector(targetID).style.display = 'block';
  });
}

// 팝업 닫기
for(var j = 0; j < target.length; j++){
  btnPopClose[j].addEventListener('click', function(){
    this.parentNode.parentNode.style.display = 'none';
  });
}