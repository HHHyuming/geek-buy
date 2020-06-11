let wrap_el = document.querySelector(".swiper-wrap");
let next_el = document.querySelector(".arrow_right");
let prev_el = document.querySelector(".arrow_left");
let swiper_timer = null;
let swiper_index = 0;
let container_el = document.querySelector(".swiper-main");
let spans_el = document.querySelectorAll(".switch-swiper");

function next_pic() {
  let new_left = parseInt(wrap_el.style.left) - 600;

  if (new_left === -3000) {
    new_left = 0;
  }
  wrap_el.style.left = new_left + "px";
}

function prev_pic() {
  let new_left = parseInt(wrap_el.style.left) + 600;
  if (new_left === 600) {
    new_left = -2400;
  }
  wrap_el.style.left = new_left + "px";
}

next_el.onclick = function () {
  next_pic();
};

prev_el.onclick = function () {
  console.log("上一张");
  prev_pic();
};

function auto_play() {
  spans_el[swiper_index].style.backgroundColor = "orange";

  swiper_timer = setInterval(function () {
    swiper_index += 1;

    if (swiper_index > 4) {
      swiper_index = 0;
    }
    console.log(swiper_index);

    spans_el[swiper_index].style.backgroundColor = "orange";
    spans_el.forEach((ele, i) => {
      if (i !== swiper_index) {
        ele.style.backgroundColor = "";
      }
    });
    next_pic();
  }, 1000);
}

container_el.onmouseenter = function () {
  clearInterval(swiper_timer);
};
container_el.onmouseleave = function () {
  auto_play();
};

spans_el.forEach((ele, i) => {
  ele.onmouseenter = function () {
    spans_el.forEach((subel) => {
      subel.style.backgroundColor = "";
    });
    ele.style.backgroundColor = "orange";
    wrap_el.style.left = i * -600 + "px";
    swiper_index = i;
  };
});
auto_play();
