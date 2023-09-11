foreign_motorcycle = r"\d{5}NN\d{3}|\d{2}NN\d{6}"



#################### 오토바이 시리즈 구분 ####################
# 외교 대표 기관, 영사 기관 및 해당 기관의 외교 ID를 가진 구성원의 오토바이(NG)
affairs_staff_motorcycle = r"^\d{5}NG\d{3}$|^\d{2}NG\d{6}$"

# 국제 조직의 대표 기관 및 해당 조직의 외교 ID를 가진 구성원의 오토바이(QT)
international_organization_staff_motorcycle = r"^\d{5}QT\d{3}$|^\d{2}QT\d{6}$"

# 외교 대표 기관, 영사 기관, 국제 조직의 행정 및 기술 직원이 소지한 공무 ID를 가진 구성원의 오토바이(CV)
administrative_technical_staff_motorcycle = r"^\d{5}CV\d{3}$|^\d{2}CV\d{6}$"

# 다른 외국 조직, 대표 사무소, 개인의 오토바이(NN)
other_foreign_motorcycle = r"^\d{5}NN\d{3}$|^\d{2}NN\d{6}$"

# json
foreign_motorcycle_type = {
    affairs_staff_motorcycle : "affairs staff motorcycle",
    international_organization_staff_motorcycle : "international organization staff motorcycle",
    administrative_technical_staff_motorcycle : "administrative technical staff motorcycle",
    other_foreign_motorcycle : "foreign motorcycle"
}


import json

file_path = "./foreign_motorcycle_type.json"
with open(file_path, "w", encoding="utf-8") as json_file:
    json.dump(foreign_motorcycle_type, json_file, ensure_ascii=False, indent=4)




