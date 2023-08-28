# special series of license plate in Vietnam
# CD, KT, LD, DA, RM, MK1~MK9, MĐ1~MĐ9, TĐ1~TĐ9, HC

# 이전 형식들도 포함함


# CD - sepcialized motorcycles used by the People's Public Security forces, 인민 공공 보안(오토바이만)
public_security_motorcycle = r"^\d{2}CD\d{5}$|^\d{2}CD\d{4}$"

# KT - vehicles of military enterprises
# 군대 기업 (자동차와 오토바이 모두)
military_enterprise = r"^\d{2}KT\d{5}$|^\d{2}KT\d{4}$"

# LD - vehicles of enterprises with foreign capital, rented vehicles from foreign countries, and vehicles of foreign companies that have won bids.
# 외국 투자 기업, 외국 렌터카, 외국 기업 입찰 차량 (자동차와 오토바이 모두)
foreign_enterprise = r"^\d{2}LD\d{5}$|^\d{2}LD\d{4}$"

# DA - vehicles of project management boards funded by foreign investment
# 외국 투자로 구성된 프로젝트 관리단 차량(자동차와 오토바이 모두)
project_management = r"^\d{2}DA\d{5}$|^\d{2}DA\d{4}$"

# R, RM - trailers and semi-trailers
# 트레일러와 세미트레일러, 2020년에는 R, 2023년에는 RM
# 일단 R은 구분 X
trailer = r"^\d{2}RM\d{5}$|^\d{2}RM\d{4}$"

# MK1 ~ MK9 - tractors
# 트랙터 (현재와 이전 버전을 의미)
tractor = r"^\d{2}MK[1-9]\d{5}$|^\d{2}MK[1-9]\d{4}$"

# MĐ1 ~ MĐ9 - electric motorcycles
# 전기 오토바이 (현재와 이전 버전을 의미)
electric_motorcycle = r"^\d{2}MĐ[1-9]\d{5}$|^\d{2}MĐ[1-9]\d{4}$"

# TĐ - domestically produced or assembled mechanical vehicles for pilot deployment
# 베트남에서 생산, 조립된 차량에 대한 시험 운행 (자동차와 오토바이 모두)
domestic_pilot_deployment = r"^\d{2}TĐ\d{5}$|^\d{2}TĐ\d{4}$"

# HC - cars with limited operational scope
# 운행 제한 차량. 특정 지역이나 시간대 등의 조건 하에서만 운행 (현재와 이전 버전의 자동차)
limited_operational_car = r"^\d{2}HC\d{5}$|^\d{2}HC\d{4}$"


# 숫자 7개
# 행사 차량
event_vehicle = r"^\d{7}$"


# json
special_series = {
    public_security_motorcycle : "public security motorcycle",
    military_enterprise : "military enterprise",
    foreign_enterprise : "foreign enterprise",
    project_management : "project management",
    trailer : "trailer",
    tractor : "tractor",
    electric_motorcycle : "electric motorcycle",
    domestic_pilot_deployment : "domestic pilot deployment",
    limited_operational_car : "limited operational car",
    event_vehicle : "event vehicle"
}

import json

file_path = "./special_series.json"
with open(file_path, "w", encoding="utf-8") as json_file:
    json.dump(special_series, json_file, ensure_ascii=False, indent=4)