from turtle import title
from fastapi import APIRouter
import uuid
from datetime import datetime
from api.v1.router import router as v1_router


router = APIRouter(
    prefix='/api',
    tags=['api']
)


@router.get('/')
def index():
    return {'timestamp': datetime.utcnow(), 'uuid': uuid.uuid4()}


router.include_router(v1_router)
