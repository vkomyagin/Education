*** Test Cases ***
Excersize 3
  ${dictionary_1}  Create Dictionary  'a'=300  'b'=400
  ${dictionary_2}  Create Dictionary  'c'=500  'd'=600
  Log To Console  ${dictionary_1}
  Log To Console  ${dictionary_2}
  Evaluate  $dictionary_1.update($dictionary_2)
  Log To Console  ${dictionary_1}