# # 이 국가 구분은 사용하지 않음. foreign country의 국가 구분만 사용
# ################# 국가 구분 #################
# foreign_motorcycle_Austria = r"\d{2}(001|002|003|004|005)NN\d{3}|\d{2}NN(001|002|003|004|005)\d{3}"
# foreign_motorcycle_Albania = r"\d{2}(006|007|008|009|010)NN\d{3}|\d{2}NN(006|007|008|009|010)\d{3}"
# foreign_motorcycle_UK_Northern_Ireland = r"\d{2}(011|012|013|014|015)NN\d{3}|\d{2}NN(011|012|013|014|015)\d{3}"
# foreign_motorcycle_Egypt = r"\d{2}(016|017|018|019|020)NN\d{3}|\d{2}NN(016|017|018|019|020)\d{3}"
# foreign_motorcycle_Azerbaijan = r"\d{2}(021|022|023|024|025)NN\d{3}|\d{2}NN(021|022|023|024|025)\d{3}"
# foreign_motorcycle_India = r"\d{2}(026|027|028|029|030)NN\d{3}|\d{2}NN(026|027|028|029|030)\d{3}"
# foreign_motorcycle_Angola = r"\d{2}(031|032|033|034|035)NN\d{3}|\d{2}NN(031|032|033|034|035)\d{3}"
# foreign_motorcycle_Afghanistan = r"\d{2}(036|037|038|039|040)NN\d{3}|\d{2}NN(036|037|038|039|040)\d{3}"
# foreign_motorcycle_Algeria = r"\d{2}(041|042|043|044|045)NN\d{3}|\d{2}NN(041|042|043|044|045)\d{3}"
# foreign_motorcycle_Argentina = r"\d{2}(046|047|048|049|050)NN\d{3}|\d{2}NN(046|047|048|049|050)\d{3}"
# foreign_motorcycle_Armenia = r"\d{2}(051|052|053|054|055)NN\d{3}|\d{2}NN(051|052|053|054|055)\d{3}"
# foreign_motorcycle_Iceland = r"\d{2}(056|057|058|059|060)NN\d{3}|\d{2}NN(056|057|058|059|060)\d{3}"
# foreing_motorcycle_Belgium = r"\d{2}(061|062|063|064|065)NN\d{3}|\d{2}NN(061|062|063|064|065)\d{3}"
# foreign_motorcycle_Poland = r"\d{2}(066|067|068|069|070)NN\d{3}|\d{2}NN(066|067|068|069|070)\d{3}"
# foreign_motorcycle_Portugal = r"\d{2}(071|072|073|074|075)NN\d{3}|\d{2}NN(071|072|073|074|075)\d{3}"
# foreign_motorcycle_Bulgaria = r"\d{2}(076|077|078|079|080)NN\d{3}|\d{2}NN(076|077|078|079|080)\d{3}"
# foreign_motorcycle_Burkina_Faso = r"\d{2}(081|082|083|084|085)NN\d{3}|\d{2}NN(081|082|083|084|085)\d{3}"
# foreign_motorcycle_Brazil = r"\d{2}(086|087|088|089|090)NN\d{3}|\d{2}NN(086|087|088|089|090)\d{3}"
# foreign_motorcycle_Bangladesh = r"\d{2}(091|092|093|094|095)NN\d{3}|\d{2}NN(091|092|093|094|095)\d{3}"
# foreign_motorcycle_Belarus = r"\d{2}(096|097|098|099|100)NN\d{3}|\d{2}NN(096|097|098|099|100)\d{3}"
# foreign_motorcycle_Bolivia = r"\d{2}(101|102|103|104|105)NN\d{3}|\d{2}NN(101|102|103|104|105)\d{3}"
# foreign_motorcycle_Benin = r"\d{2}(106|107|108|109|110)NN\d{3}|\d{2}NN(106|107|108|109|110)\d{3}"
# foreign_motorcycle_Brunei = r"\d{2}(111|112|113|114|115)NN\d{3}|\d{2}NN(111|112|113|114|115)\d{3}"
# foreign_motorcycle_Burundi = r"\d{2}(116|117|118|119|120)NN\d{3}|\d{2}NN(116|117|118|119|120)\d{3}"
# foreign_motorcycle_Cuba = r"\d{2}(121|122|123|124|125)NN\d{3}|\d{2}NN(121|122|123|124|125)\d{3}"
# foreign_motorcycle_Ivory_Coast = r"\d{2}(126|127|128|129|130)NN\d{3}|\d{2}NN(126|127|128|129|130)\d{3}"
# foreign_motorcycle_Congo_Brazzaville = r"\d{2}(131|132|133|134|135)NN\d{3}|\d{2}NN(131|132|133|134|135)\d{3}"
# foreign_motorcycle_Congo_Kinshasa = r"\d{2}(136|137|138|139|140)NN\d{3}|\d{2}NN(136|137|138|139|140)\d{3}"
# foreign_motorcycle_Chile = r"\d{2}(141|142|143|144|145)NN\d{3}|\d{2}NN(141|142|143|144|145)\d{3}"
# foreign_motorcycle_Colombia = r"\d{2}(146|147|148|149|150)NN\d{3}|\d{2}NN(146|147|148|149|150)\d{3}"
# foreign_motorcycle_Cameroon = r"\d{2}(151|152|153|154|155)NN\d{3}|\d{2}NN(151|152|153|154|155)\d{3}"
# foreign_motorcycle_Canada = r"\d{2}(156|157|158|159|160)NN\d{3}|\d{2}NN(156|157|158|159|160)\d{3}"
# foreign_motorcycle_Kuwait = r"\d{2}(161|162|163|164|165)NN\d{3}|\d{2}NN(161|162|163|164|165)\d{3}"
# foreign_motorcycle_Cambodia = r"\d{2}(166|167|168|169|170)NN\d{3}|\d{2}NN(166|167|168|169|170)\d{3}"
# foreign_motorcycle_Kyrgyzstan = r"\d{2}(171|172|173|174|175)NN\d{3}|\d{2}NN(171|172|173|174|175)\d{3}"
# foreign_motorcycle_Qatar = r"\d{2}(176|177|178|179|180)NN\d{3}|\d{2}NN(176|177|178|179|180)\d{3}"
# foreign_motorcycle_Cape_Verde = r"\d{2}(181|182|183|184|185)NN\d{3}|\d{2}NN(181|182|183|184|185)\d{3}"
# foreign_motorcycle_Costa_Rica = r"\d{2}(186|187|188|189|190)NN\d{3}|\d{2}NN(186|187|188|189|190)\d{3}"
# foreign_motorcycle_Germany = r"\d{2}(191|192|193|194|195)NN\d{3}|\d{2}NN(191|192|193|194|195)\d{3}"
# foreign_motorcycle_Zambia = r"\d{2}(196|197|198|199|200)NN\d{3}|\d{2}NN(196|197|198|199|200)\d{3}"
# foreign_motorcycle_Zimbabwe = r"\d{2}(201|202|203|204|205)NN\d{3}|\d{2}NN(201|202|203|204|205)\d{3}"
# foreign_motorcycle_Denmark = r"\d{2}(206|207|208|209|210)NN\d{3}|\d{2}NN(206|207|208|209|210)\d{3}"
# foreign_motorcycle_Ecuador = r"\d{2}(211|212|213|214|215)NN\d{3}|\d{2}NN(211|212|213|214|215)\d{3}"
# foreign_motorcycle_Eritrea = r"\d{2}(216|217|218|219|220)NN\d{3}|\d{2}NN(216|217|218|219|220)\d{3}"
# foreign_motorcycle_Ethiopia = r"\d{2}(221|222|223|224|225)NN\d{3}|\d{2}NN(221|222|223|224|225)\d{3}"
# foreign_motorcycle_Estonia = r"\d{2}(226|227|228|229|230)NN\d{3}|\d{2}NN(226|227|228|229|230)\d{3}"
# foreign_motorcycle_Guyana = r"\d{2}(231|232|233|234|235)NN\d{3}|\d{2}NN(231|232|233|234|235)\d{3}"
# foreign_motorcycle_Gabon = r"\d{2}(236|237|238|239|240)NN\d{3}|\d{2}NN(236|237|238|239|240)\d{3}"
# foreign_motorcycle_Gambia = r"\d{2}(241|242|243|244|245)NN\d{3}|\d{2}NN(241|242|243|244|245)\d{3}"
# foreign_motorcycle_Djibouti = r"\d{2}(246|247|248|249|250)NN\d{3}|\d{2}NN(246|247|248|249|250)\d{3}"
# foreign_motorcycle_Georgia = r"\d{2}(251|252|253|254|255)NN\d{3}|\d{2}NN(251|252|253|254|255)\d{3}"
# foreign_motorcycle_Jordan = r"\d{2}(256|257|258|259|260)NN\d{3}|\d{2}NN(256|257|258|259|260)\d{3}"
# foreign_motorcycle_Guinea = r"\d{2}(261|262|263|264|265)NN\d{3}|\d{2}NN(261|262|263|264|265)\d{3}"
# foreign_motorcycle_Ghana = r"\d{2}(266|267|268|269|270)NN\d{3}|\d{2}NN(266|267|268|269|270)\d{3}"
# foreign_motorcycle_Guinea_Bissau = r"\d{2}(271|272|273|274|275)NN\d{3}|\d{2}NN(271|272|273|274|275)\d{3}"
# foreign_motorcycle_Grenada = r"\d{2}(276|277|278|279|280)NN\d{3}|\d{2}NN(276|277|278|279|280)\d{3}"
# foreign_motorcycle_Equatorial_Guinea = r"\d{2}(281|282|283|284|285)NN\d{3}|\d{2}NN(281|282|283|284|285)\d{3}"
# foreign_motorcycle_Guatemala = r"\d{2}(286|287|288|289|290)NN\d{3}|\d{2}NN(286|287|288|289|290)\d{3}"
# foreign_motorcycle_Hungary = r"\d{2}(291|292|293|294|295)NN\d{3}|\d{2}NN(291|292|293|294|295)\d{3}"
# foreign_motorcycle_United_States = r"\d{2}(296|297|298|299|300)NN\d{3}|\d{2}NN(296|297|298|299|300)\d{3}"
# foreign_motorcycle_Netherlands = r"\d{2}(301|302|303|304|305)NN\d{3}|\d{2}NN(301|302|303|304|305)\d{3}"
# foreign_motorcycle_Greece = r"\d{2}(306|307|308|309|310)NN\d{3}|\d{2}NN(306|307|308|309|310)\d{3}"
# foreign_motorcycle_Jamaica = r"\d{2}(311|312|313|314|315)NN\d{3}|\d{2}NN(311|312|313|314|315)\d{3}"
# foreign_motorcycle_Indonesia = r"\d{2}(316|317|318|319|320)NN\d{3}|\d{2}NN(316|317|318|319|320)\d{3}"
# foreign_motorcycle_Iran = r"\d{2}(321|322|323|324|325)NN\d{3}|\d{2}NN(321|322|323|324|325)\d{3}"
# foreign_motorcycle_Iraq = r"\d{2}(326|327|328|329|330)NN\d{3}|\d{2}NN(326|327|328|329|330)\d{3}"
# foreign_motorcycle_Italy = r"\d{2}(331|332|333|334|335)NN\d{3}|\d{2}NN(331|332|333|334|335)\d{3}"
# foreign_motorcycle_Israel = r"\d{2}(336|337|338|339|340)NN\d{3}|\d{2}NN(336|337|338|339|340)\d{3}"
# foreign_motorcycle_Kazakhstan = r"\d{2}(341|342|343|344|345)NN\d{3}|\d{2}NN(341|342|343|344|345)\d{3}"
# foreign_motorcycle_Laos = r"\d{2}(346|347|348|349|350)NN\d{3}|\d{2}NN(346|347|348|349|350)\d{3}"
# foreign_motorcycle_Lebanon = r"\d{2}(351|352|353|354|355)NN\d{3}|\d{2}NN(351|352|353|354|355)\d{3}"
# foreign_motorcycle_Libya = r"\d{2}(356|357|358|359|360)NN\d{3}|\d{2}NN(356|357|358|359|360)\d{3}"
# foreign_motorcycle_Luxembourg = r"\d{2}(361|362|363|364|365)NN\d{3}|\d{2}NN(361|362|363|364|365)\d{3}"
# foreign_motorcycle_Lithuania = r"\d{2}(366|367|368|369|370)NN\d{3}|\d{2}NN(366|367|368|369|370)\d{3}"
# foreign_motorcycle_Latvia = r"\d{2}(371|372|373|374|375)NN\d{3}|\d{2}NN(371|372|373|374|375)\d{3}"
# foreign_motorcycle_Myanmar = r"\d{2}(376|377|378|379|380)NN\d{3}|\d{2}NN(376|377|378|379|380)\d{3}"
# foreign_motorcycle_Mongolia = r"\d{2}(381|382|383|384|385)NN\d{3}|\d{2}NN(381|382|383|384|385)\d{3}"
# foreign_motorcycle_Mozambique = r"\d{2}(386|387|388|389|390)NN\d{3}|\d{2}NN(386|387|388|389|390)\d{3}"
# foreign_motorcycle_Madagascar = r"\d{2}(391|392|393|394|395)NN\d{3}|\d{2}NN(391|392|393|394|395)\d{3}"
# foreign_motorcycle_Moldova = r"\d{2}(396|397|398|399|400)NN\d{3}|\d{2}NN(396|397|398|399|400)\d{3}"
# foreign_motorcycle_Maldives = r"\d{2}(401|402|403|404|405)NN\d{3}|\d{2}NN(401|402|403|404|405)\d{3}"
# foreign_motorcycle_Mexico = r"\d{2}(406|407|408|409|410)NN\d{3}|\d{2}NN(406|407|408|409|410)\d{3}"
# foreign_motorcycle_Mali = r"\d{2}(411|412|413|414|415)NN\d{3}|\d{2}NN(411|412|413|414|415)\d{3}"
# foreign_motorcycle_Malaysia = r"\d{2}(416|417|418|419|420)NN\d{3}|\d{2}NN(416|417|418|419|420)\d{3}"
# foreign_motorcycle_Morocco = r"\d{2}(421|422|423|424|425)NN\d{3}|\d{2}NN(421|422|423|424|425)\d{3}"
# foreign_motorcycle_Mauritania = r"\d{2}(426|427|428|429|430)NN\d{3}|\d{2}NN(426|427|428|429|430)\d{3}"
# foreign_motorcycle_Malta = r"\d{2}(431|432|433|434|435)NN\d{3}|\d{2}NN(431|432|433|434|435)\d{3}"
# foreign_motorcycle_Vatican = r"\d{2}(436|437|438|439|440|843)NN\d{3}|\d{2}NN(436|437|438|439|440|843)\d{3}"
# foreign_motorcycle_Russia = r"\d{2}(441|442|443|444|445)NN\d{3}|\d{2}NN(441|442|443|444|445)\d{3}"
# foreign_motorcycle_Japan = r"\d{2}(446|447|448|449|450)NN\d{3}|\d{2}NN(446|447|448|449|450)\d{3}"
# foreign_motorcycle_Nicaragua = r"\d{2}(451|452|453|454|455)NN\d{3}|\d{2}NN(451|452|453|454|455)\d{3}"
# foreign_motorcycle_New_Zealand = r"\d{2}(456|457|458|459|460)NN\d{3}|\d{2}NN(456|457|458|459|460)\d{3}"
# foreign_motorcycle_Niger = r"\d{2}(461|462|463|464|465)NN\d{3}|\d{2}NN(461|462|463|464|465)\d{3}"
# foreign_motorcycle_Nigeria = r"\d{2}(466|467|468|469|470)NN\d{3}|\d{2}NN(466|467|468|469|470)\d{3}"
# foreign_motorcycle_Namibia = r"\d{2}(471|472|473|474|475)NN\d{3}|\d{2}NN(471|472|473|474|475)\d{3}"
# foreign_motorcycle_Nepal = r"\d{2}(476|477|478|479|480)NN\d{3}|\d{2}NN(476|477|478|479|480)\d{3}"
# foreign_motorcycle_South_Africa = r"\d{2}(481|482|483|484|485)NN\d{3}|\d{2}NN(481|482|483|484|485)\d{3}"
# foreign_motorcycle_Yugoslavia = r"\d{2}(486|487|488|489|490)NN\d{3}|\d{2}NN(486|487|488|489|490)\d{3}"
# foreign_motorcycle_Norway = r"\d{2}(491|492|493|494|495)NN\d{3}|\d{2}NN(491|492|493|494|495)\d{3}"
# foreign_motorcycle_Oman = r"\d{2}(496|497|498|499|500)NN\d{3}|\d{2}NN(496|497|498|499|500)\d{3}"
# foreign_motorcycle_Australia = r"\d{2}(501|502|503|504|505)NN\d{3}|\d{2}NN(501|502|503|504|505)\d{3}"
# foreign_motorcycle_France = r"\d{2}(506|507|508|509|510)NN\d{3}|\d{2}NN(506|507|508|509|510)\d{3}"
# foreign_motorcycle_Fiji = r"\d{2}(511|512|513|514|515)NN\d{3}|\d{2}NN(511|512|513|514|515)\d{3}"
# foreign_motorcycle_Pakistan = r"\d{2}(516|517|518|519|520)NN\d{3}|\d{2}NN(516|517|518|519|520)\d{3}"
# foreign_motorcycle_Finland = r"\d{2}(521|522|523|524|525)NN\d{3}|\d{2}NN(521|522|523|524|525)\d{3}"
# foreign_motorcycle_Philippines = r"\d{2}(526|527|528|529|530)NN\d{3}|\d{2}NN(526|527|528|529|530)\d{3}"
# foreign_motorcycle_Palestine = r"\d{2}(531|532|533|534|535)NN\d{3}|\d{2}NN(531|532|533|534|535)\d{3}"
# foreign_motorcycle_Panama = r"\d{2}(536|537|538|539|540)NN\d{3}|\d{2}NN(536|537|538|539|540)\d{3}"
# foreign_motorcycle_Papua_New_Guinea = r"\d{2}(541|542|543|544|545)NN\d{3}|\d{2}NN(541|542|543|544|545)\d{3}"
# foreign_motorcycle_International_Organization = r"\d{2}(546|547|548|549|550)NN\d{3}|\d{2}NN(546|547|548|549|550)\d{3}"
# foreign_motorcycle_Rwanda = r"\d{2}(551|552|553|554|555)NN\d{3}|\d{2}NN(551|552|553|554|555)\d{3}"
# foreign_motorcycle_Romania = r"\d{2}(556|557|558|559|560)NN\d{3}|\d{2}NN(556|557|558|559|560)\d{3}"
# foreign_motorcycle_Chad = r"\d{2}(561|562|563|564|565)NN\d{3}|\d{2}NN(561|562|563|564|565)\d{3}"
# foreign_motorcycle_Czech_Republic = r"\d{2}(566|567|568|569|570)NN\d{3}|\d{2}NN(566|567|568|569|570)\d{3}"
# foreign_motorcycle_Cyprus = r"\d{2}(571|572|573|574|575)NN\d{3}|\d{2}NN(571|572|573|574|575)\d{3}"
# foreign_motorcycle_Spain = r"\d{2}(576|577|578|579|580)NN\d{3}|\d{2}NN(576|577|578|579|580)\d{3}"
# foreign_motorcycle_Sweden = r"\d{2}(581|582|583|584|585)NN\d{3}|\d{2}NN(581|582|583|584|585)\d{3}"
# foreign_motorcycle_Tanzania = r"\d{2}(586|587|588|589|590)NN\d{3}|\d{2}NN(586|587|588|589|590)\d{3}"
# foreign_motorcycle_Togo = r"\d{2}(591|592|593|594|595)NN\d{3}|\d{2}NN(591|592|593|594|595)\d{3}"
# foreign_motorcycle_Tajikistan = r"\d{2}(596|597|598|599|600)NN\d{3}|\d{2}NN(596|597|598|599|600)\d{3}"
# foreign_motorcycle_China = r"\d{2}(601|602|603|604|605)NN\d{3}|\d{2}NN(601|602|603|604|605)\d{3}"
# foreign_motorcycle_Thailand = r"\d{2}(606|607|608|609|610)NN\d{3}|\d{2}NN(606|607|608|609|610)\d{3}"
# foreign_motorcycle_Turkmenistan = r"\d{2}(611|612|613|614|615)NN\d{3}|\d{2}NN(611|612|613|614|615)\d{3}"
# foreign_motorcycle_Tunisia = r"\d{2}(616|617|618|619|620)NN\d{3}|\d{2}NN(616|617|618|619|620)\d{3}"
# foreign_motorcycle_Turkey = r"\d{2}(621|622|623|624|625)NN\d{3}|\d{2}NN(621|622|623|624|625)\d{3}"
# foreign_motorcycle_Switzerland = r"\d{2}(626|627|628|629|630)NN\d{3}|\d{2}NN(626|627|628|629|630)\d{3}"
# foreign_motorcycle_North_Korea = r"\d{2}(631|632|633|634|635)NN\d{3}|\d{2}NN(631|632|633|634|635)\d{3}"
# foreign_motorcycle_South_Korea = r"\d{2}(636|637|638|639|640)NN\d{3}|\d{2}NN(636|637|638|639|640)\d{3}"
# foreign_motorcycle_United_Arab_Emirates = r"\d{2}(641|642|643|644|645)NN\d{3}|\d{2}NN(641|642|643|644|645)\d{3}"
# foreign_motorcycle_Samoa = r"\d{2}(646|647|648|649|650)NN\d{3}|\d{2}NN(646|647|648|649|650)\d{3}"
# foreign_motorcycle_Ukraine = r"\d{2}(651|652|653|654|655)NN\d{3}|\d{2}NN(651|652|653|654|655)\d{3}"
# foreign_motorcycle_Uzbekistan = r"\d{2}(656|657|658|659|660)NN\d{3}|\d{2}NN(656|657|658|659|660)\d{3}"
# foreign_motorcycle_Uganda = r"\d{2}(661|662|663|664|665)NN\d{3}|\d{2}NN(661|662|663|664|665)\d{3}"
# foreign_motorcycle_Uruguay = r"\d{2}(666|667|668|669|670)NN\d{3}|\d{2}NN(666|667|668|669|670)\d{3}"
# foreign_motorcycle_Vanuatu = r"\d{2}(671|672|673|674|675)NN\d{3}|\d{2}NN(671|672|673|674|675)\d{3}"
# foreign_motorcycle_Venezuela = r"\d{2}(676|677|678|679|680)NN\d{3}|\d{2}NN(676|677|678|679|680)\d{3}"
# foreign_motorcycle_Sudan = r"\d{2}(681|682|683|684|685)NN\d{3}|\d{2}NN(681|682|683|684|685)\d{3}"
# foreign_motorcycle_Sierra_Leone = r"\d{2}(686|687|688|689|690)NN\d{3}|\d{2}NN(686|687|688|689|690)\d{3}"
# foreign_motorcycle_Singapore = r"\d{2}(691|692|693|694|695)NN\d{3}|\d{2}NN(691|692|693|694|695)\d{3}"
# foreign_motorcycle_Sri_Lanka = r"\d{2}(696|697|698|699|700)NN\d{3}|\d{2}NN(696|697|698|699|700)\d{3}"
# foreign_motorcycle_Somalia = r"\d{2}(701|702|703|704|705)NN\d{3}|\d{2}NN(701|702|703|704|705)\d{3}"
# foreign_motorcycle_Senegal = r"\d{2}(706|707|708|709|710)NN\d{3}|\d{2}NN(706|707|708|709|710)\d{3}"
# foreign_motorcycle_Syria = r"\d{2}(711|712|713|714|715)NN\d{3}|\d{2}NN(711|712|713|714|715)\d{3}"
# foreign_motorcycle_Sahrawi_Arab_Democratic_Republic = r"\d{2}(716|717|718|719|720)NN\d{3}|\d{2}NN(716|717|718|719|720)\d{3}"
# foreign_motorcycle_Seychelles = r"\d{2}(721|722|723|724|725)NN\d{3}|\d{2}NN(721|722|723|724|725)\d{3}"
# foreign_motorcycle_Sao_Tome_and_Principe = r"\d{2}(726|727|728|729|730)NN\d{3}|\d{2}NN(726|727|728|729|730)\d{3}"
# foreign_motorcycle_Slovakia = r"\d{2}(731|732|733|734|735)NN\d{3}|\d{2}NN(731|732|733|734|735)\d{3}"
# foreign_motorcycle_Yemen = r"\d{2}(736|737|738|739|740)NN\d{3}|\d{2}NN(736|737|738|739|740)\d{3}"
# foreign_motorcycle_Liechtenstein = r"\d{2}(741|742|743|744|745)NN\d{3}|\d{2}NN(741|742|743|744|745)\d{3}"
# foreign_motorcycle_Hong_Kong = r"\d{2}(746|747|748|749|750)NN\d{3}|\d{2}NN(746|747|748|749|750)\d{3}"
# foreign_motorcycle_East_Timor = r"\d{2}(751|752|753|754|755)NN\d{3}|\d{2}NN(751|752|753|754|755)\d{3}"
# foreign_motorcycle_European_Union_Delegation = r"\d{2}(756|757|758|759|760)NN\d{3}|\d{2}NN(756|757|758|759|760)\d{3}"
# foreign_motorcycle_Saudi_Arabia = r"\d{2}(761|762|763|764|765)NN\d{3}|\d{2}NN(761|762|763|764|765)\d{3}"
# foreign_motorcycle_Liberia = r"\d{2}(766|767|768|769|770)NN\d{3}|\d{2}NN(766|767|768|769|770)\d{3}"

