import re


# std::wstring kor_region =
#     L"\uC11C\uC6B8|\uBD80\uC0B0|\uB300\uAD6C|\uC778\uCC9C|\uAD11\uC8FC|"
#     L"\uB300\uC804|\uC6B8\uC0B0|\uC138\uC885|\uACBD\uAE30|\uAC15\uC6D0|"
#     L"\uCDA9\uBD81|\uCDA9\uB0A8|\uC804\uBD81|\uC804\uB0A8|\uACBD\uBD81|"
#     L"\uACBD\uB0A8|\uC81C\uC8FC";
# std::wstring kor_middle =
#     L"\uAC00|\uB098|\uB2E4|\uB77C|\uB9C8|\uAC70|\uB108|\uB354|\uB7EC|"
#     "\uBA38|\uBC84|\uC11C|\uC5B4|\uC800|\uACE0|\uB178|\uB3C4|\uB85C|"
#     "\uBAA8|\uBCF4|\uC18C|\uC624|\uC870|\uAD6C|\uB204|\uB450|\uB8E8|"
#     "\uBB34|\uBD80|\uC218|\uC6B0|\uC8FC|\uBC14|\uC0AC|\uC544|\uC790|"
#     "\uD5C8|\uD558|\uD638|\uBC30";
# std::wstring viet_middle =
#     L"\u0041|\u0042|\u0043|\u0044|\u0110|\u0045|\u0046|\u0047|\u0048|"
#     "\u004B|\u004C|\u004D|\u004E|\u0050|\u0051|\u0052|"
#     "\u0053|\u0054|\u0055|\u0056|\u0058|\u0059|\u005A|\u004C\u0044";
# std::wstring viet_middle_2 = L"\u004E\u0047|\u004E\u004E";

# std::wregex kor_patt(L"(^(\\d{2}|\\d{3})(" + kor_middle + L")\\d{4}$)|(^(" +
#                      kor_region + L")\\d{2}(" + kor_middle + L")\\d{4}$)");
# std::wregex viet_patt_1(L"(^\\d{2}(" + viet_middle + L")(\\d{5})$)");
# std::wregex viet_patt_2(L"(^\\d{5}(" + viet_middle_2 + L")(\\d{2})$)");



alphabet = r"(A|B|C|D|\u0110|E|F|G|H|K|L|M|N|P|Q|R|S|T|U|V|X|Y|Z)"
alphabet_or_number = r"(A|B|C|D|\u0110|E|F|G|H|K|L|M|N|P|Q|R|S|T|U|V|X|Y|Z|0|1|2|3|4|5|6|7|8|9)"


# 법률 58호에 따른 베트남 번호판 규칙


############################ 1. 베트남 차량 번호판 ############################
# 형식: 12A-345.67
# 1) 앞의 두 자리: 등록 장소 표시 (도/시)
# 2) 한 자리: 등록 번호판 종류
# 3) 다음 다섯 자리: 차량 번호

vietnam_car = r"\d{2}" + alphabet + r"\d{5}"


############################ 2. 베트남 오토바이 번호판 ############################
# 형식: 12-A3-456.78
# 1) 앞의 두 자리: 등록 장소 표시 (도/시)
# 2) 한 자리: 등록 번호판 종류
# 3) 다음 다섯 자리: 차량 번호

vietnam_motorcycle = r"\d{2}" + alphabet + alphabet_or_number + r"\d{5}"


############################ 3. 트랙터, 전동 오토바이 번호판 ############################
# 형식: 12-AB3-456.78
# 1) 앞의 두 자리: 등록 장소 표시 (도/시)
# 2) 두 자리: 등록 series
# 3) 다음 다섯 자리: 차량 번호

tractor_electric_motorcycle = r"\d{2}" + alphabet + alphabet + r"\d{6}"



############################ 4. 외국 자동차 번호판 ############################
# 처음 두 자리: 등록 장소 표시 (도/시)
# 다음 세 자리: 국가 코드(등록자 국적)
# 두 글자 코드: NN, NG, CV, QT  -->  표지판에 이 두 글자를 가로지르는 빨간색 줄이 그어져 있는 경우 각 표지판의 상위 수준을 나타냄.(어떠한 상황에도 무단 침입 금지)
# 마지막 차량번호 두 자리(오토바이의 경우 세자리)


