// 获取所有的 <h4> 元素
var statusElements = document.querySelectorAll(".member-status h4");

// 遍历所有的 <h4> 元素
statusElements.forEach(function(element) {
  // 获取当前 <h4> 元素内的文字内容
  var statusText = element.innerText.trim();

  // 根据状态文字，添加相应的 CSS 类
  if (statusText === "在線") {
    element.classList.add("online");
  } else if (statusText === "離線") {
    element.classList.add("offline");
  }
});