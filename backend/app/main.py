from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.main import api_router


app = FastAPI()

# Configure CORS Middleware to share ressources with frontend
origins = ["https://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# All routers will have the prefix "/api"
app.include_router(api_router, prefix="/api", tags=["api"])
