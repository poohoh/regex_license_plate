#include "lp_analysis.h"

#include <fstream>
#include <iostream>
#include <regex>

LpAnalysis::LpAnalysis() {}

void LpAnalysis::LoadRegexJson(std::string filepath)
{
  std::ifstream instream(filepath);
  if (!instream.is_open())
  {
    std::cerr << "error occurs during opening " << filepath << std::endl;
    return;
  }

  instream >> regex_tree_;
}

std::map<std::string, std::string> LpAnalysis::Match(std::string lp) const
{
  std::string line_break = "\\/";
  std::map<std::string, std::string> ret;
  const nlohmann::json* current;

  // 1. region
  if (!regex_tree_.contains("region"))
  {
    std::cerr << "No region in JSON file." << std::endl;
    ret["region"] = "None";
  }

  std::string lp_region;
  if (lp[0] == 'T')
  {
    if (lp[1] >= '0' && lp[1] <= '9')  // 임시 차량
      lp_region = lp.substr(1, 2);
    else  // 군용 차량
      ret["region"] = "None";
  }
  else  // 일반 차량
    lp_region = lp.substr(0, 2);

  if (ret["region"] != "None")
  {
    current = &regex_tree_["region"];
    for (char c : lp_region)
    {
      if (current->find(std::string(1, c)) == current->end())  // 해당 지역이 없는 경우
      {
        ret["region"] = "None";
        break;
      }
      current = &((*current)[std::string(1, c)]);
    }

    if (current->is_string() && ret["region"] != "None")
      ret["region"] = current->get<std::string>();
  }

  // 2. special_series
  if (!regex_tree_.contains("special_series"))
  {
    std::cerr << "No special_series in JSON file." << std::endl;
    ret["special_series"] = "None";
  }

  current = &regex_tree_["special_series"];
  for (const auto& [regex, name] : current->items())
  {
    std::regex pattern(regex);
    if (std::regex_search(lp, pattern))
    {
      ret["special_series"] = name.get<std::string>();
      break;
    }
  }

  if (ret["special_series"] == "")
    ret["special_series"] = "None";
  

  // 3. foreign country
  if (!regex_tree_.contains("foreign_country"))
  {
    std::cerr << "No foreign_country in JSON file." << std::endl;
    ret["foreign_country"] = "None";
  }

  std::string lp_country;
  std::string foreign_pattern1 = "^\\d{5}(NG|QT|CV|NN)\\d{2,3}$";
  std::string foreign_pattern2 = "^\\d{2}(NG|QT|CV|NN)\\d{5,6}$";
  std::string foreign_pattern3 = "^\\d{5}" + line_break + "(NG|QT|CV|NN)\\d{2,3}$";
  std::string foreign_pattern4 = "^\\d{2}(NG|QT|CV|NN)"+ line_break +"\\d{5,6}$";
  std::regex foreign_regex1(foreign_pattern1);
  std::regex foreign_regex2(foreign_pattern2);
  std::regex foreign_regex3(foreign_pattern3);
  std::regex foreign_regex4(foreign_pattern4);

  if (std::regex_search(lp, foreign_regex1))
    lp_country = lp.substr(2, 3);
  else if (std::regex_search(lp, foreign_regex2))
    lp_country = lp.substr(4, 3);
  else if (std::regex_search(lp, foreign_regex3))
    lp_country = lp.substr(2, 3);
  else if (std::regex_search(lp, foreign_regex4))
    lp_country = lp.substr(5, 3);
  else
    ret["foreign_country"] = "None";  // not foreign vehicle
  
  if (ret["foreign_country"] != "None")
  {
    current = &regex_tree_["foreign_country"];
    for (char c : lp_country)
    {
      if (current->find(std::string(1, c)) == current->end())  // 해당 국가가 없는 경우
      {
        ret["foreign_country"] = "None";
        break;
      }
      current = &((*current)[std::string(1, c)]);
    }

    if (current->is_string() && ret["foreign_country"] != "None")  // 해당 국가가 있는 경우
      ret["foreign_country"] = current->get<std::string>();
  }

  // 4. vehicle type
  if (!regex_tree_.contains("vehicle_type"))
  {
    std::cerr << "No vehicle_type in JSON file." << std::endl;
    ret["vehicle_type"] = "None";
  }

  current = &regex_tree_["vehicle_type"];
  for (const auto& [regex, name] : current->items())
  {
    std::regex pattern(regex);
    if (std::regex_search(lp, pattern))
    {
      ret["vehicle_type"] = name.get<std::string>();
      break;
    }
  }

  if (ret["vehicle_type"] == "")
    ret["vehicle_type"] = "None";

  // 5. military unit
  if (!regex_tree_.contains("military_unit"))
  {
    std::cerr << "No military_unit in JSON file." << std::endl;
    ret["military_unit"] = "None";
  }

  std::string military_unit = lp.substr(0, 2);

  current = &regex_tree_["military_unit"];
  for (char c : military_unit)
  {
    if (current->find(std::string(1, c)) == current->end())  // 해당 소속이 없는 경우
    {
      ret["military_unit"] = "None";
      break;
    }
    current = &((*current)[std::string(1, c)]);
  }

  if (current->is_string() && ret["military_unit"] != "None")
    ret["military_unit"] = current->get<std::string>();

  return ret;
}