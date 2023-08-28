# 2. special series
line_break = r"\/"


alphabet = r"(A|B|C|D|\u0110|E|F|G|H|K|L|M|N|P|Q|R|S|T|U|V|X|Y|Z)"

special_series = r"^T|^\d{2}" + alphabet + alphabet


# T - Temporary Registered Vehicles
# 임시 등록 차량 (자동차와 오토바이 모두)
temporary_registered_vehicle = r"^T"

# CD - sepcialized motorcycles used by the People's Public Security forces, 인민 공공 보안(오토바이만)
public_security_motorcycle = r"^\d{2}CD\d{5}$|^\d{2}CD\d{4}$|^\d{2}CD" + line_break + r"\d{5}$|^\d{2}CD" + line_break + r"\d{4}$"

# KT - vehicles of military enterprises
# 군대 기업 (자동차와 오토바이 모두)
military_enterprise = r"^\d{2}KT\d{5}$|^\d{2}KT\d{4}$|^\d{2}KT" + line_break + r"\d{5}$|^\d{2}KT" + line_break + r"\d{4}$"

# LD - vehicles of enterprises with foreign capital, rented vehicles from foreign countries, and vehicles of foreign companies that have won bids.
# 외국 투자 기업, 외국 렌터카, 외국 기업 입찰 차량 (자동차와 오토바이 모두)
foreign_enterprise = r"^\d{2}LD\d{5}$|^\d{2}LD\d{4}$|^\d{2}LD" + line_break + r"\d{5}$|^\d{2}LD" + line_break + r"\d{4}$"

# DA - vehicles of project management boards funded by foreign investment
# 외국 투자로 구성된 프로젝트 관리단 차량(자동차와 오토바이 모두)
project_management = r"^\d{2}DA\d{5}$|^\d{2}DA\d{4}$|^\d{2}DA" + line_break + r"\d{5}$|^\d{2}DA" + line_break + r"\d{4}$"

# R, RM - trailers and semi-trailers
# 트레일러와 세미트레일러, 2020년에는 R, 2023년에는 RM
trailer = r"^\d{2}R\d{5}$|^\d{2}R\d{4}$|^\d{2}RM\d{5}$|^\d{2}R" + line_break + r"\d{5}$|^\d{2}R" + line_break + r"\d{4}$|^\d{2}RM" + line_break + r"\d{5}$"

# MK1 ~ MK9 - tractors
# 트랙터 (현재와 이전 버전을 의미)
tractor = r"^\d{2}MK[1-9]\d{5}$|^\d{2}MK[1-9]\d{4}$|^\d{2}MK[1-9]" + line_break + r"\d{5}$|^\d{2}MK[1-9]" + line_break + r"\d{4}$"

# MĐ1 ~ MĐ9 - electric motorcycles
# 전기 오토바이 (현재와 이전 버전을 의미)
electric_motorcycle = r"^\d{2}MĐ[1-9]\d{5}$|^\d{2}MĐ[1-9]\d{4}$|^\d{2}MĐ[1-9]" + line_break + r"\d{5}$|^\d{2}MĐ[1-9]" + line_break + r"\d{4}$"

# TĐ - domestically produced or assembled mechanical vehicles for pilot deployment
# 베트남에서 생산, 조립된 차량에 대한 시험 운행 (자동차와 오토바이 모두?)
domestic_pilot_deployment = r"^\d{2}TĐ\d{5}$|^\d{2}TĐ\d{4}$|^\d{2}TĐ" + line_break + r"\d{5}$|^\d{2}TĐ" + line_break + r"\d{4}$"

# HC - cars with limited operational scope
# 운행 제한 차량. 특정 지역이나 시간대 등의 조건 하에서만 운행 (현재와 이전 버전의 자동차)
limited_operational_car = r"^\d{2}HC\d{5}$|^\d{2}HC\d{4}$|^\d{2}HC" + line_break + r"\d{5}$|^\d{2}HC" + line_break + r"\d{4}$"


# 숫자 7개
# 행사 임시 차량
event_vehicle = r"^\d{7}$|^\d{2}" + line_break + r"\d{5}$"


# json
special_series = {
    temporary_registered_vehicle : "Temporary Registered Vehicle",
    public_security_motorcycle : "Public Security Motorcycle",
    military_enterprise : "Military Enterprise",
    foreign_enterprise : "Foreign Enterprise",
    project_management : "Project Management",
    trailer : "Trailer",
    tractor : "Tractor",
    electric_motorcycle : "Electric Motorcycle",
    domestic_pilot_deployment : "Domestic Pilot Deployment",
    limited_operational_car : "Limited Operational Car",
    event_vehicle : "Event Vehicle"
}

import json

def save_json(file_path, data):
    with open(file_path, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

def make_json_data():
    json_data = {}
    json_data["special_series"] = special_series
    return json_data

if __name__ == "__main__":
    file_path = "./special_series_trie.json"
    json_data = make_json_data()
    save_json(file_path, json_data)
