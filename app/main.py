import logging
import time
import uuid

from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware

from utils.env import env
from api.router import router as api_router


logging.config.fileConfig('resources/logging.conf',
                          disable_existing_loggers=False)
logger = logging.getLogger(__name__)

app = FastAPI(
    title=env('PROJECT_NAME', 'Potatoe')
)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    idem = uuid.uuid4().hex
    logger.info(f"rid={idem} start request path={request.url.path}")
    start_time = time.time()

    request.state.request_id = idem
    response = await call_next(request)

    process_time = (time.time() - start_time) * 1000
    formatted_process_time = '{0:.2f}'.format(process_time)
    logger.info(
        f"rid={idem} completed_in={formatted_process_time}ms status_code={response.status_code}")

    return response


# Set all CORS enabled origins
if env('CORS_ORIGINS_ENABLED', True):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router)