# foreign_motorcycle_Haiti = r"\d{2}(781|782|783|784|785)NN\d{3}|\d{2}NN(781|782|783|784|785)\d{3}"
# foreign_motorcycle_Peru = r"\d{2}(786|787|788|789|790)NN\d{3}|\d{2}NN(786|787|788|789|790)\d{3}"

# foreign_motorcycle_Andorra = r"\d{2}(791)NN\d{3}|\d{2}NN(791)\d{3}"
# foreign_motorcycle_Anguilla = r"\d{2}(792)NN\d{3}|\d{2}NN(792)\d{3}"
# foreign_motorcycle_Antigua_and_Barbuda = r"\d{2}(793)NN\d{3}|\d{2}NN(793)\d{3}"
# foreign_motorcycle_Bahamas = r"\d{2}(794)NN\d{3}|\d{2}NN(794)\d{3}"
# foreign_motorcycle_Bahrain = r"\d{2}(795)NN\d{3}|\d{2}NN(795)\d{3}"
# foreign_motorcycle_Barbados = r"\d{2}(796)NN\d{3}|\d{2}NN(796)\d{3}"
# foreign_motorcycle_Belize = r"\d{2}(797)NN\d{3}|\d{2}NN(797)\d{3}"
# foreign_motorcycle_Bermuda = r"\d{2}(798)NN\d{3}|\d{2}NN(798)\d{3}"
# foreign_motorcycle_Bhutan = r"\d{2}(799)NN\d{3}|\d{2}NN(799)\d{3}"
# foreign_motorcycle_Bosnia_And_Herzegovina = r"\d{2}(800)NN\d{3}|\d{2}NN(800)\d{3}"

