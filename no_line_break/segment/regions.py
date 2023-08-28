# 지역 구분
# 11	Cao Bằng
# 12	Lạng Sơn
# 14	Quảng Ninh
# 15	Hải Phòng
# 16	Hải Phòng
# 17	Thái Bình
# 18	Nam Định
# 19	Phú Thọ
# 20	Thái Nguyên
# 21	Yên Bái
# 22	Tuyên Quang
# 23	Hà Giang
# 24	Lào Cai
# 25	Lai Châu
# 26	Sơn La
# 27	Điện Biên
# 28	Hòa Bình
# 29	Hà Nội
# 30	Hà Nội
# 31	Hà Nội
# 32	Hà Nội
# 33	Hà Nội
# 34	Hải Dương
# 35	Ninh Bình
# 36	Thanh Hóa
# 37	Nghệ An
# 38	Hà Tĩnh
# 39	Đồng Nai
# 40	Hà Nội
# 41	Thành phố Hồ Chí Minh
# 43	Đà Nẵng
# 47	Đắk Lắk
# 48	Đắk Nông
# 49	Lâm Đồng
# 50	Thành phố Hồ Chí Minh
# 51	Thành phố Hồ Chí Minh
# 52	Thành phố Hồ Chí Minh
# 53	Thành phố Hồ Chí Minh
# 54	Thành phố Hồ Chí Minh
# 55	Thành phố Hồ Chí Minh
# 56	Thành phố Hồ Chí Minh
# 57	Thành phố Hồ Chí Minh
# 58	Thành phố Hồ Chí Minh
# 59	Thành phố Hồ Chí Minh
# 60	Đồng Nai
# 61	Bình Dương
# 62	Long An
# 63	Tiền Giang
# 64	Vĩnh Long
# 65	Cần Thơ
# 66	Đồng Tháp
# 67	An Giang
# 68	Kiên Giang
# 69	Cà Mau
# 70	Tây Ninh
# 71	Bến Tre
# 72	Bà Rịa – Vũng Tàu
# 73	Quảng Bình
# 74	Quảng Trị
# 75	Thừa Thiên Huế
# 76	Quảng Ngãi
# 77	Bình Định
# 78	Phú Yên
# 79	Khánh Hòa
# 80	Trung ương
# 81	Gia Lai
# 82	Kon Tum
# 83	Sóc Trăng
# 84	Trà Vinh
# 85	Ninh Thuận
# 86	Bình Thuận
# 88	Vĩnh Phúc
# 89	Hưng Yên
# 90	Hà Nam
# 92	Quảng Nam
# 93	Bình Phước
# 94	Bạc Liêu
# 95	Hậu Giang
# 97	Bắc Kạn
# 98	Bắc Giang
# 99	Bắc Ninh


#################### 차량 등록 지역 구분 ####################
region = r"^T?(\d{2})"

region_CaoBang = r"^T?11"
region_LangSon = r"^T?12"
region_QuangNinh = r"^T?14"
region_HaiPhong = r"^T?1[56]"
region_ThaiBinh = r"^T?17"
region_NamDinh = r"^T?18"
region_PhuTho = r"^T?19"
region_ThaiNguyen = r"^T?20"
region_YenBai = r"^T?21"
region_TuyenQuang = r"^T?22"
region_HaGiang = r"^T?23"
region_LaoCai = r"^T?24"
region_LaiChau = r"^T?25"
region_SonLa = r"^T?26"
region_DienBien = r"^T?27"
region_HoaBinh = r"^T?28"
region_HaNoi = r"^T?(29|3[0123]|40)"
region_HaiDuong = r"^T?34"
region_NinhBinh = r"^T?35"
region_ThanhHoa = r"^T?36"
region_NgheAn = r"^T?37"
region_HaTinh = r"^T?38"
region_DongNai = r"^T?(39|60)"
region_HoChiMinh = r"^T?(41|5[0-9])"
region_DaNang = r"^T?43"
region_DakLak = r"^T?47"
region_DakNong = r"^T?48"
region_LamDong = r"^T?49"
region_BinhDuong = r"^T?61"
region_LongAn = r"^T?62"
region_TienGiang = r"^T?63"
region_VinhLong = r"^T?64"
region_CanTho = r"^T?65"
region_DongThap = r"^T?66"
region_AnGiang = r"^T?67"
region_KienGiang = r"^T?68"
region_CaMau = r"^T?69"
region_TayNinh = r"^T?70"
region_BenTre = r"^T?71"
region_BaRiaVungTau = r"^T?72"
region_QuangBinh = r"^T?73"
region_QuangTri = r"^T?74"
region_ThuaThienHue = r"^T?75"
region_QuangNgai = r"^T?76"
region_BinhDinh = r"^T?77"
region_PhuYen = r"^T?78"
region_KhanhHoa = r"^T?79"
region_Government = r"^T?80"
region_GiaLai = r"^T?81"
region_KonTum = r"^T?82"
region_SocTrang = r"^T?83"
region_TraVinh = r"^T?84"
region_NinhThuan = r"^T?85"
region_BinhThuan = r"^T?86"
region_VinhPhuc = r"^T?88"
region_HungYen = r"^T?89"
region_HaNam = r"^T?90"
region_QuangNam = r"^T?92"
region_BinhPhuoc = r"^T?93"
region_BacLieu = r"^T?94"
region_HauGiang = r"^T?95"
region_BacKan = r"^T?97"
region_BacGiang = r"^T?98"
region_BacNinh = r"^T?99"


