*** Test Cases ***
Excersize 2
  ${test_list}   create list  0  1  55  5  2  3  8  13  1  21  34 
  ${test_sorted}  Evaluate  sorted(${test_list})
  Log To Console  ${test_sorted[0]} ${test_sorted[-1]}