# foreign_motorcycle_Ireland = r"\d{2}(801|802|803|804|805)NN\d{3}|\d{2}NN(801|802|803|804|805)\d{3}"

# foreign_motorcycle_Kenya = r"\d{2}(806)NN\d{3}|\d{2}NN(806)\d{3}"
# foreign_motorcycle_Botswana = r"\d{2}(807)NN\d{3}|\d{2}NN(807)\d{3}"
# foreign_motorcycle_Comoros = r"\d{2}(808)NN\d{3}|\d{2}NN(808)\d{3}"
# foreign_motorcycle_Dominican_Republic = r"\d{2}(809)NN\d{3}|\d{2}NN(809)\d{3}"
# foreign_motorcycle_North_Macedonia = r"\d{2}(810)NN\d{3}|\d{2}NN(810)\d{3}"
# foreign_motorcycle_Central_African_Republic = r"\d{2}(811)NN\d{3}|\d{2}NN(811)\d{3}"
# foreign_motorcycle_Croatia = r"\d{2}(812)NN\d{3}|\d{2}NN(812)\d{3}"
# foreign_motorcycle_Curacao = r"\d{2}(813)NN\d{3}|\d{2}NN(813)\d{3}"
# foreign_motorcycle_Dominica = r"\d{2}(814)NN\d{3}|\d{2}NN(814)\d{3}"
# foreign_motorcycle_El_Salvador = r"\d{2}(815)NN\d{3}|\d{2}NN(815)\d{3}"
# foreign_motorcycle_Honduras = r"\d{2}(816)NN\d{3}|\d{2}NN(816)\d{3}"
# foreign_motorcycle_Kiribati = r"\d{2}(817)NN\d{3}|\d{2}NN(817)\d{3}"
# foreign_motorcycle_Lesotho = r"\d{2}(818)NN\d{3}|\d{2}NN(818)\d{3}"
# foreign_motorcycle_Federated_States_of_Micronesia = r"\d{2}(819)NN\d{3}|\d{2}NN(819)\d{3}"
# foreign_motorcycle_Malawi = r"\d{2}(820)NN\d{3}|\d{2}NN(820)\d{3}"
# foreign_motorcycle_Mauritius = r"\d{2}(821)NN\d{3}|\d{2}NN(821)\d{3}"
# foreign_motorcycle_Monaco = r"\d{2}(822)NN\d{3}|\d{2}NN(822)\d{3}"
# foreign_motorcycle_Montenegro = r"\d{2}(823)NN\d{3}|\d{2}NN(823)\d{3}"
# foreign_motorcycle_South_Sudan = r"\d{2}(824)NN\d{3}|\d{2}NN(824)\d{3}"
# foreign_motorcycle_Nauru = r"\d{2}(825)NN\d{3}|\d{2}NN(825)\d{3}"
# foreign_motorcycle_Niue = r"\d{2}(826)NN\d{3}|\d{2}NN(826)\d{3}"
# foreign_motorcycle_Palau = r"\d{2}(827)NN\d{3}|\d{2}NN(827)\d{3}"
# foreign_motorcycle_paraguay = r"\d{2}(828)NN\d{3}|\d{2}NN(828)\d{3}"
# foreign_motorcycle_Cook_Islands = r"\d{2}(829)NN\d{3}|\d{2}NN(829)\d{3}"
# foreign_motorcycle_Puerto_Rico = r"\d{2}(830)NN\d{3}|\d{2}NN(830)\d{3}"
# foreign_motorcycle_Northern_Mariana_Islands = r"\d{2}(831)NN\d{3}|\d{2}NN(831)\d{3}"
# foreign_motorcycle_Solomon_Islands = r"\d{2}(832)NN\d{3}|\d{2}NN(832)\d{3}"
# foreign_motorcycle_Saint_Kitts_and_Nevis = r"\d{2}(833)NN\d{3}|\d{2}NN(833)\d{3}"
# foreign_motorcycle_Saint_Lucia = r"\d{2}(834)NN\d{3}|\d{2}NN(834)\d{3}"
# foreign_motorcycle_Saint_Vincent_and_the_Grenadines = r"\d{2}(835)NN\d{3}|\d{2}NN(835)\d{3}"
# foreign_motorcycle_San_Marino = r"\d{2}(836)NN\d{3}|\d{2}NN(836)\d{3}"
# foreign_motorcycle_Slovenia = r"\d{2}(837)NN\d{3}|\d{2}NN(837)\d{3}"
# foreign_motorcycle_Suriname = r"\d{2}(838)NN\d{3}|\d{2}NN(838)\d{3}"
# foreign_motorcycle_Eswatini = r"\d{2}(839)NN\d{3}|\d{2}NN(839)\d{3}"
# foreign_motorcycle_Tonga = r"\d{2}(840)NN\d{3}|\d{2}NN(840)\d{3}"
# foreign_motorcycle_Trinidad_And_Tobago = r"\d{2}(841)NN\d{3}|\d{2}NN(841)\d{3}"
# foreign_motorcycle_Tuvalu = r"\d{2}(842)NN\d{3}|\d{2}NN(842)\d{3}"
# # foreign_motorcycle_Vatican = r"\d{2}(843)NN\d{3}|\d{2}NN(843)\d{3}"  # 436-440에 포함


