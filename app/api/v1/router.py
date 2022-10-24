from fastapi import APIRouter
import uuid
from datetime import datetime


router = APIRouter(
    prefix='/v1',
    tags=['v1']
)


@router.get('/')
def index():
    return {'timestamp': datetime.utcnow(), 'uuid': uuid.uuid4()}
