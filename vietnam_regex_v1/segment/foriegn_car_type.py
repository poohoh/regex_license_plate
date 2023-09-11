# # 네 가지 등록 시리즈
# foreign = r"(NG|QT|CV|NN)"
# # 외국인 자동차 번호판 형식
# foreign = r"\d{5}" + foreign + r"\d{2}|\d{2}" + foreign + r"\d{5}"
# # 외국인 오토바이 번호판 형식
# foreign = r"\d{5}" + foreign + r"\d{3}|\d{2}" + foreign + r"\d{6}"


#################### 자동차 시리즈 구분 ####################

# 외교 대표 기관, 영사 기관 및 해당 기관의 외교 ID를 가진 구성원의 차량(NG)
affairs_ambassador = r"^\d{5}NG01$|^\d{2}NG\d{3}01$"
affairs_vice_ambassador = r"^\d{5}NG02$|^\d{2}NG\d{3}02$"
affairs_staff_car = r"^\d{5}NG(0[3-9]|[1-9][0-9])$|^\d{2}NG\d{3}(0[3-9]|[1-9][0-9])$"

# 국제 조직의 대표 기관 및 해당 조직의 외교 ID를 가진 구성원의 차량(QT)
international_organization_representative = r"^\d{5}QT01$|^\d{2}QT\d{3}01$"
international_organization_staff_car = r"^\d{5}QT(0[2-9]|[1-9][0-9])$|^\d{2}QT\d{3}(0[2-9]|[1-9][0-9])$"

# 외교 대표 기관, 영사 기관, 국제 조직의 행정 및 기술 직원이 소지한 공무 ID를 가진 차량(CV)
administrative_technical_staff_car = r"^\d{5}CV\d{2}$|^\d{2}CV\d{5}$"

# 다른 외국 조직, 대표 사무소, 개인의 차량(NN)
other_foreign_car = r"^\d{5}NN\d{2}$|^\d{2}NN\d{5}$"


# json
foreign_car_type = {
    affairs_ambassador : "affairs ambassador car",
    affairs_vice_ambassador : "affairs vice ambassador car",
    affairs_staff_car : "affairs staff car",

    international_organization_representative : "international organization representative car",
    international_organization_staff_car : "international organization staff car",

    administrative_technical_staff_car : "administrative technical staff car",

    other_foreign_car : "foreign car"
}

import json

file_path = "./foreign_car_type.json"
with open(file_path, "w", encoding="utf-8") as json_file:
    json.dump(foreign_car_type, json_file, ensure_ascii=False, indent=4)