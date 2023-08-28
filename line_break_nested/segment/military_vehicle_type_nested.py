# 6. military vehicles type

alphabet = r"(A|B|C|D|\u0110|E|F|G|H|K|L|M|N|P|Q|R|S|T|U|V|X|Y|Z)"
line_break = r"\/"


# 자동차 및 트랙터: AB-12-34
military_car_and_tractor = r"^" + alphabet + alphabet + r"\d{4}$|" + r"^" + alphabet + alphabet + line_break + r"\d{4}$"

# 오토바이: AB-123
military_motorcycle = r"^" + alphabet + alphabet + r"\d{3}$|" + r"^" + alphabet + alphabet + line_break + r"\d{3}$"

# 군사 트레일러: AB-123RM
military_trailer = r"^" + alphabet + alphabet + r"\d{3}RM$|" + r"^" + alphabet + alphabet + line_break + r"\d{3}RM$"

# 군사 세미 트레일러: AB-123BM
military_semi_trailer = r"^" + alphabet + alphabet + r"\d{3}BM$|" + r"^" + alphabet + alphabet + line_break + r"\d{3}BM$"

# 특수 목적 오토바이: ABS-12-34, ABL-12-34, ABX-12-34
special_purpose_motorcycle = r"^" + alphabet + alphabet + r"(S|L|X)\d{4}$|" + r"^" + alphabet + alphabet + r"(S|L|X)" + line_break + r"\d{4}$"


# json
military_vehicle_type = {
    military_car_and_tractor : "Military Car and Tractor",
    military_motorcycle : "Military Motorcycle",
    military_trailer : "Military Trailer",
    military_semi_trailer : "Military Semi Trailer",
    special_purpose_motorcycle : "Special Purpose Motorcycle"
}



import json

def save_json(file_path, data):
    with open(file_path, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

def make_json_data():
    json_data = {}
    json_data["military_vehicle_type"] = military_vehicle_type
    return json_data

if __name__ == "__main__":
    file_path = "./military_vehicle_type_trie.json"
    json_data = make_json_data()
    save_json(file_path, json_data)
