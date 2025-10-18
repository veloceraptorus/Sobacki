import uvicorn
from fastapi import FastAPI
from fastapi.routing import APIRouter

from src.config import settings
# from src.routes.auto import router as auto_router
# from src.routes.shit import router as kaka_router
# from src.routes.dogs import router as dogo_router

router = APIRouter(prefix=settings.BASE_ROUTE_PATH)

app = FastAPI(
    openapi_url=f"{settings.BASE_ROUTE_PATH}/openapi.json",
    docs_url=f"{settings.BASE_ROUTE_PATH}/docs",
)

# router.include_router(kaka_router, prefix='/poop', tags=['Говно'])
# router.include_router(auto_router, prefix='/car', tags=['Не говно'])
# router.include_router(dogo_router, prefix='/dog', tags=['Сэбэки'])

app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='localhost',
        port=8000,
        reload=True,
    )
