#include "JSONSearch.h"
#include <fstream>
#include <regex>

std::string line_break = "\\/";

JSONSearch::JSONSearch(const std::string &file_path)
{
    std::ifstream file(file_path);
    if (!file.is_open())
    {
        throw std::runtime_error("Failed to open the file.");
    }
    file >> json_data;
}


// 1. search region
result_struct JSONSearch::search_region(const std::string &input_string) const
{
    std::string region_code = input_string;   // 입력 문자열을 복사
    result_struct region_result("region");

    if (input_string[0] == 'T') {  // T로 시작하는 경우
        region_code = region_code.substr(1, 2);  // 등록 지역 숫자만 추출
    } else {  // 차량 등록 지역 숫자로 시작하는 경우
        region_code = region_code.substr(0, 2);  // 등록 지역 숫자만 추출
    }

    if (!json_data.contains("region"))  // JSON 파일에 카테고리가 없는 경우
    {
        region_result.value = "No region key in JSON file.";
        return region_result;
    }

    const nlohmann::json *current = &json_data["region"];
    for (char c : region_code)
    {
        if (current->find(std::string(1, c)) == current->end())  // 해당 지역이 없는 경우
        {
            return region_result;
        }
        current = &((*current)[std::string(1, c)]);  // 다음 문자로 이동
    }
    if (current->is_string())  // 해당 지역이 있는 경우
    {
        region_result.value = *current;
        return region_result;
    }
    
    return region_result;
}


// 2. search special_series
result_struct JSONSearch::search_special_series(const std::string &input_string) const
{
    result_struct special_series_result("special_series");

    if (!json_data.contains("special_series"))  // JSON 파일에 카테고리가 없는 경우
    {
        special_series_result.value = "No special_series key in JSON file.";
        return special_series_result;
    }

    const nlohmann::json *current = &json_data["special_series"];
    
    for (const auto&[regex, name] : current->items())
    {
        std::regex pattern(regex);

        if (std::regex_search(input_string, pattern))
        {
            special_series_result.value = name;
            return special_series_result;
        }
    }

    return special_series_result;
}


// 3. search foreign_country
result_struct JSONSearch::search_foreign_country(const std::string &input_string) const {
    result_struct foreign_country_result("foreign_country");
    std::string country_code;

    // 정규표현식 패턴
    // "^\d{2}(001|002|003|004|005)(NG|QT|CV|NN)\d{2,3}$|^\d{2}(NG|QT|CV|NN)(001|002|003|004|005)\d{2,3}$|" + r"^\d{2}(001|002|003|004|005)" + line_break + r"(NG|QT|CV|NN)\d{2,3}$|^\d{2}(NG|QT|CV|NN)" + line_break + r"(001|002|003|004|005)\d{2,3}$"
    std::string regex_pattern1 = "^\\d{5}(NG|QT|CV|NN)\\d{2,3}$";
    std::string regex_pattern2 = "^\\d{2}(NG|QT|CV|NN)\\d{5,6}$";
    std::string regex_pattern3 = "^\\d{5}" + line_break + "(NG|QT|CV|NN)\\d{2,3}$";
    std::string regex_pattern4 = "^\\d{2}(NG|QT|CV|NN)"+ line_break +"\\d{5,6}$";

    std::regex foreign_country_pattern1(regex_pattern1);
    std::regex foreign_country_pattern2(regex_pattern2);
    std::regex foreign_country_pattern3(regex_pattern3);
    std::regex foreign_country_pattern4(regex_pattern4);

    if (!json_data.contains("foreign_country"))  // JSON 파일에 카테고리가 없는 경우
    {
        foreign_country_result.value = "No foreign_country key in JSON file.";
        return foreign_country_result;
    }
    
    /* 입력 문자열을 정규표현식에 매칭시켜서 외국인 번호판 형식과 맞는지 검사 후 국가 코드 추출*/
        if (std::regex_search(input_string, foreign_country_pattern1)) {
        country_code = input_string.substr(2, 3);
    } else if (std::regex_search(input_string, foreign_country_pattern2)) {
        country_code = input_string.substr(4, 3);
    } else if (std::regex_search(input_string, foreign_country_pattern3)) {
        country_code = input_string.substr(2, 3);
    } else if (std::regex_search(input_string, foreign_country_pattern4)) {
        country_code = input_string.substr(5, 3);
    } else {
        return foreign_country_result;  // 외국인 번호판 형식이 아닌 경우 "None" 리턴
    }

    const nlohmann::json *current = &json_data["foreign_country"];  // JSON 객체
    for (char c : country_code)
    {
        if (current->find(std::string(1, c)) == current->end())  // 해당 국가가 없는 경우
        {
            return foreign_country_result;
        }
        current = &((*current)[std::string(1, c)]);  // 다음 문자로 이동
    }
    if (current->is_string())  // 해당 국가가 있는 경우
    {
        foreign_country_result.value = *current;
        return foreign_country_result;
    }
    
    return foreign_country_result;
}


// 4. search foreign_vehicle_type
result_struct JSONSearch::search_foreign_vehicle_type(const std::string &input_string) const {
    result_struct foreign_vehicle_type_result("foreign_vehicle_type");

    if (!json_data.contains("foreign_vehicle_type"))  // JSON 파일에 카테고리가 없는 경우
    {
        foreign_vehicle_type_result.value = "No foreign_vehicle_type key in JSON file.";
        return foreign_vehicle_type_result;
    }

    const nlohmann::json *current = &json_data["foreign_vehicle_type"];
    
    for (const auto&[regex, name] : current->items())
    {
        std::regex pattern(regex);

        if (std::regex_search(input_string, pattern))
        {
            foreign_vehicle_type_result.value = name;
            return foreign_vehicle_type_result;
        }
    }

    return foreign_vehicle_type_result;
}


// 5. search military vehicle type
result_struct JSONSearch::search_military_vehicle_type(const std::string &input_string) const {
    result_struct military_vehicle_type_result("military_vehicle_type");

    if (!json_data.contains("military_vehicle_type"))  // JSON 파일에 카테고리가 없는 경우
    {
        military_vehicle_type_result.value = "No military_vehicle_type key in JSON file.";
        return military_vehicle_type_result;
    }

    const nlohmann::json *current = &json_data["military_vehicle_type"];
    
    for (const auto&[regex, name] : current->items())
    {
        std::regex pattern(regex);

        if (std::regex_search(input_string, pattern))
        {
            military_vehicle_type_result.value = name;
            return military_vehicle_type_result;
        }
    }

    return military_vehicle_type_result;
}


// 6. search military unit
result_struct JSONSearch::search_military_unit(const std::string &input_string) const {
    result_struct military_unit_result("military_unit");

    std::string military_unit = input_string.substr(0, 2);

    if (!json_data.contains("military_unit"))  // JSON 파일에 카테고리가 없는 경우
    {
        military_unit_result.value = "No military_unit key in JSON file.";
        return military_unit_result;
    }

    const nlohmann::json *current = &json_data["military_unit"];
    for (char c : military_unit)
    {
        if (current->find(std::string(1, c)) == current->end())  // 해당 소속이 없는 경우
        {
            return military_unit_result;
        }
        current = &((*current)[std::string(1, c)]);  // 다음 문자로 이동
    }
    if (current->is_string())  // 해당 소속이 있는 경우
    {
        military_unit_result.value = *current;
        return military_unit_result;
    }
    
    return military_unit_result;
}