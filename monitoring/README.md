# MediCare - Monitoring & Logging

## Giới thiệu

Hệ thống giám sát và thu thập nhật ký cho dự án MediCare, triển khai bằng Docker Compose trên Ubuntu Linux.

## Công nghệ sử dụng

- Prometheus: Thu thập metrics.
- Grafana: Dashboard và cảnh báo.
- Loki: Lưu trữ và truy vấn logs.
- Promtail: Thu thập logs từ container.
- Node Exporter: Giám sát tài nguyên máy chủ.
- cAdvisor: Giám sát tài nguyên container.
- MySQL Exporter: Thu thập metrics MySQL.

## Cấu hình

Sao chép file môi trường mẫu:

cp .env.example .env

Thay thế các giá trị mẫu bằng thông tin thực tế.

Không đưa file .env chứa mật khẩu lên GitHub.

## Khởi chạy

docker compose up -d

Kiểm tra trạng thái:

docker compose ps

## Dashboard Grafana

Dashboard: MediCare - System Monitoring

Các chỉ số giám sát:

1. CPU Usage
2. RAM Usage
3. Disk Usage
4. Container CPU Usage
5. Container Memory Usage
6. Running Containers

Dashboard được cấu hình qua thư mục grafana-provisioning.

## Cảnh báo

Các quy tắc cảnh báo đã thực hành:

- MediCare - CPU Usage > 70%
- MediCare - RAM Usage > 80%

Grafana được cấu hình gửi thông báo qua Gmail SMTP.

## Truy vấn LogQL

Ví dụ truy vấn log Grafana:

{container="grafana"}

Ví dụ lọc log lỗi:

{container=~".+"} |~ "(?i)(error|warn|failed|exception)"

## Lưu ý

Stack giám sát độc lập với ứng dụng Django MediCare.

Không chạy docker compose down -v nếu cần giữ dữ liệu.

Các địa chỉ dịch vụ, mật khẩu và quyền truy cập cần được cấu hình phù hợp với môi trường triển khai.
