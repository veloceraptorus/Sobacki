import uvicorn
from fastapi import FastAPI
from fastapi.routing import APIRouter

from src.config import settings
from src.routers.client import router as client_router
from src.routers.permitions import router as permitions_router
from src.routers.project import router as project_router
from src.routers.subtask import router as subtask_router
from src.routers.tasks import router as tasks_router
from src.routers.worker import router as worker_router
from src.routers.worker_task import router as worker_task_router
# from src.DZ.user.router import router as user_router
# from src.DZ.user_role.router import router as user_role_router

router = APIRouter(prefix=settings.BASE_ROUTE_PATH)

app = FastAPI(
    openapi_url=f"{settings.BASE_ROUTE_PATH}/openapi.json",
    docs_url=f"{settings.BASE_ROUTE_PATH}/docs",
)

router.include_router(project_router, prefix='/project', tags=['Проекты'])
router.include_router(client_router, prefix='/client', tags=['Клиенты'])
router.include_router(permitions_router, prefix='/permitions', tags=['Права'])
router.include_router(tasks_router, prefix='/task', tags=['Задачи'])
router.include_router(subtask_router, prefix='/subtask', tags=['Подзадачи'])
router.include_router(worker_task_router, prefix='/worker_task', tags=['Рабочие задач'])
router.include_router(worker_router, prefix='/worker', tags=['Рабочие'])
# router.include_router(user_router, prefix='/user', tags=['Пользователь'])
# router.include_router(user_role_router, prefix='/user_role', tags=['Роли пользователя'])

app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='localhost',
        port=8000,
        reload=True,
    )
