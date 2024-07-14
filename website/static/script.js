function followUser(userId) {
  fetch(`/follow/${userId}`, {
    method: "POST",
    body: JSON.stringify({ userId: userId }),
  })
    .then((response) => {
      if (response.ok) {
        console.log(`Successfully followed user with ID ${userId}`);
      } else {
        console.error("Failed to follow user");
      }
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}

function unfollowUser(userId) {
  fetch(`/unfollow/${userId}`, {
    method: "POST",
    body: JSON.stringify({ userId: userId }),
  })
    .then((response) => {
      if (response.ok) {
        console.log(`Successfully unfollowed user with ID ${userId}`);
      } else {
        console.error("Failed to unfollow user");
      }
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}
