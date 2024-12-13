
'''
async def send_friend_request(db: AsyncIOMotorClient, sender: UserModel, receiver: UserModel):
    pass

async def handle_friend_request(db: AsyncIOMotorClient, current_user: UserModel, sender_id: str, action: RequestAction):
    sender = await db["users"].find_one({"_id": ObjectId(sender_id)})
    if not sender:
        return {"error": "Sender not found"}

    if ObjectId(sender_id) not in current_user.friend_requests_received:
        return {"error": "No friend request from this user"}
    
    if action == RequestAction.ACCEPT:
        # Accept friend request: Add sender to friends list and vice versa
        await db["users"].update_one(
            {"_id": current_user.id},
            {
                "$pull": {"friend_requests_received": ObjectId(sender_id)},
                "$push": {"friends": ObjectId(sender_id)}
            }
        )
        await db["users"].update_one(
            {"_id": ObjectId(sender_id)},
            {
                "$pull": {"friend_requests_sent": current_user.id},
                "$push": {"friends": current_user.id}
            }
        )
        return {"message": "Friend request accepted"}

    elif action == RequestAction.REJECT:
        # Reject friend request: Remove from request lists
        await db["users"].update_one(
            {"_id": current_user.id},
            {"$pull": {"friend_requests_received": ObjectId(sender_id)}}
        )
        await db["users"].update_one(
            {"_id": ObjectId(sender_id)},
            {"$pull": {"friend_requests_sent": current_user.id}}
        )
        return {"message": "Friend request rejected"}


async def list_incoming_friend_requests(db: AsyncIOMotorClient, current_user: UserModel):
    return {"incoming_requests": current_user.friend_requests_received}

async def list_sent_friend_requests(db: AsyncIOMotorClient, current_user: UserModel):
    return {"sent_requests": current_user.friend_requests_sent}

async def list_following(db: AsyncIOMotorClient, current_user: UserModel):
    following = await db["users"].find({"_id": {"$in": current_user.following}}).to_list(None)
    return [user["_id"] for user in following]  # Returning list of user IDs for simplicity

async def list_followers(db: AsyncIOMotorClient, current_user: UserModel):
    followers = await db["users"].find({"_id": {"$in": current_user.followers}}).to_list(None)
    return [user["_id"] for user in followers]

async def unfollow_user(db: AsyncIOMotorClient, current_user: UserModel, unfollow_user_id: str):
    unfollow_user_id = ObjectId(unfollow_user_id)

    # Check if the user is actually being followed
    if unfollow_user_id not in current_user.following:
        return {"error": "You are not following this user"}
    
    # Update current user and unfollowed user
    await db["users"].update_one(
        {"_id": current_user.id},
        {"$pull": {"following": unfollow_user_id}}
    )
    await db["users"].update_one(
        {"_id": unfollow_user_id},
        {"$pull": {"followers": current_user.id}}
    )

    return {"message": "Unfollowed successfully"}

async def remove_follower(db: AsyncIOMotorClient, current_user: UserModel, follower_id: str):
    follower_id = ObjectId(follower_id)

    # Check if the user is actually a follower
    if follower_id not in current_user.followers:
        return {"error": "This user is not following you"}

    # Update current user and follower
    await db["users"].update_one(
        {"_id": current_user.id},
        {"$pull": {"followers": follower_id}}
    )
    await db["users"].update_one(
        {"_id": follower_id},
        {"$pull": {"following": current_user.id}}
    )

    return {"message": "Follower removed successfully"}
    '''