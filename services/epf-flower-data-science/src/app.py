from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from src.api.router import router


def get_application() -> FastAPI:
    """Create a FastAPI application."""
    application = FastAPI(
        title="epf-flower-data-science",
        description="""Fast API""",
        version="1.0.0",
        redoc_url=None,
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
