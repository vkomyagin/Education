*** Test Cases ***
Excersize 1 test1
  ${test_str1}  Set Variable  "мокнет Оксана с котенком"
  Log  Var1 ${test_str1}
  Should Be Equal As Strings  ${test_str1[1].lower()}  ${test_str1[-2].lower()}  "Symbols different!"
Excersize 1 test2
  ${test_str2}  Set Variable  "Йохонсон просто отличный парень"
  Log  Var2 ${test_str2}
  Should Be Equal As Strings  ${test_str2[1].lower()}  ${test_str2[-2].lower()}  "Symbols different!"
  