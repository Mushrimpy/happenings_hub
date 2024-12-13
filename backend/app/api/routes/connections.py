from fastapi import APIRouter
# , Depends, HTTPException, Path, Query
# from motor.motor_asyncio import AsyncIOMotorClient

connections_router = APIRouter()


@connections_router.get("/{user_id}")
async def list_connections(direction: str):
    pass


@connections_router.get("/requests/{user_id}")
async def get_requests(direction: str):
    pass


@connections_router.post("/send-request/{receiver_id}")
async def send_friend_request():
    pass


@connections_router.put("/accept-request/{request_id}")
async def accept_request():
    pass


@connections_router.delete("/delete-request/{request_id}")
async def delete_request():
    pass
