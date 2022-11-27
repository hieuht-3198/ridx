from starlette.config import Config

config = Config('./.env')

DB_DATABASE = config('DB_DATABASE', cast=str)
DB_USERNAME = config('DB_USERNAME', cast=str)
DB_PASSWORD = config('DB_PASSWORD', cast=str)
DB_HOST = config('DB_HOST', cast=str)
DB_PORT = config('DB_PORT', cast=str)
SERVER_SELECTION_TIMEOUT_MS = config('SERVER_SELECTION_TIMEOUT_MS', cast=int, default=1000)

SECRET_KEY = config('SECRET_KEY', cast=str, default='00b8c82eb2c1abe7e82ed2d87e49b37c9dcdcdb4715e2a282f9c831f24c8c94d')
ALGORITHM = config('ALGORITHM', cast=str, default='HS256')
ACCESS_TOKEN_EXPIRE_MINUTES = config('ACCESS_TOKEN_EXPIRE_MINUTES', cast=int, default=15)

NVD_KEY = config('NVD_KEY', cast=str, default=None)
