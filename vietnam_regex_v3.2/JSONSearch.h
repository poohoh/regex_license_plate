#include <string>
#include "json.hpp"

// 카테고리와 해당 값의 결과를 저장할 구조체
struct result_struct
{
    std::string category;
    std::string value;

    result_struct(const std::string &cat) : category(cat), value("None") {}
};

class JSONSearch
{
public:
    JSONSearch(const std::string &file_path);
    result_struct search_region(const std::string &input_string) const;
    result_struct search_special_series(const std::string &input_string) const;
    result_struct search_foreign_country(const std::string &input_string) const;
    result_struct search_vehicle_type(const std::string &input_string) const;
    result_struct search_military_unit(const std::string &input_string) const;

private:
    nlohmann::json json_data;
};