# 4.1. 외교 대표 기관, 영사 기관 및 해당 기관의 외교 ID를 가진 구성원의 차량(NG)
# 형식: XX-XXX-NG-XX, XX-NG-XXX-XX
# 위 표현식에서 가운데 세 자리 숫자를 각 나라별로 적용해야 함.

# 4.1.1. 대사 및 총영사관 차량
# 형식: XX-XXX-NG-01, XX-NG-XXX-01
foreign_affairs_ambassador = r"\d{5}NG01|\d{2}NG\d{3}01"

# 4.1.2. 부대사 및 총영사관 차량
# 형식: XX-XXX-NG-02, XX-NG-XXX-02
foreign_affairs_vice_ambassador = r"\d{5}NG02|\d{2}NG\d{3}02"

# 4.1.3. 그 외 해당 기관의 외교 신분증을 소지한 외국인 직원의 차량
# 형식: XX-XXX-NG-XX, XX-NG-XXX-XX
foreign_affairs_etc = r"\d{5}NG\d{2}|\d{2}NG\d{5}"


# !!!!!!! 하노이에 주재하는 외교관은 80-123-NG-45, 80-NG-123-45 형식
# !!!!!!! 하노이 외부에 있는 외교 공관은 하노이를 위해 예약된 80 대신 표준 지역 코드를 받음
# !!!!!!! 출처: 위키피디아 영어 버전



# 4.2. 국제 조직의 대표 기관 및 해당 조직의 외교 ID를 가진 구성원의 차량(QT)
# 형식: XX-XXX-QT-XX, XX-QT-XXX-XX

# 4.2.1. 국제 조직의 대표 차량
# 형식: XX-XXX-QT-01, XX-QT-XXX-01
international_organization_ambassador = r"\d{5}QT01|\d{2}QT\d{3}01"

# 4.2.2. 국제 조직 차량
# 형식: XX-XXX-QT-XX, XX-QT-XXX-XX
international_organization_etc = r"\d{5}QT\d{2}|\d{2}QT\d{5}"



# 4.3. 외교 대표 기관, 영사 기관, 국제 조직의 행정 및 기술 직원이 소지한 공무 ID를 가진 차량(CV)
# 형식: XX-XXX-CV-XX, XX-CV-XXX-XX
administrative_technical_staff = r"\d{5}CV\d{2}|\d{2}CV\d{5}"



# 4.4. 다른 외국 조직, 대표 사무소, 개인의 차량(NN)
# 형식: XX-XXX-NN-XX, XX-NN-XXX-XX
other_foreign = r"\d{5}NN\d{2}|\d{2}NN\d{5}"




############################ 5. 외국인 오토바이 번호판 ############################
# 형식: XX-XXX-NN-XXX, XX-NN-XXX-XXX
foreign_motorcycle = r"\d{5}NN\d{3}|\d{2}NN\d{6}"



############################ 6. 합작 투자, 프로젝트, 군사 기업 차량의 자동차 및 오토바이 번호판 ############################
# 형식: 12AB-345.67
joint_venture_project_military = r"\d{2}" + alphabet + alphabet + r"\d{3}\d{2}|\d{2}\d{3}" + alphabet + alphabet + r"\d{2}"

############################ 7. 정부 규정에 따른 경제-상업특구 차량번호판 ############################
# 형식: 12AB-345.67
# 2개의 등록 지역 기호, 2개의 경제*상업 구역의 지명에 따른 등록 시리즈, 5개의 등록 순서
economic_commercial_zone = r"\d{2}" + alphabet + alphabet + r"\d{5}"

############################ 8. 임시등록번호판에 관한 사항 ############################
# 형식: T12-345.67
# 임시 등록의 T, 2개의 등록 장소 기호, 5개의 등록 순서
temporary_registration = r"T\d{7}"

