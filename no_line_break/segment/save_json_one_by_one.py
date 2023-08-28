# 각 파일 내에서 사용

import json

file_path = "./military_vehicles.json"
with open(file_path, "w", encoding="utf-8") as json_file:
    json.dump(military_vehicles, json_file, ensure_ascii=False, indent=4)

file_path