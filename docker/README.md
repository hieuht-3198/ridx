# Cài đặt
1. Clone repo 
2. Thực hiện các câu lệnh sau 
```
cp .env.example .env
cp docker-compose.dev docker-compose.yml
```
3. Cấu hình file *.env*
- SERVER_PATH: Đường dẫn đến thư mục server fastapi
- WEB_PATH: Đường dẫn đến thư mục web 
- NGINX_DOCUMENT_ROOT: Đường dẫn thư mục sẽ mount với nginx của web 
- PORT: Cổng ra của máy chủ nginx 
- DB_USERNAME: username của database muốn đặt 
- DB_PASSWORD: password của database muốn đặt
- COMPOSE_PROJECT_NAME: Tên chung các container 
# Hướng dẫn sử dụng 
- Để chạy project 
```
./project up 
```
- Để bash các services 
```
./project sh <service_name>
```
