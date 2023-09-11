import json

regions_path = "./regions.json"
special_series_path = "./special_series.json"
foreign_country_path = "./foreign_country.json"
foreign_car_type_path = "./foreign_car_type.json"
foreign_motorcycle_type_path = "./foreign_motorcycle_type.json"
military_agencies_and_units_path = "./military_agencies_and_units.json"
military_vehicles_type_path = "./military_vehicles_type.json"

def save_json(file_path):
    with open(regions_path, "r", encoding="utf-8") as json_file:
        regions = json.load(json_file)

    with open(special_series_path, "r", encoding="utf-8") as json_file:
        special_series = json.load(json_file)

    with open(foreign_country_path, "r", encoding="utf-8") as json_file:
        foreign_country = json.load(json_file)

    with open(foreign_car_type_path, "r", encoding="utf-8") as json_file:
        foreign_car_type = json.load(json_file)

    with open(foreign_motorcycle_type_path, "r", encoding="utf-8") as json_file:
        foreign_motorcycle_type = json.load(json_file)

    with open(military_agencies_and_units_path, "r", encoding="utf-8") as json_file:
        military_agencies_and_units = json.load(json_file)

    with open(military_vehicles_type_path, "r", encoding="utf-8") as json_file:
        military_vehicles_type = json.load(json_file)
    
    merged_data = {}
    merged_data["regions"] = regions
    merged_data["special_series"] = special_series
    merged_data["foreign_country"] = foreign_country
    merged_data["foreign_car_type"] = foreign_car_type
    merged_data["foreign_motorcycle_type"] = foreign_motorcycle_type
    merged_data["military_agencies_and_units"] = military_agencies_and_units
    merged_data["military_vehicles_type"] = military_vehicles_type

    with open(file_path, "w", encoding="utf-8") as json_file:
        json.dump(merged_data, json_file, ensure_ascii=False, indent=4)

file_path = "./merged.json"

save_json(file_path)
