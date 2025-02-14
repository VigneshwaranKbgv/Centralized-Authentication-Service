from fastapi import FastAPI, Request
from contextlib import asynccontextmanager
from .routes import auth, test
from .core.database import engine, Base
from fastapi.middleware.cors import CORSMiddleware
from ..backend.utils.redis_client import redis_client
from fastapi.openapi.docs import get_swagger_ui_html
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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
app = FastAPI(
    title="Centralized Auth Service",
    description="API documentation for authentication service",
    version="1.0.0",
    docs_url=None,
    lifespan=lifespan
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# Include routers with proper prefixes
app.include_router(auth.router)  # This will now handle /auth/* routes
app.include_router(test.router)

# Root endpoint
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="API Documentation",
        swagger_favicon_url="/static/favicon.ico"
    )

@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Request: {request.method} {request.url.path}")
    response = await call_next(request)
    logger.info(f"Response Status: {response.status_code}")
    return response