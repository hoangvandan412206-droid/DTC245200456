from django.urls import path

from django.urls import path

from .views import (
    trang_chu,
    danh_sach_bac_si,
    danh_sach_benh_nhan,
    danh_sach_lich_kham,
    danh_sach_ho_so,
    danh_sach_thuoc,
    danh_sach_don_thuoc,
   danh_sach_chi_tiet_don_thuoc,
)

urlpatterns = [
    path("", trang_chu, name="trang_chu"),

    path(
        "bac-si/",
        danh_sach_bac_si,
        name="danh_sach_bac_si",
    ),

    path(
        "benh-nhan/",
        danh_sach_benh_nhan,
        name="danh_sach_benh_nhan",
    ),

    path(
        "lich-kham/",
        danh_sach_lich_kham,
        name="danh_sach_lich_kham",
    ),

    path(
        "ho-so/",
        danh_sach_ho_so,
        name="danh_sach_ho_so",
    ),
path(
    "thuoc/",
    danh_sach_thuoc,
    name="danh_sach_thuoc",
),
path(
    "don-thuoc/",
    danh_sach_don_thuoc,
    name="danh_sach_don_thuoc",
),
path(
    "chi-tiet-don-thuoc/",
    danh_sach_chi_tiet_don_thuoc,
    name="danh_sach_chi_tiet_don_thuoc",
),
]
