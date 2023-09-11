#include <iostream>
#include "json.hpp"
#include "JSONSearch.h"
#include <chrono>

int main()
{
    // 전체 카테고리의 결과를 저장할 리스트
    std::vector<result_struct> result_list;

    std::string file_path = "vietnam_regex_nested.json";  // JSON 파일 경로
    std::string input_string;
    std::cout << "Input String: ";
    std::cin >> input_string;

    try
    {
        JSONSearch search(file_path);

        auto start = std::chrono::high_resolution_clock::now();

        result_list.push_back(search.search_region(input_string));  // 차량 등록 지역 검색
        result_list.push_back(search.search_special_series(input_string));  // 특수 등록 시리즈 검색
        result_list.push_back(search.search_foreign_country(input_string));  // 외국 차량 검색
        result_list.push_back(search.search_vehicle_type(input_string));  // 외국 차종 검색
        result_list.push_back(search.search_military_unit(input_string));  // 군용 차량 소속 검색

        auto end = std::chrono::high_resolution_clock::now();
        auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start).count();

        //std::cout << "Input String: " << input_string << std::endl;
        std::cout << "Execution Time: " << duration << " us" << std::endl;
        
    }
    catch (const std::exception &e)
    {
        std::cout << e.what() << std::endl;
        return 1;
    }

    for (const auto& result : result_list)
    {
        std::cout << result.category << ": " << result.value << std::endl;
    }

    return 0;


}