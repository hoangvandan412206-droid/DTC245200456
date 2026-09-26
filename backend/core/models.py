from django.db import models


class Khoa(models.Model):
    ten_khoa = models.CharField(max_length=100)
    mo_ta = models.TextField(blank=True)

    def __str__(self):
        return self.ten_khoa


class BacSi(models.Model):
    ho_ten = models.CharField(max_length=100)
    chuyen_khoa = models.CharField(max_length=100)
    so_dien_thoai = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    khoa = models.ForeignKey(
        Khoa,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="bac_si"
    )

    def __str__(self):
        return self.ho_ten


class BenhNhan(models.Model):
    ho_ten = models.CharField(max_length=100)
    ngay_sinh = models.DateField()
    gioi_tinh = models.CharField(max_length=20)
    so_dien_thoai = models.CharField(max_length=20)
    dia_chi = models.TextField()
    email = models.EmailField(blank=True)
    ngay_tao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ho_ten


class LichKham(models.Model):
    TRANG_THAI_CHOICES = [
        ("cho", "Chờ khám"),
        ("da_xac_nhan", "Đã xác nhận"),
        ("hoan_thanh", "Hoàn thành"),
        ("huy", "Đã hủy"),
    ]

    benh_nhan = models.ForeignKey(
        BenhNhan,
        on_delete=models.CASCADE,
        related_name="lich_kham"
    )
    bac_si = models.ForeignKey(
        BacSi,
        on_delete=models.CASCADE,
        related_name="lich_kham"
    )
    ngay_kham = models.DateField()
    gio_kham = models.TimeField()
    ly_do = models.TextField()
    trang_thai = models.CharField(
        max_length=20,
        choices=TRANG_THAI_CHOICES,
        default="cho"
    )

    def __str__(self):
        return f"{self.benh_nhan} - {self.ngay_kham}"


class HoSoBenhAn(models.Model):
    benh_nhan = models.ForeignKey(
        BenhNhan,
        on_delete=models.CASCADE,
        related_name="ho_so"
    )
    bac_si = models.ForeignKey(
        BacSi,
        on_delete=models.CASCADE,
        related_name="ho_so"
    )
    ngay_kham = models.DateField()
    trieu_chung = models.TextField()
    chan_doan = models.TextField()
    ghi_chu = models.TextField(blank=True)

    def __str__(self):
        return f"Hồ sơ - {self.benh_nhan}"


class Thuoc(models.Model):
    ten_thuoc = models.CharField(max_length=150)
    don_vi = models.CharField(max_length=50)
    gia = models.DecimalField(max_digits=12, decimal_places=2)
    so_luong = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.ten_thuoc


class DonThuoc(models.Model):
    benh_nhan = models.ForeignKey(
        BenhNhan,
        on_delete=models.CASCADE,
        related_name="don_thuoc"
    )
    bac_si = models.ForeignKey(
        BacSi,
        on_delete=models.CASCADE,
        related_name="don_thuoc"
    )
    ngay_ke = models.DateField(auto_now_add=True)
    ghi_chu = models.TextField(blank=True)

    def __str__(self):
        return f"Đơn thuốc #{self.id}"


class ChiTietDonThuoc(models.Model):
    don_thuoc = models.ForeignKey(
        DonThuoc,
        on_delete=models.CASCADE,
        related_name="chi_tiet"
    )
    thuoc = models.ForeignKey(
        Thuoc,
        on_delete=models.CASCADE
    )
    so_luong = models.PositiveIntegerField()
    lieu_dung = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.thuoc} - {self.so_luong}"
