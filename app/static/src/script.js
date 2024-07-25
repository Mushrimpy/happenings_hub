function removeFollower(follower_id) {
  fetch("/connections/remove-follower", {
    method: "POST",
    body: JSON.stringify({ follower_id: follower_id }),
  }).then((_res) => {
    window.location.href = "/connections/followers";
  });
}

function unfollowUser(followed_id) {
  fetch("/connections/unfollow", {
    method: "POST",
    body: JSON.stringify({ followed_id: followed_id }),
  }).then((_res) => {
    window.location.href = "/connections/following";
  });
}
function acceptRequest(request_id) {
  fetch("/connections/accept-request", {
    method: "POST",
    body: JSON.stringify({ request_id: request_id }),
  }).then((_res) => {
    window.location.href = "/connections/followers";
  });
}

function declineRequest(request_id) {
  fetch("/connections/decline-request", {
    method: "POST",
    body: JSON.stringify({ request_id: request_id }),
  }).then((_res) => {
    window.location.href = "/connections/followers";
  });
}

// Example starter JavaScript for disabling form submissions if there are invalid fields
(function () {
  "use strict";

  // Fetch all the forms we want to apply custom Bootstrap validation styles to
  var forms = document.querySelectorAll(".needs-validation");

  // Loop over them and prevent submission
  Array.prototype.slice.call(forms).forEach(function (form) {
    form.addEventListener(
      "submit",
      function (event) {
        if (!form.checkValidity()) {
          event.preventDefault();
          event.stopPropagation();
        }
        form.classList.add("was-validated");
      },
      false
    );
  });
})();

$(document).ready(function () {
  $(".container").addClass("fade-in");

  $("a.page-link").on("click", function (event) {
    event.preventDefault();
    const linkLocation = this.href;

    // Remove fade-in class and apply fade-out effect
    $(".container").removeClass("fade-in");
    $(".container").css("opacity", "0");
    setTimeout(function () {
      window.location = linkLocation;
    }, 400);
  });
});

// Button to clear image file name
document
  .getElementById("delete-file-button")
  .addEventListener("click", function () {
    document.getElementById("image_file").value = "";
  });

function handleSuccess(pos) {
  document.getElementById("posLat").value = pos.coords.latitude;
  document.getElementById("posLong").value = pos.coords.longitude;
}

function handleError() {
  alert("Ensure location services are enabled");
}

function getPosition() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function (pos) {
      handleSuccess(pos);
    }, handleError);
  } else {
    alert("Geolocation is not supported this browser");
  }
}