# foreign_motorcycle_Taiwan = r"\d{2}(885|886|887|888|889|890)NN\d{3}|\d{2}NN(885|886|887|888|889|890)\d{3}"




# # json
# foreign_motorcycle = {
#     foreign_motorcycle_Austria : "Austria",
#     foreign_motorcycle_Albania : "Albania",
#     foreign_motorcycle_UK_Northern_Ireland : "UK, Northern Ireland",
#     foreign_motorcycle_Egypt : "Egypt",
#     foreign_motorcycle_Azerbaijan : "Azerbaijan",
#     foreign_motorcycle_India : "India",
#     foreign_motorcycle_Angola : "Angola",
#     foreign_motorcycle_Afghanistan : "Afghanistan",
#     foreign_motorcycle_Algeria : "Algeria",
#     foreign_motorcycle_Argentina : "Argentina",
#     foreign_motorcycle_Armenia : "Armenia",
#     foreign_motorcycle_Iceland : "Iceland",
#     foreing_motorcycle_Belgium : "Belgium",
#     foreign_motorcycle_Poland : "Poland",
#     foreign_motorcycle_Portugal : "Portugal",
#     foreign_motorcycle_Bulgaria : "Bulgaria",
#     foreign_motorcycle_Burkina_Faso : "Burkina Faso",
#     foreign_motorcycle_Brazil : "Brazil",
#     foreign_motorcycle_Bangladesh : "Bangladesh",
#     foreign_motorcycle_Belarus : "Belarus",
#     foreign_motorcycle_Bolivia : "Bolivia",
#     foreign_motorcycle_Benin : "Benin",
#     foreign_motorcycle_Brunei : "Brunei",
#     foreign_motorcycle_Cuba : "Cuba",
#     foreign_motorcycle_Ivory_Coast : "Ivory Coast",
#     foreign_motorcycle_Congo_Brazzaville : "Congo Brazzaville",
#     foreign_motorcycle_Congo_Kinshasa : "Congo Kinshasa",
#     foreign_motorcycle_Chile : "Chile",
#     foreign_motorcycle_Colombia : "Colombia",
#     foreign_motorcycle_Cameroon : "Cameroon",
#     foreign_motorcycle_Canada : "Canada",
#     foreign_motorcycle_Kuwait : "Kuwait",
#     foreign_motorcycle_Cambodia : "Cambodia",
#     foreign_motorcycle_Kyrgyzstan : "Kyrgyzstan",
#     foreign_motorcycle_Qatar : "Qatar",
#     foreign_motorcycle_Cape_Verde : "Cape Verde",
#     foreign_motorcycle_Costa_Rica : "Costa Rica",
#     foreign_motorcycle_Germany : "Germany",
#     foreign_motorcycle_Zambia : "Zambia",
#     foreign_motorcycle_Zimbabwe : "Zimbabwe",
#     foreign_motorcycle_Denmark : "Denmark",
#     foreign_motorcycle_Ecuador : "Ecuador",
#     foreign_motorcycle_Eritrea : "Eritrea",
#     foreign_motorcycle_Ethiopia : "Ethiopia",
#     foreign_motorcycle_Estonia : "Estonia",
#     foreign_motorcycle_Guyana : "Guyana",
#     foreign_motorcycle_Gabon : "Gabon",
#     foreign_motorcycle_Gambia : "Gambia",
#     foreign_motorcycle_Djibouti : "Djibouti",
#     foreign_motorcycle_Georgia : "Georgia",
#     foreign_motorcycle_Jordan : "Jordan",
#     foreign_motorcycle_Guinea : "Guinea",
#     foreign_motorcycle_Ghana : "Ghana",
#     foreign_motorcycle_Guinea_Bissau : "Guinea Bissau",
#     foreign_motorcycle_Grenada : "Grenada",
#     foreign_motorcycle_Equatorial_Guinea : "Equatorial Guinea",
#     foreign_motorcycle_Guatemala : "Guatemala",
#     foreign_motorcycle_Hungary : "Hungary",
#     foreign_motorcycle_United_States : "United States",
#     foreign_motorcycle_Netherlands : "Netherlands",
#     foreign_motorcycle_Greece : "Greece",
#     foreign_motorcycle_Jamaica : "Jamaica",
#     foreign_motorcycle_Indonesia : "Indonesia",
#     foreign_motorcycle_Iran : "Iran",
#     foreign_motorcycle_Iraq : "Iraq",
#     foreign_motorcycle_Italy : "Italy",
#     foreign_motorcycle_Israel : "Israel",
#     foreign_motorcycle_Kazakhstan : "Kazakhstan",
#     foreign_motorcycle_Laos : "Laos",
#     foreign_motorcycle_Lebanon : "Lebanon",
#     foreign_motorcycle_Libya : "Libya",
#     foreign_motorcycle_Luxembourg : "Luxembourg",
#     foreign_motorcycle_Lithuania : "Lithuania",
#     foreign_motorcycle_Latvia : "Latvia",
#     foreign_motorcycle_Myanmar : "Myanmar",
#     foreign_motorcycle_Mongolia : "Mongolia",
#     foreign_motorcycle_Mozambique : "Mozambique",
#     foreign_motorcycle_Madagascar : "Madagascar",
#     foreign_motorcycle_Moldova : "Moldova",
#     foreign_motorcycle_Maldives : "Maldives",
#     foreign_motorcycle_Mexico : "Mexico",
#     foreign_motorcycle_Mali : "Mali",
#     foreign_motorcycle_Malaysia : "Malaysia",
#     foreign_motorcycle_Morocco : "Morocco",
#     foreign_motorcycle_Mauritania : "Mauritania",
#     foreign_motorcycle_Malta : "Malta",
#     foreign_motorcycle_Russia : "Russia",
#     foreign_motorcycle_Japan : "Japan",
#     foreign_motorcycle_Nicaragua : "Nicaragua",
#     foreign_motorcycle_New_Zealand : "New Zealand",
#     foreign_motorcycle_Niger : "Niger",
#     foreign_motorcycle_Nigeria : "Nigeria",
#     foreign_motorcycle_Namibia : "Namibia",
#     foreign_motorcycle_Nepal : "Nepal",
#     foreign_motorcycle_South_Africa : "South Africa",
#     foreign_motorcycle_Yugoslavia : "Yugoslavia",
#     foreign_motorcycle_Norway : "Norway",
#     foreign_motorcycle_Oman : "Oman",
#     foreign_motorcycle_Australia : "Australia",
#     foreign_motorcycle_France : "France",
#     foreign_motorcycle_Fiji : "Fiji",
#     foreign_motorcycle_Pakistan : "Pakistan",
#     foreign_motorcycle_Finland : "Finland",
#     foreign_motorcycle_Philippines : "Philippines",
#     foreign_motorcycle_Palestine : "Palestine",
#     foreign_motorcycle_Panama : "Panama",
#     foreign_motorcycle_Papua_New_Guinea : "Papua New Guinea",
#     foreign_motorcycle_International_Organization : "International Organization",
#     foreign_motorcycle_Rwanda : "Rwanda",
#     foreign_motorcycle_Romania : "Romania",
#     foreign_motorcycle_Chad : "Chad",
#     foreign_motorcycle_Czech_Republic : "Czech Republic",
#     foreign_motorcycle_Cyprus : "Cyprus",
#     foreign_motorcycle_Spain : "Spain",
#     foreign_motorcycle_Sweden : "Sweden",
#     foreign_motorcycle_Tanzania : "Tanzania",
#     foreign_motorcycle_Togo : "Togo",
#     foreign_motorcycle_Tajikistan : "Tajikistan",
#     foreign_motorcycle_China : "China",
#     foreign_motorcycle_Thailand : "Thailand",
#     foreign_motorcycle_Turkmenistan : "Turkmenistan",
#     foreign_motorcycle_Tunisia : "Tunisia",
#     foreign_motorcycle_Turkey : "Turkey",
#     foreign_motorcycle_Switzerland : "Switzerland",
#     foreign_motorcycle_North_Korea : "North Korea",
#     foreign_motorcycle_South_Korea : "South Korea",
#     foreign_motorcycle_United_Arab_Emirates : "United Arab Emirates",
#     foreign_motorcycle_Samoa : "Samoa",
#     foreign_motorcycle_Ukraine : "Ukraine",
#     foreign_motorcycle_Uzbekistan : "Uzbekistan",
#     foreign_motorcycle_Uganda : "Uganda",
#     foreign_motorcycle_Uruguay : "Uruguay",
#     foreign_motorcycle_Vanuatu : "Vanuatu",
#     foreign_motorcycle_Venezuela : "Venezuela",
#     foreign_motorcycle_Sudan : "Sudan",
#     foreign_motorcycle_Sierra_Leone : "Sierra Leone",
#     foreign_motorcycle_Singapore : "Singapore",
#     foreign_motorcycle_Sri_Lanka : "Sri Lanka",
#     foreign_motorcycle_Somalia : "Somalia",
#     foreign_motorcycle_Senegal : "Senegal",
#     foreign_motorcycle_Syria : "Syria",
#     foreign_motorcycle_Sahrawi_Arab_Democratic_Republic : "Sahrawi Arab Democratic Republic",
#     foreign_motorcycle_Seychelles : "Seychelles",
#     foreign_motorcycle_Sao_Tome_and_Principe : "Sao Tome and Principe",
#     foreign_motorcycle_Slovakia : "Slovakia",
#     foreign_motorcycle_Yemen : "Yemen",
#     foreign_motorcycle_Liechtenstein : "Liechtenstein",
#     foreign_motorcycle_Hong_Kong : "Hong Kong",
#     foreign_motorcycle_East_Timor : "East Timore",
#     foreign_motorcycle_European_Union_Delegation : "European Union Delegation",
#     foreign_motorcycle_Saudi_Arabia : "Saudi Arabia",
#     foreign_motorcycle_Liberia : "Liberia",

