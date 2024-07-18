function removeFollower(follower_id) {
  fetch("/friends/remove-follower", {
    method: "POST",
    body: JSON.stringify({ follower_id: follower_id }),
  }).then((_res) => {
    window.location.href = "/friends/followers";
  });
}

function unfollowUser(followed_id) {
  fetch("/friends/unfollow", {
    method: "POST",
    body: JSON.stringify({ followed_id: followed_id }),
  }).then((_res) => {
    window.location.href = "/friends/following";
  });
}
function acceptRequest(request_id) {
  fetch("/friends/accept-request", {
    method: "POST",
    body: JSON.stringify({ request_id: request_id }),
  }).then((_res) => {
    window.location.href = "/friends/followers";
  });
}

function declineRequest(request_id) {
  fetch("/friends/decline-request", {
    method: "POST",
    body: JSON.stringify({ request_id: request_id }),
  }).then((_res) => {
    window.location.href = "/friends/followers";
  });
}
