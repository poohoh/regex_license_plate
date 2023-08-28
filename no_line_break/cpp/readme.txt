<vietnam_regex.cpp>

1. 입력: input_string 변수 (std::string 타입)

2. 출력: result 변수 (std::string 타입)

3. 작동
    1) input_string 변수의 값을 설정 - 매칭시키고자 하는 문자열
    2) JSON 파일 값을 읽음
    3) 전체 정규표현식과 비교하여 일치하는 값을 모두 std::vector 타입의 match_list 변수에 저장
    4) std::vector 타입의 전체 결과 match_list 변수의 값들을 이어 붙여, 하나의 std::string 타입 변수 result으로 저장 후 출력

4. 외부 라이브러리: nlohmann/json (nlohmann::json 타입, json.hpp 파일)