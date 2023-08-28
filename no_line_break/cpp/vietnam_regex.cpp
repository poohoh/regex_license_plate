#include <iostream>
#include <fstream>
#include <regex>
#include <vector>
#include "json.hpp"
#include <chrono>

nlohmann::json load_json(std::string file_name);
std::vector<std::string> match_regex(std::string input_string, nlohmann::json json_data);
std::string v2s(std::vector<std::string> input_vector);

int main()
{
    std::string input_string = "50MK153482";

    // JSON 파일 읽기
    nlohmann::json json_data;
    json_data = load_json("vietnam_regex.json");

    auto start = std::chrono::high_resolution_clock::now();

    // 정규표현식 매칭
    std::vector<std::string> match_list;
    match_list = match_regex(input_string, json_data);

    auto end = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end-start).count();

    std::cout << "Execution Time: " << duration << " microseconds" << std::endl;

    // 하나의 string으로 변환
    std::string result;
    result = v2s(match_list);

    // 결과 문자열: result 변수
    std::cout << result << std::endl;
}

// JSON 파일 읽기
nlohmann::json load_json(std::string filename)
{
    std::ifstream input_file(filename);
    if (!input_file.is_open())
    {
        std::cout << "Error opening file" << std::endl;
        return 1;
    }

    nlohmann::json json_data;
    input_file >> json_data;
    return json_data;
}

// 정규표현식 매칭
std::vector<std::string> match_regex(std::string input_string, nlohmann::json json_data)
{
    std::vector<std::string> match_list;

    // 모든 최상위 키를 순회
    for (const auto &[main_category, top_value] : json_data.items()) {
        bool matched = false;

        // 해당 카테고리의 모든 키-값 쌍을 검사
        for (const auto &[regex, name] : top_value.items()) {
            std::regex pattern(regex);

            std::smatch matches;
            if (std::regex_search(input_string, matches, pattern)) {
                std::string result = main_category + ": " + name.get<std::string>();
                match_list.push_back(result);
                matched = true;
            }
        }
        if (!matched) {
            std::string result = main_category + ": " + "None";
            match_list.push_back(result);
        }
    }

    return match_list;
}

// vector to string
std::string v2s(std::vector<std::string> input_vector)
{
    std::string delimiter = ", ";
    std::string result = "";

    for (size_t i=0; i<input_vector.size(); i++) {
        result += input_vector[i];
        if (i != input_vector.size()-1) {
            result += delimiter;
        }
    }

    return result;
}