import json
import re

file_path = "./vietnam_regex.json"

# Loading the JSON file
with open(file_path, "r", encoding="utf-8") as json_file:
    patterns = json.load(json_file)

# Generating sample test strings
test_strings = [
    # "QH6253",  # military car, Naval service
    # "AB1234",  # military car
    # "CD567",
    # "XY89",
    # "YZ9",
    # "12AB3456",
    # "12EF890",
    # "59A123482",
    # "12NG123456"

    "59S288308",
    "59U219002",
    "54R26619",
    "59T245990",
    "41MĐ11653",
    "41441NG16",
    "50LD08683",
    "59636NN922",
    "62B169165"
]

# # Checking patterns
# matching_results = {}
# for test_str in sample_strings:
#     matched_value = None
#     for pattern, value in patterns.items():
#         if re.match("^" + pattern + "$", test_str):
#             matched_value = value
#             break
#     matching_results[test_str] = matched_value

# print(matching_results)




# 이중 구조의 json 파일 읽고 매칭
matching_results = {}
for test_str in test_strings:
    matched_categories = []
    for main_category, sub_patterns in patterns.items():

        matched = False
        for pattern, sub_category in sub_patterns.items():
            if re.match(pattern, test_str):
                matched_categories.append((main_category + ":" + sub_category).strip())
                matched = True
                break
        if matched == False:
            matched_categories.append((main_category + ":None").strip())
    matching_results[test_str] = matched_categories


for test_str, matched_categories in matching_results.items():
    print(test_str, matched_categories)



# 행사 차량