function unfollowUser(follower_id) {
  fetch("/contacts/unfollow", {
    method: "POST",
    body: JSON.stringify({ follower_id: follower_id }),
  }).then((_res) => {
    window.location.href = "/contacts/followers";
  });
}