############################ 9. 정치, 회의, 스포츠를 위한 임시 수단 ############################
# 형식: 12-345.67
# 로고, 2개의 등록 지역 기호, 5개의 등록 순서
temporary_means = r"\d{7}"

############################ 10. 자동차 및 오토바이의 번호판 변경 및 재발급 시 4자리 번호판에 관한 규정 ############################
# 형식: 12A-3456, 12-A3-4567
# 2개의 등록 지역 기호, 1개의 등록 시리즈, 4개의 등록 순서
change_reissue = r"\d{2}" + alphabet + r"\d{4}|\d{2}" + alphabet + r"\d{5}"























# pattern = r"\d{2,3}-[A-Z]{1,2}-\d{4,5}"

# test_strings = ["51A-12345", "123B-4567", "12-AB-1234", "ABC-12345", "123-BG-23459", "123a-2354"]
# match_results = [re.match(pattern, test_string) for test_string in test_strings]
# match_results_bool = [bool(match_result) for match_result in match_results]

# print(match_results_bool)



############################ 1. 베트남 차량 번호판 ############################
vietnam_car = r"\d{2}" + alphabet + r"\d{5}"

############################ 2. 베트남 오토바이 번호판 ############################
vietnam_motorcycle = r"\d{2}[A-Z][A-Z0-9]\d{5}"

############################ 3. 트랙터, 전동 오토바이 번호판 ############################
tractor_electric_motorcycle = r"\d{2}" + alphabet + alphabet + r"\d{6}"

############################ 4. 외국 자동차 번호판 ############################
# 4.1.1. 대사 및 총영사관 차량
foreign_affairs_ambassador = r"\d{5}NG01|\d{2}NG\d{3}01"

# 4.1.2. 부대사 및 총영사관 차량
foreign_affairs_vice_ambassador = r"\d{5}NG02|\d{2}NG\d{3}02"

# 4.1.3. 그 외 해당 기관의 외교 신분증을 소지한 외국인 직원의 차량
foreign_affairs_etc = r"\d{5}NG\d{2}|\d{2}NG\d{5}"

# 4.2.1. 국제 조직의 대표 차량
international_organization_ambassador = r"\d{5}QT01|\d{2}QT\d{3}01"

# 4.2.2. 국제 조직 차량
international_organization_etc = r"\d{5}QT\d{2}|\d{2}QT\d{5}"

# 4.3. 외교 대표 기관, 영사 기관, 국제 조직의 행정 및 기술 직원이 소지한 공무 ID를 가진 차량(CV)
administrative_technical_staff = r"\d{5}CV\d{2}|\d{2}CV\d{5}"

# 4.4. 다른 외국 조직, 대표 사무소, 개인의 차량(NN)
other_foreign = r"\d{5}NN\d{2}|\d{2}NN\d{5}"

############################ 5. 외국인 오토바이 번호판 ############################
foreign_motorcycle = r"\d{5}NN\d{3}|\d{2}NN\d{6}"

############################ 6. 합작 투자, 프로젝트, 군사 기업 차량의 자동차 및 오토바이 번호판 ############################
joint_venture_project_military = r"\d{2}" + alphabet + alphabet + r"\d{3}\d{2}|\d{2}\d{3}" + alphabet + alphabet + r"\d{2}"

############################ 7. 정부 규정에 따른 경제-상업특구 차량번호판 ############################
# 2개의 등록 지역 기호, 2개의 경제*상업 구역의 지명에 따른 등록 시리즈, 5개의 등록 순서
economic_commercial_zone = r"\d{2}" + alphabet + alphabet + r"\d{5}"

############################ 8. 임시등록번호판에 관한 사항 ############################
temporary_registration = r"T\d{7}"

############################ 9. 정치, 회의, 스포츠를 위한 임시 수단 ############################
temporary_means = r"\d{7}"

############################ 10. 자동차 및 오토바이의 번호판 변경 및 재발급 시 4자리 번호판에 관한 규정 ############################
change_reissue = r"\d{2}" + alphabet + r"\d{4}|\d{2}" + alphabet + r"\d{5}"