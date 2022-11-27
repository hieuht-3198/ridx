from datetime import datetime
import importlib
# import logging

from fastapi import BackgroundTasks, FastAPI, Request, UploadFile, Form, Depends
from app.config.auth import get_password_hash
# from fastapi_utils.timing import add_timing_middleware, record_timing

from app.handle.exception import CustomHTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.model.user import User, UserRole
from app.router.base import get_admin, get_current_user

from core.crawl.src.main import get_cpe, get_cpe_dict, mapping_config

if __name__ == "__main__":
    import sys
    if len(sys.argv) >= 2:
        import time
        from core.crawl.src.main import get_cve, get_cwe
        import asyncio


        loop = asyncio.get_event_loop()
        
        async def crawl_data():
            t0 = time.time()
            if sys.argv[1] in 'create-admin':
                user = await User.find_one({'email': 'admin@ridx.com'})
                if user:
                    print('Admin account is existed')
                else:
                    user_data = {
                        'email': 'admin@ridx.com',
                        'password': get_password_hash('12345678'),
                        'role': UserRole.ADMIN.value,
                        'created_at': datetime.now(),
                        'updated_at': datetime.now(),
                        'active': True,
                    }
                    await User.insert_one(user_data)
                    print('Create admin success!')
            elif sys.argv[1] in 'import':
                if 'cve' in sys.argv:
                    await get_cve(isUpdate=False, delete=True)
                if 'cwe' in sys.argv:
                    await get_cwe()
                if 'cpe-match' in sys.argv:
                    await get_cpe()
                if 'cpe-dict' in sys.argv:
                    await get_cpe_dict()
                if 'cve' in sys.argv or 'cpe-match' in sys.argv:
                    await mapping_config()
            elif sys.argv[1] in 'update':
                if 'cve' in sys.argv:
                    await get_cve(isUpdate=True, delete=True)
                if 'cwe' in sys.argv:
                    await get_cwe()
                if 'cpe-match' in sys.argv:
                    await get_cpe()
                # TODO: update cpe
            else:
                print('Error: python main.py import/update [entity]')
            t1 = time.time()            
            print("All in {:.2f}s".format(t1-t0))
        loop.run_until_complete(crawl_data())
    else:
        print('Error: python main.py import/update [entity]')
        exit(0)
else:
    # logging.basicConfig(level=logging.INFO)
    # logger = logging.getLogger(__name__)
    app = FastAPI(docs_url="/api/docs", openapi_url='/api/openapi.json')
    # add_timing_middleware(app, record=logger.info, prefix="app")

    update_database_mode = False
    updating_database = False

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


    @app.middleware('http')
    async def middleware(request: Request, call_next):
        global update_database_mode, updating_database
        if update_database_mode:
            url = str(request.url).replace(str(request.base_url), '/')
            if url == '/api/nvd' and request.method == 'POST' and not updating_database:
                return await call_next(request)
            return JSONResponse(
                status_code=503,
                content=jsonable_encoder({
                    'message': 'Service unavailable',
                }),
            )
        return await call_next(request)


    @app.get("/api")
    async def read_root():
        return {"Hello": "World"}


    @app.post('/api/nvd')
    async def sync_database(background_tasks: BackgroundTasks):  # need add body
        global update_database_mode, updating_database
        if update_database_mode:
            background_tasks.add_task(sync_db)
            updating_database = True
            return {
                'status': True,
                'message': 'Sync database doing',
            }
        return {
            'status': False,
            'message': 'Please change update database mode is on!',
        }


    @app.get('/api/database_mode')
    async def turn_on_update_database_mode(user: dict = Depends(get_admin)):
        global update_database_mode
        update_database_mode = True
        return {
            'status': True,
            'message': 'Ok',
        }

    @app.post('/api/upload_file')
    async def create_upload_file(file: UploadFile = Form(default=None)):
        return file


    @app.exception_handler(CustomHTTPException)
    async def http_exception_handler(request: Request, exc: CustomHTTPException):
        return JSONResponse(
            status_code=exc.status_code,
            content=jsonable_encoder(exc.custom_body),
        )


    @app.exception_handler(Exception)
    async def http_exception_handler(request: Request, exc: Exception):
        return JSONResponse(
            status_code=500,
            content=jsonable_encoder({
                'error': str(exc),
            }),
        )


    m = importlib.import_module('app.router')
    for key in m.__dict__:
        if 'router' in key:
            app.include_router(
                getattr(m, key)
            )


    def sync_db():
        global update_database_mode
        global updating_database
        get_cve(isUpdate=False)
        get_cwe()
        get_cpe()
        update_database_mode = False
        updating_database = False
