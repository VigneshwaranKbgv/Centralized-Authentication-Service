from fastapi import FastAPI
from contextlib import asynccontextmanager
from .routes import auth, test
from .core.database import engine, Base
from fastapi.middleware.cors import CORSMiddleware
from ..backend.utils.redis_client import redis_client

# Create database tables
Base.metadata.create_all(bind=engine)

# Lifespan event handler
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    try:
        redis_client.ping()
        print("Redis connected successfully!")
    except Exception as e:
        print(f"Redis connection error: {e}")
    yield
    # Shutdown logic (optional)
    redis_client.close()

# Initialize FastAPI app with lifespan events
app = FastAPI(lifespan=lifespan)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router)
app.include_router(test.router)

# Root endpoint
@app.get("/")
def read_root():
    return {"Hello": "World"}