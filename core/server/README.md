# Cài đặt
1. Clone repo 
2. Thực hiện các câu lệnh sau 
```
cp .env.example .env
```
3. Cấu hình file *.env*
- DB_HOST: Tên service DB MongoDB trong docker default là mongodb. Trường hợp muốn chạy không dùng docker thì chọn là localhost
- DB_PORT: Cổng của DB
- DB_DATABASE: Tên DB
- DB_USERNAME: Username để truy cập DB
- DB_PASSWORD: Password để truy cập DB
- SERVER_SELECTION_TIMEOUT_MS: Thời gian server chờ tối thiểu để kết nối với DB
- SECRET_KEY: Mã bí mật trong mã hóa JWT
- ALGORITHM: Thuật toán mã hóa JWT
- ACCESS_TOKEN_EXPIRE_MINUTES: Thời gian sống của JWT (đơn vị phút)

# Hướng dẫn sử dụng 
- Để chạy project 
```
uvicorn main:app
```
- Để chạy project với các chế độ khác nhau như debug thì tìm hiểu thêm về uvicorn
