# foreign car type

line_break = r"\/"

# 외교 대표 기관, 영사 기관 및 해당 기관의 외교 ID를 가진 구성원의 차량(NG)
affairs_ambassador = r"^\d{5}NG01$|^\d{2}NG\d{3}01$|" + r"^\d{5}" + line_break + r"NG01$|^\d{2}NG" + line_break + r"\d{3}01$"
affairs_vice_ambassador = r"^\d{5}NG02$|^\d{2}NG\d{3}02$|" + r"^\d{5}" + line_break + r"NG02$|^\d{2}NG" + line_break + r"\d{3}02$"
affairs_staff_car = r"^\d{5}NG(0[3-9]|[1-9][0-9])$|^\d{2}NG\d{3}(0[3-9]|[1-9][0-9])$|" + r"^\d{5}" + line_break + r"NG(0[3-9]|[1-9][0-9])$|^\d{2}NG" + line_break + r"\d{3}(0[3-9]|[1-9][0-9])$"

# 국제 조직의 대표 기관 및 해당 조직의 외교 ID를 가진 구성원의 차량(QT)
international_organization_representative = r"^\d{5}QT01$|^\d{2}QT\d{3}01$|" + r"^\d{5}" + line_break + r"QT01$|^\d{2}QT" + line_break + r"\d{3}01$"
international_organization_staff_car = r"^\d{5}QT(0[2-9]|[1-9][0-9])$|^\d{2}QT\d{3}(0[2-9]|[1-9][0-9])$|" + r"^\d{5}" + line_break + r"QT(0[2-9]|[1-9][0-9])$|^\d{2}QT" + line_break + r"\d{3}(0[2-9]|[1-9][0-9])$"

# 외교 대표 기관, 영사 기관, 국제 조직의 행정 및 기술 직원이 소지한 공무 ID를 가진 차량(CV)
administrative_technical_staff_car = r"^\d{5}CV\d{2}$|^\d{2}CV\d{5}$|" + r"^\d{5}" + line_break + r"CV\d{2}$|^\d{2}CV" + line_break + r"\d{5}$"

# 다른 외국 조직, 대표 사무소, 개인의 차량(NN)
other_foreign_car = r"^\d{5}NN\d{2}$|^\d{2}NN\d{5}$|" + r"^\d{5}" + line_break + r"NN\d{2}$|^\d{2}NN" + line_break + r"\d{5}$"





# foreign motorcycle type


# 외교 대표 기관, 영사 기관 및 해당 기관의 외교 ID를 가진 구성원의 오토바이(NG)
affairs_staff_motorcycle = r"^\d{5}NG\d{3}$|^\d{2}NG\d{6}$|" + r"^\d{5}" + line_break + r"NG\d{3}$|^\d{2}NG" + line_break + r"\d{6}$"

# 국제 조직의 대표 기관 및 해당 조직의 외교 ID를 가진 구성원의 오토바이(QT)
international_organization_staff_motorcycle = r"^\d{5}QT\d{3}$|^\d{2}QT\d{6}$|" + r"^\d{5}" + line_break + r"QT\d{3}$|^\d{2}QT" + line_break + r"\d{6}$"

# 외교 대표 기관, 영사 기관, 국제 조직의 행정 및 기술 직원이 소지한 공무 ID를 가진 구성원의 오토바이(CV)
administrative_technical_staff_motorcycle = r"^\d{5}CV\d{3}$|^\d{2}CV\d{6}$|" + r"^\d{5}" + line_break + r"CV\d{3}$|^\d{2}CV" + line_break + r"\d{6}$"

# 다른 외국 조직, 대표 사무소, 개인의 오토바이(NN)
other_foreign_motorcycle = r"^\d{5}NN\d{3}$|^\d{2}NN\d{6}$|" + r"^\d{5}" + line_break + r"NN\d{3}$|^\d{2}NN" + line_break + r"\d{6}$"




# json
foreign_vehicle_type = {
    affairs_ambassador : "Affairs Ambassador Car",
    affairs_vice_ambassador : "Affairs Vice Ambassador Car",
    affairs_staff_car : "Affairs Staff Car",

    international_organization_representative : "International Organization Representative Car",
    international_organization_staff_car : "International Organization Staff Car",

    administrative_technical_staff_car : "Administrative Technical Staff Car",

    other_foreign_car : "Foreign Car",


    affairs_staff_motorcycle : "Affairs Staff Motorcycle",
    international_organization_staff_motorcycle : "International Organization Staff Motorcycle",
    administrative_technical_staff_motorcycle : "Administrative Technical Staff Motorcycle",
    other_foreign_motorcycle : "Foreign Motorcycle",
}



import json

def save_json(file_path, data):
    with open(file_path, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

def make_json_data():
    json_data = {}
    json_data["foreign_vehicle_type"] = foreign_vehicle_type
    return json_data

if __name__ == "__main__":
    file_path = "./foreign_vehicle_type_trie.json"
    json_data = make_json_data()
    save_json(file_path, json_data)
