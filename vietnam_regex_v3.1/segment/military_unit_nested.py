# 7. military agencies and units

General_Staff_Department = "TM"
Political_General_Department = "TC"
Logistics_General_Department = "TH"
Technical_General_Department = "TT"
Defense_Industry_General_Department = "TK"
General_Department_II = "TN"
Military_Region_1 = "KA"
Military_Region_2 = "KB"
Military_Region_3 = "KC"
Military_Region_4 = "KD"
Military_Region_5 = "KV"
Military_Region_7 = "KP"
Military_Region_9 = "KK"
Hanoi_Capital_Command = "KT"
Army_Corps_1 = "AA"
Army_Corps_2 = "AB"
Army_Corps_3 = "AC"
Army_Corps_4 = "AD"
Air_Defense = "QA"
Naval_Service = "QH"
Border_Guard_Command = "QB"
Marine_Police_Command = "QC"
Command_86 = "QM"
Command_Protection_Ho_Chi_Minh_Mausoleum = "BL"
Armor_Mechanized_Infantry_Corps = "BB"
Engineering_Corps = "BC"
Special_Forces_Corps = "BK"
Artillery_Corps = "BP"
Chemical_Corps = "BH"
Signal_Corps = "BT"
National_Defense_Academy = "HA"
Army_Officer_Academy = "HB"
Political_Officer_Academy = "HC"
Logistics_Academy = "HE"
Military_Technical_Academy = "HD"
Military_Medical_Academy = "HH"
Army_Officer_School_1 = "HT"
Army_Officer_School_2 = "HQ"
Political_Officer_School = "HN"
Foreign_Affairs_Department = "PA"
Vietnam_Peacekeeping_Department = "PG"
Government_Office = "PK"
Military_Science_Technology_Institute = "PQ"
Defense_Design_Institute = "PM"
Viet_Russia_Tropical_Center = "PX"
# Central_Military_Hospital_108 = "pp-10"  # 'PP10'으로 시작하는 것이 맞는지 조사 필요
# Military_Medical_Hospital_175 = "PP-40"
# Military_Traditional_Medicine_Institute = "PP-60"
Military_Unit_11 = "AV"
Military_Unit_12 = "AT"
Military_Unit_15 = "AN"
Military_Unit_16 = "AX"
Military_Unit_18 = "AM"
Military_Telecommunication_Group = "VT"
General_Company_36 = "CA"
Military_Commercial_Joint_Stock_Bank = "CB"
Van_Xuan_General_Import_Export_Company = "CD"
Dong_Bac_General_Company = "CH"
Thai_Son_General_Company = "CM"
Military_Housing_Urban_Development_General_Company = "CN"
General_Company_319 = "CP"
Technical_Application_Production_Company = "CT"
Lung_Lo_Construction_General_Company = "CV"

# json
military_unit = {
    General_Staff_Department : "General Staff Department",
    Political_General_Department : "Political General Department",
    Logistics_General_Department : "Logistics General Department",
    Technical_General_Department : "Technical General Department",
    Defense_Industry_General_Department : "Defense Industry General Department",
    General_Department_II : "General Department II",
    Military_Region_1 : "Military Region 1",
    Military_Region_2 : "Military Region 2",
    Military_Region_3 : "Military Region 3",
    Military_Region_4 : "Military Region 4",
    Military_Region_5 : "Military Region 5",
    Military_Region_7 : "Military Region 7",
    Military_Region_9 : "Military Region 9",
    Hanoi_Capital_Command : "Hanoi Capital Command",
    Army_Corps_1 : "Army Corps 1",
    Army_Corps_2 : "Army Corps 2",
    Army_Corps_3 : "Army Corps 3",
    Army_Corps_4 : "Army Corps 4",
    Air_Defense : "Air Defense",
    Naval_Service : "Naval Service",
    Border_Guard_Command : "Border Guard Command",
    Marine_Police_Command : "Marine Police Command",
    Command_86 : "Command 86",
    Command_Protection_Ho_Chi_Minh_Mausoleum : "Command for the Protection of Ho Chi Minh Mausoleum",
    Armor_Mechanized_Infantry_Corps : "Armor and Mechanized Infantry Corps",
    Engineering_Corps : "Engineering Corps",
    Special_Forces_Corps : "Special Forces Corps",
    Artillery_Corps : "Artillery Corps",
    Chemical_Corps : "Chemical Corps",
    Signal_Corps : "Signal Corps",
    National_Defense_Academy : "National Defense Academy",
    Army_Officer_Academy : "Army Officer Academy",
    Political_Officer_Academy : "Political Officer Academy",
    Logistics_Academy : "Logistics Academy",
    Military_Technical_Academy : "Military Technical Academy",
    Military_Medical_Academy : "Military Medical Academy",
    Army_Officer_School_1 : "Army Officer School 1",
    Army_Officer_School_2 : "Army Officer School 2",
    Political_Officer_School : "Political Officer School",
    Foreign_Affairs_Department : "Foreign Affairs Department",
    Vietnam_Peacekeeping_Department : "Vietnam Peacekeeping Department",
    Government_Office : "Government Office",
    Military_Science_Technology_Institute : "Military Science and Technology Institute",
    Defense_Design_Institute : "Defense Design Institute",
    Viet_Russia_Tropical_Center : "Viet-Russia Tropical Center",
    # Central_Military_Hospital_108 : "Central Military Hospital 108",
    # Military_Medical_Hospital_175 : "Military Medical Hospital 175",
    # Military_Traditional_Medicine_Institute : "Military Traditional Medicine Institute",
    Military_Unit_11 : "Military Unit 11",
    Military_Unit_12 : "Military Unit 12",
    Military_Unit_15 : "Military Unit 15",
    Military_Unit_16 : "Military Unit 16",
    Military_Unit_18 : "Military Unit 18",
    Military_Telecommunication_Group : "Military Telecommunication Group",
    General_Company_36 : "General Company 36",
    Military_Commercial_Joint_Stock_Bank : "Military Commercial Joint Stock Bank",
    Van_Xuan_General_Import_Export_Company : "Van Xuan General Import and Export Company",
    Dong_Bac_General_Company : "Dong Bac General Company",
    Thai_Son_General_Company : "Thai Son General Company",
    Military_Housing_Urban_Development_General_Company : "Military Housing and Urban Development General Company",
    General_Company_319 : "General Company 319",
    Technical_Application_Production_Company : "Technical Application and Production Company",
    Lung_Lo_Construction_General_Company : "Lung Lo Construction General Company"
}



import json
from collections import defaultdict

def save_json(file_path, data):
    with open(file_path, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)



# trie 형식으로 저장
def build_nested_trie():
    def nested_dict():
        return defaultdict(nested_dict)
    
    # trie 구조로 모든 키에 해당하는 데이터를 저장
    def insert_into_trie(trie, key, value):
        current = trie
        for char in key[:-1]:
            if char not in current:
                current[char] = {}
            current = current[char]
        current[key[-1]] = value
    
    trie_structure = nested_dict()

    trie_structure["military_unit"] = {}
    trie_regions = trie_structure["military_unit"]  # trie structure의 foreign country 부분

    for pattern, value in military_unit.items():
        clean_pattern = pattern.strip('^$')
        
        insert_into_trie(trie_regions, clean_pattern, value)
    
    return trie_structure

if __name__ == "__main__":
    file_path = "./military_unit_trie.json"

    sample_trie_data = build_nested_trie()
    
    save_json(file_path, sample_trie_data)