#     foreign_motorcycle_Haiti : "Haiti",
#     foreign_motorcycle_Peru : "Peru",

#     foreign_motorcycle_Andorra : "Andorra",
#     foreign_motorcycle_Anguilla : "Anguilla",
#     foreign_motorcycle_Antigua_and_Barbuda : "Antigua and Barbuda",
#     foreign_motorcycle_Bahamas : "Bahamas",
#     foreign_motorcycle_Bahrain : "Bahrain",
#     foreign_motorcycle_Barbados : "Barbados",
#     foreign_motorcycle_Belize : "Belize",
#     foreign_motorcycle_Bermuda : "Bermuda",
#     foreign_motorcycle_Bhutan : "Bhutan",
#     foreign_motorcycle_Bosnia_And_Herzegovina : "Bosnia And Herzegovina",

#     foreign_motorcycle_Ireland : "Ireland",

#     foreign_motorcycle_Kenya : "Kenya",
#     foreign_motorcycle_Botswana : "Botswana",
#     foreign_motorcycle_Comoros : "Comoros",
#     foreign_motorcycle_Dominican_Republic : "Dominican Republic",
#     foreign_motorcycle_North_Macedonia : "North Macedonia",
#     foreign_motorcycle_Central_African_Republic : "Central African Republic",
#     foreign_motorcycle_Croatia : "Croatia",
#     foreign_motorcycle_Curacao : "Curacao",
#     foreign_motorcycle_Dominica : "Dominica",
#     foreign_motorcycle_El_Salvador : "El Salvador",
#     foreign_motorcycle_Honduras : "Honduras",
#     foreign_motorcycle_Kiribati : "Kiribati",
#     foreign_motorcycle_Lesotho : "Lesotho",
#     foreign_motorcycle_Federated_States_of_Micronesia : "Federated States of Micronesia",
#     foreign_motorcycle_Malawi : "Malawi",
#     foreign_motorcycle_Mauritius : "Mauritius",
#     foreign_motorcycle_Monaco : "Monaco",
#     foreign_motorcycle_Montenegro : "Montenegro",
#     foreign_motorcycle_South_Sudan : "South Sudan",
#     foreign_motorcycle_Nauru : "Nauru",
#     foreign_motorcycle_Niue : "Niue",
#     foreign_motorcycle_Palau : "Palau",
#     foreign_motorcycle_paraguay : "paraguay",
#     foreign_motorcycle_Cook_Islands : "Cook Islands",
#     foreign_motorcycle_Puerto_Rico : "Puerto Rico",
#     foreign_motorcycle_Northern_Mariana_Islands : "Northern Mariana Islands",
#     foreign_motorcycle_Solomon_Islands : "Solomon Islands",
#     foreign_motorcycle_Saint_Kitts_and_Nevis : "Saint Kitts and Nevis",
#     foreign_motorcycle_Saint_Lucia : "Saint Lucia",
#     foreign_motorcycle_Saint_Vincent_and_the_Grenadines : "Saint Vincent and the Grenadines",
#     foreign_motorcycle_San_Marino : "San Marino",
#     foreign_motorcycle_Slovenia : "Slovenia",
#     foreign_motorcycle_Suriname : "Suriname",
#     foreign_motorcycle_Eswatini : "Eswatini",
#     foreign_motorcycle_Tonga : "Tonga",
#     foreign_motorcycle_Trinidad_And_Tobago : "Trinidad And Tobago",
#     foreign_motorcycle_Tuvalu : "Tuvalu",
#     foreign_motorcycle_Vatican : "Vatican",

#     foreign_motorcycle_Taiwan : "Taiwan"
# }