# json
regions = {
    region_CaoBang : "Cao Bang",
    region_LangSon : "Lang Son",
    region_QuangNinh : "Quang Ninh",
    region_HaiPhong : "Hai Phong",
    region_ThaiBinh : "Thai Binh",
    region_NamDinh : "Nam Dinh",
    region_PhuTho : "Phu Tho",
    region_ThaiNguyen : "Thai Nguyen",
    region_YenBai : "Yen Bai",
    region_TuyenQuang : "Tuyen Quang",
    region_HaGiang : "Ha Giang",
    region_LaoCai : "Lao Cai",
    region_LaiChau : "Lai Chau",
    region_SonLa : "Son La",
    region_DienBien : "Dien Bien",
    region_HoaBinh : "Hoa Binh",
    region_HaNoi : "Ha Noi",
    region_HaiDuong : "Hai Duong",
    region_NinhBinh : "Ninh Binh",
    region_ThanhHoa : "Thanh Hoa",
    region_NgheAn : "Nghe An",
    region_HaTinh : "Ha Tinh",
    region_DongNai : "Dong Nai",
    region_HoChiMinh : "Ho Chi Minh",
    region_DaNang : "Da Nang",
    region_DakLak : "Dak Lak",
    region_DakNong : "Dak Nong",
    region_LamDong : "Lam Dong",
    region_BinhDuong : "Binh Duong",
    region_LongAn : "Long An",
    region_TienGiang : "Tien Giang",
    region_VinhLong : "Vinh Long",
    region_CanTho : "Can Tho",
    region_DongThap : "Dong Thap",
    region_AnGiang : "An Giang",
    region_KienGiang : "Kien Giang",
    region_CaMau : "Ca Mau",
    region_TayNinh : "Tay Ninh",
    region_BenTre : "Ben Tre",
    region_BaRiaVungTau : "Ba Ria Vung Tau",
    region_QuangBinh : "Quang Binh",
    region_QuangTri : "Quang Tri",
    region_ThuaThienHue : "Thua Thien Hue",
    region_QuangNgai : "Quang Ngai",
    region_BinhDinh : "Binh Dinh",
    region_PhuYen : "Phu Yen",
    region_KhanhHoa : "Khanh Hoa",
    region_Government : "Government",
    region_GiaLai : "Gia Lai",
    region_KonTum : "Kon Tum",
    region_SocTrang : "Soc Trang",
    region_TraVinh : "Tra Vinh",
    region_NinhThuan : "Ninh Thuan",
    region_BinhThuan : "Binh Thuan",
    region_VinhPhuc : "Vinh Phuc",
    region_HungYen : "Hung Yen",
    region_HaNam : "Ha Nam",
    region_QuangNam : "Quang Nam",
    region_BinhPhuoc : "Binh Phuoc",
    region_BacLieu : "Bac Lieu",
    region_HauGiang : "Hau Giang",
    region_BacKan : "Bac Kan",
    region_BacGiang : "Bac Giang",
    region_BacNinh : "Bac Ninh"
}

import json

file_path = "./regions.json"
with open(file_path, "w", encoding="utf-8") as json_file:
    json.dump(regions, json_file, ensure_ascii=False, indent=4)