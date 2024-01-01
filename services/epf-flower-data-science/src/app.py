from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from src.api.router import router
from pyrate_limiter import (
    RequestRate, MemoryListBucket, Duration, RateLimiter, RequestRateExceeded
)
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
from starlette.types import ASGIApp


class RateLimiterMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp, rate_limiter: RateLimiter) -> None:
        super().__init__(app)
        self.rate_limiter = rate_limiter

    async def dispatch(self, request: Request, call_next):
        try:
            self.rate_limiter.acquire(RequestRate(5, Duration.MINUTE))
        except RequestRateExceeded:
            return Response("Too many requests", status_code=429)

        response = await call_next(request)
        return response


rate_limiter = RateLimiter(MemoryListBucket)


def get_application() -> FastAPI:
    """Create a FastAPI application."""
    application = FastAPI(
        title="epf-flower-data-science",
        description="""Fast API""",
        version="1.0.0",
        redoc_url=None,
    )
    application.add_middleware(
        RateLimiterMiddleware,
        rate_limiter=rate_limiter
    )

    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @application.get("/", include_in_schema=False)
    async def root():
        return RedirectResponse(url='/docs')

    application.include_router(router)

    return application
