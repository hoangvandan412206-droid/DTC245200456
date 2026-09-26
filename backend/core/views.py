from django.shortcuts import render

from .models import (
    BacSi,
    BenhNhan,
    LichKham,
    HoSoBenhAn,
    Thuoc,
    DonThuoc,
    ChiTietDonThuoc,
)


def trang_chu(request):
    context = {
        "so_bac_si": BacSi.objects.count(),
        "so_benh_nhan": BenhNhan.objects.count(),
        "so_lich_kham": LichKham.objects.count(),
        "so_ho_so": HoSoBenhAn.objects.count(),
        "so_thuoc": Thuoc.objects.count(),
        "so_don_thuoc": DonThuoc.objects.count(),
    }

    return render(request, "core/trang_chu.html", context)


def danh_sach_bac_si(request):
    bac_si = BacSi.objects.select_related("khoa").all()

    return render(
        request,
        "core/bac_si.html",
        {
            "bac_si": bac_si,
        },
    )
def danh_sach_benh_nhan(request):
    benh_nhans = BenhNhan.objects.all().order_by("-ngay_tao")

    return render(
        request,
        "core/benh_nhan.html",
        {
            "benh_nhans": benh_nhans,
        },
    )
def danh_sach_lich_kham(request):
    lich_khams = LichKham.objects.select_related(
        "benh_nhan",
        "bac_si"
    ).order_by("-ngay_kham", "-gio_kham")

    return render(
        request,
        "core/lich_kham.html",
        {
            "lich_khams": lich_khams,
        },
    )
def danh_sach_ho_so(request):
    ho_so = HoSoBenhAn.objects.select_related(
        "benh_nhan",
        "bac_si"
    ).order_by("-ngay_kham")

    return render(
        request,
        "core/ho_so.html",
        {
            "ho_so": ho_so,
        },
    )
def danh_sach_thuoc(request):
    thuoc = Thuoc.objects.all().order_by("id")

    return render(
        request,
        "core/thuoc.html",
        {
            "thuoc": thuoc,
        },
    )
def danh_sach_don_thuoc(request):
    don_thuocs = DonThuoc.objects.select_related(
        "benh_nhan",
        "bac_si"
    ).order_by("-ngay_ke")

    return render(
        request,
        "core/don_thuoc.html",
        {
            "don_thuocs": don_thuocs,
        },
    )
def danh_sach_chi_tiet_don_thuoc(request):
    chi_tiets = ChiTietDonThuoc.objects.select_related(
        "don_thuoc",
        "thuoc"
    ).all().order_by("id")

    return render(
        request,
        "core/chi_tiet_don_thuoc.html",
        {
            "chi_tiets": chi_tiets,
        },
    )
