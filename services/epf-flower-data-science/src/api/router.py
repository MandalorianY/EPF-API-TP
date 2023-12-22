"""API Router for Fast API."""
from fastapi import APIRouter

from src.api.routes import hello, data, load, processing, split, train, predict, params

router = APIRouter()

router.include_router(hello.router, tags=["Hello"])
router.include_router(data.router, tags=["Data"])
router.include_router(load.router, tags=["Load Dataset"])
router.include_router(processing.router, tags=["Processed Dataset"])
router.include_router(split.router, tags=["Split Dataset"])
router.include_router(train.router, tags=["Train"])
router.include_router(predict.router, tags=["Predict"])
router.include_router(params.router, tags=["Get Parameters"])
