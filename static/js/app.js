var updateBtns = document.querySelectorAll(".update-Cart");
console.log(updateBtns);

for (i = 0; i < updateBtns.length; i++) {
  updateBtns[i].addEventListener("click", function () {
    var productId = this.dataset.product;
    var action = this.dataset.action;
    console.log("productId:", productId, "Action:", action);

    console.log("User:", user);

    if (user == "AnonymousUser") {
      console.log("user is not authenticated");
    } else {
      updateUserOrder(productId, action);
    }
  });
}

function updateUserOrder(productId, action) {
  console.log("User is authenticated, sending the data.....");
  var url = "/update_cart/";

  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({ productId: productId, action: action }),
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      console.log("Data:", data);
      location.reload();
    });
}

var owl = $("#indexSlider");
owl.owlCarousel({
  loop: true,
  nav: false,
  autoplay: true,
  dots: false,
  animateOut: "fadeOut",
  responsive: {
    0: {
      items: 1,
    },
    600: {
      items: 1,
    },
    1000: {
      items: 1,
    },
  },
});

$(document).ready(function () {
  $("#testimonial-slider").owlCarousel({
    items: 2,
    itemsDesktop: [1000, 2],
    itemsDesktopSmall: [979, 2],
    itemsTablet: [768, 2],
    itemsMobile: [650, 1],
    pagination: true,
    navigation: false,
    slideSpeed: 1000,
    autoPlay: true,
    responsive: {
      0: {
        items: 1,
      },
      600: {
        items: 1,
      },
      1000: {
        items: 2,
      },
    },
  });
});

$(document).ready(function () {
  $(".About-Us-Icons").waypoint(
    function (direction) {
      $(".About-Us-Icons").addClass("animate__animated animate__fadeInUp");
    },
    {
      offset: "80%",
    }
  );

  $(".discoverPageStory").waypoint(
    function (direction) {
      $(".discoverPageStory").addClass(
        "animate__animated animate__fadeInRight"
      );
    },
    {
      offset: "80%",
    }
  );

  $(".contact").waypoint(
    function (direction) {
      $(".contact").addClass("animate__animated animate__fadeInUp");
    },
    {
      offset: "80%",
    }
  );

  $(".featureSection").waypoint(
    function (direction) {
      $(".featureSection").addClass("animate__animated animate__fadeInUp");
    },
    {
      offset: "80%",
    }
  );
});

//timeline
const tl = gsap.timeline({ defaults: { ease: "power1.out" } });
tl.fromTo("nav", { opacity: 0 }, { opacity: 1, duration: 1 });
tl.fromTo(
  ".caption-animation",
  { opacity: 0, y: 30 },
  { opacity: 1, y: 0, duration: 1 }
);

//menuFilter
filterSelection("drinks");
function filterSelection(c) {
  var x, i;
  x = document.getElementsByClassName("Card");
  console.log(x);
  if (c == "all") c = "";
  for (i = 0; i < x.length; i++) {
    w3RemoveClass(x[i], "show");
    if (x[i].className.indexOf(c) > -1) w3AddClass(x[i], "show");
  }
}

function w3AddClass(element, name) {
  var i, arr1, arr2;
  arr1 = element.className.split(" ");
  arr2 = name.split(" ");
  for (i = 0; i < arr2.length; i++) {
    if (arr1.indexOf(arr2[i]) == -1) {
      element.className += " " + arr2[i];
    }
  }
}

function w3RemoveClass(element, name) {
  var i, arr1, arr2;
  arr1 = element.className.split(" ");
  arr2 = name.split(" ");
  for (i = 0; i < arr2.length; i++) {
    while (arr1.indexOf(arr2[i]) > -1) {
      arr1.splice(arr1.indexOf(arr2[i]), 1);
    }
  }
  element.className = arr1.join(" ");
}

// Add active class to the current button (highlight it)
var btnContainer = document.getElementById("btnContainer");
var btns = btnContainer.getElementsByClassName("productButton");
for (var i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", function () {
    var current = document.getElementsByClassName("current");
    current[0].className = current[0].className.replace(" current", "");
    this.className += " current";
  });
}
