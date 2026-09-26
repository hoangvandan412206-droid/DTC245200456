from django.contrib import admin

from .models import (
    Khoa,
    BacSi,
    BenhNhan,
    LichKham,
    HoSoBenhAn,
    Thuoc,
    DonThuoc,
    ChiTietDonThuoc,
)


@admin.register(Khoa)
class KhoaAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "ten_khoa",
        "mo_ta",
    )
    search_fields = (
        "ten_khoa",
    )


@admin.register(BacSi)
class BacSiAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "ho_ten",
        "chuyen_khoa",
        "khoa",
        "so_dien_thoai",
        "email",
    )
    search_fields = (
        "ho_ten",
        "chuyen_khoa",
        "so_dien_thoai",
        "email",
    )
    list_filter = (
        "khoa",
        "chuyen_khoa",
    )


@admin.register(BenhNhan)
class BenhNhanAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "ho_ten",
        "ngay_sinh",
        "gioi_tinh",
        "so_dien_thoai",
        "email",
        "ngay_tao",
    )
    search_fields = (
        "ho_ten",
        "so_dien_thoai",
        "email",
        "dia_chi",
    )
    list_filter = (
        "gioi_tinh",
        "ngay_tao",
    )


@admin.register(LichKham)
class LichKhamAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "benh_nhan",
        "bac_si",
        "ngay_kham",
        "gio_kham",
        "trang_thai",
    )
    search_fields = (
        "benh_nhan__ho_ten",
        "bac_si__ho_ten",
        "ly_do",
    )
    list_filter = (
        "trang_thai",
        "ngay_kham",
    )


@admin.register(HoSoBenhAn)
class HoSoBenhAnAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "benh_nhan",
        "bac_si",
        "ngay_kham",
        "chan_doan",
    )
    search_fields = (
        "benh_nhan__ho_ten",
        "bac_si__ho_ten",
        "trieu_chung",
        "chan_doan",
    )
    list_filter = (
        "ngay_kham",
    )


@admin.register(Thuoc)
class ThuocAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "ten_thuoc",
        "don_vi",
        "gia",
        "so_luong",
    )
    search_fields = (
        "ten_thuoc",
    )
    list_filter = (
        "don_vi",
    )


@admin.register(DonThuoc)
class DonThuocAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "benh_nhan",
        "bac_si",
        "ngay_ke",
        "ghi_chu",
    )
    search_fields = (
        "benh_nhan__ho_ten",
        "bac_si__ho_ten",
        "ghi_chu",
    )
    list_filter = (
        "ngay_ke",
    )


@admin.register(ChiTietDonThuoc)
class ChiTietDonThuocAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "don_thuoc",
        "thuoc",
        "so_luong",
        "lieu_dung",
    )
    search_fields = (
        "thuoc__ten_thuoc",
        "lieu_dung",
    )
