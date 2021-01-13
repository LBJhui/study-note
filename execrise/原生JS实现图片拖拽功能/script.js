//第一步 获取节点
const fill = document.querySelector(".fill");
const empties = document.querySelectorAll(".empty");

//第二步 fill的事件监听
fill.addEventListener("dragstart", dragStart);
fill.addEventListener("dragend", dragEnd);

//第四步 循环empty盒子并设置事件监听
for (const empty of empties) {
  empty.addEventListener("dragover", dragOver);
  empty.addEventListener("dragenter", dragEnter);
  empty.addEventListener("dragleave", dragLeave);
  empty.addEventListener("drop", dragDrop);
}

//第三步 fill拖动函数
function dragStart() {
  this.className += " holder";
  setTimeout(() => {
    this.className = "invisible";
  }, 0);
}

function dragEnd() {
  this.className = "fill";
}

//第五步 empty函数
function dragOver(e) {
  e.preventDefault();
}
function dragEnter(e) {
  e.preventDefault();
  this.className += " hovered";
}
function dragLeave() {
  this.className = "empty";
}
function dragDrop() {
  this.className = "empty";
  this.append(fill);
}
