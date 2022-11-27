# Setup
## 1. System Requirements (for Ubuntu 20.04 LTS)
- Minimum 8GB RAM
- Docker and Docker-compose installed ( Docker version 19.03.13, build 4484c46d9d, Docker-compose version 1.27.4, build 40524192)

## 2. Setup
- Project structure
```
- <Project_name>
    |--- docker
    |--- core
        |--- server
        |--- web
```
- Go to *<Project_name>/docker* folder and follow attached README.md
- Go to *<Project_name>/core/server* folder and follow attached README.md

## 3. Init
- Go to *<Project_name>/docker*
```
./project up
```
In Terminal 1
```
./project sh react
yarn
yarn start
```
In Terminal 2
```
./project sh fastapi
uvicorn main:app —host 0.0.0.0
```
After accessing http://localhost/

To stop running
```
cd <Project_name>/docker
./project down
```

## 4. Init data
### Create an admin account
- Access folder <Project_name>/docker
```
./project sh fastapi
python3 main.py create-admin
```
- The system automatically generates an admin account
```
- Email: admin@ridx.com
- Password: 12345678
```
### Initialize data CVE, CPE, CWE
- Access folder <Project_name>/docker
```
./project sh fastapi
python3 main.py import cve cpe-match cwe cpe-dict
```