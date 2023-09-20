#include <iostream>
#include "json.hpp"
#include "lp_analysis.h"
#include <chrono>

int main()
{
    // 전체 카테고리의 결과를 저장할 리스트
    std::map<std::string, std::string> ret;

    std::string file_path = "vietnam_regex_nested.json";  // JSON 파일 경로
    std::string lp;
    std::cout << "lp: ";
    std::cin >> lp;

    try
    {
        LpAnalysis::GetInstance().LoadRegexJson("vietnam_regex_nested.json");

        auto start = std::chrono::high_resolution_clock::now();

        ret = LpAnalysis::GetInstance().Match(lp);

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

    for (const auto& pair : ret)
    {
        std::cout << pair.first << ": " << pair.second << std::endl;
    }
    
    return 0;
}