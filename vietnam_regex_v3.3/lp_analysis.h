#pragma once

#include "json.hpp"

class LpAnalysis
{
 public:
  LpAnalysis(LpAnalysis const&) = delete;
  void operator=(LpAnalysis const&) = delete;

  static LpAnalysis& GetInstance()
  {
    static LpAnalysis lp_analysis;
    return lp_analysis;
  }

  void LoadRegexJson(std::string filepath);
  std::map<std::string, std::string> Match(std::string lp) const;

 private:
  LpAnalysis();

  nlohmann::json regex_tree_;
};