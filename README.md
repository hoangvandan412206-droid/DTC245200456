# MediCare - Hệ thống quản lý bệnh viện

## 1. Giới thiệu

MediCare là hệ thống quản lý bệnh viện được phát triển bằng Django và PostgreSQL, triển khai bằng Docker Compose trên Ubuntu.

Dự án sử dụng Nginx làm Reverse Proxy và pgAdmin để hỗ trợ quản trị cơ sở dữ liệu.

## 2. Công nghệ sử dụng

- Python và Django: Xây dựng ứng dụng Web.
- PostgreSQL: Lưu trữ dữ liệu.
- Nginx: Reverse Proxy và phục vụ tài nguyên tĩnh.
- Docker và Docker Compose: Đóng gói và triển khai dịch vụ.
- pgAdmin: Quản trị PostgreSQL.
- Ubuntu Linux: Môi trường triển khai.

## 3. Kiến trúc hệ thống

Người dùng
    |
    v
Nginx (Port 80)
    |
    v
Django Web (Port 8000)
    |
    v
PostgreSQL (Port 5432)

pgAdmin (Port 5050) hỗ trợ quản trị PostgreSQL.

Các dịch vụ được kết nối thông qua mạng Docker riêng.

## 4. Cấu trúc dự án

hospital-management/
    backend/
        Dockerfile
        manage.py
        requirements.txt
    nginx/
        default.conf
    docker-compose.yml
    .env.example
    .gitignore
    README.md

## 5. Yêu cầu hệ thống

- Ubuntu Linux hoặc hệ điều hành hỗ trợ Docker.
- Docker Engine.
- Docker Compose Plugin.
- Git.

## 6. Hướng dẫn cài đặt

### Bước 1: Clone repository

git clone https://github.com/hoangvandan412206-droid/hospital-management.git

cd hospital-management

### Bước 2: Cấu hình biến môi trường

cp .env.example .env

Mở file .env và thay các giá trị mẫu bằng thông tin phù hợp.

Không sử dụng mật khẩu mẫu trong môi trường thực tế.

### Bước 3: Khởi chạy hệ thống

docker compose up -d --build

### Bước 4: Kiểm tra container

docker compose ps

### Bước 5: Truy cập hệ thống

Website MediCare:
http://localhost/

pgAdmin:
http://localhost:5050/

Khi truy cập từ máy khác, thay localhost bằng địa chỉ IP của máy chủ Ubuntu.

## 7. Các biện pháp bảo mật

- Sử dụng mạng Docker riêng cho các dịch vụ.
- PostgreSQL không công khai cổng trực tiếp ra máy chủ.
- Django chỉ ánh xạ cổng 8000 tới localhost.
- Sử dụng Nginx làm Reverse Proxy.
- Không bật chế độ Privileged cho các container.
- Bổ sung Security Headers trong Nginx.
- Quản lý mật khẩu và Secret Key thông qua biến môi trường.
- Sử dụng .gitignore để tránh đưa file .env lên GitHub.

Lưu ý: pgAdmin hiện công khai cổng 5050 và cần được giới hạn truy cập phù hợp khi triển khai trong môi trường production.

## 8. Giám sát hệ thống

Môi trường thực hành DevOps sử dụng một Docker Compose stack riêng gồm:

- Prometheus: Thu thập metrics.
- Grafana: Hiển thị dashboard và cấu hình cảnh báo.
- Loki: Lưu trữ và truy vấn logs.
- Promtail: Thu thập logs.
- cAdvisor: Giám sát container.
- Node Exporter: Giám sát tài nguyên máy chủ.

Stack giám sát được quản lý riêng trong thư mục lab-monitoring và không nằm trong Docker Compose của repository này.

## 9. Kiểm tra và vận hành

Kiểm tra trạng thái:

docker compose ps

Xem logs:

docker compose logs --tail=100

Kiểm tra cấu hình Nginx:

docker exec hospital-nginx nginx -t

Lưu ý: Không sử dụng docker compose down -v khi cần giữ lại dữ liệu cơ sở dữ liệu.

## 10. Repository

https://github.com/hoangvandan412206-droid/hospital-management
