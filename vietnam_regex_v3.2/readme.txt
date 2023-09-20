* 수정 사항 *

1. foreign_vehicle_type, military vehicle type 카테고리를 vehicle_type 카테고리로 합침

2. vehicle_type 카테고리에 vietnam_car, vietnam_motorcycle 추가
    - 일반 베트남 자동차와 오토바이 구분
    - vietnam_car: 소유주가 베트남인 차량, 베트남산 차량이라는 의미가 아님.

3. Đ 문자 주석처리
    - 실행에는 문제가 없었으나, 입력 문자열에 Đ 문자를 사용하면 매치되지 않는 문제 발생
    - special series의 MĐ(전기 오토바이)와 TĐ(시험 운행 차량)도 주석 처리