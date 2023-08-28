# 군사 차량 종류에 따른 구분
# 자동차 및 트랙터: AB-12-34
# 오토바이: AB-123
# 군사 트레일러: AB-123RM
# 군사 세미 트레일러: AB-123BM
# 특수 용도 오토바이: ABS-12-34, ABL-12-34, ABX-12-34

# 방법 1. 모든 기호 명시 (AA|AB|...)
# 방법 2. 알파벳 사용 - alphabet + alphabet

alphabet = r"(A|B|C|D|\u0110|E|F|G|H|K|L|M|N|P|Q|R|S|T|U|V|X|Y|Z)"


# 자동차 및 트랙터: AB-12-34
military_cars_and_tractors = r"^" + alphabet + alphabet + r"\d{4}$"

# 오토바이: AB-123
military_motorcycles = r"^" + alphabet + alphabet + r"\d{3}$"

# 군사 트레일러: AB-123RM
military_trailers = r"^" + alphabet + alphabet + r"\d{3}RM$"

# 군사 세미 트레일러: AB-123BM
military_semi_trailers = r"^" + alphabet + alphabet + r"\d{3}BM$"

# 특수 목적 오토바이: ABS-12-34, ABL-12-34, ABX-12-34
special_purpose_motorcycles = r"^" + alphabet + alphabet + r"(S|L|X)\d{4}$"


# json
military_vehicles = {
    military_cars_and_tractors : "military cars and tractors",
    military_motorcycles : "military motorcycles",
    military_trailers : "military trailers",
    military_semi_trailers : "military semi trailers",
    special_purpose_motorcycles : "special purpose motorcycles"
}

import json

file_path = "./military_vehicles_type.json"
with open(file_path, "w", encoding="utf-8") as json_file:
    json.dump(military_vehicles, json_file, ensure_ascii=False, indent=4)