def build_and_find_binaries(current_string,target_len,current_len,one_counter,zero_counter):
  ''' Finds all N-digit binary numbers having more 1's than 0's for any prefix recursively'''



  # create a string of every binary number of to target length
  if len(current_string) == target_len:
    # if current_string has more 1's print and stop the recursion
    if(one_counter > zero_counter):
      print(current_string)
      return current_string
    
    # do nothin if current_string has more less or equal 1's to 0's
    if(one_counter < zero_counter):
      pass

  # if current_string less than target_len start recursion
  # two recursive functions are called while appenedning a 1 or a 0 to the current_string, respectively.
  if len(current_string) < target_len:
    if current_string != None:
      build_and_find_binaries(current_string+'0',target_len,current_len,one_counter,zero_counter+1)
      build_and_find_binaries(current_string+'1',target_len,current_len,one_counter+1,zero_counter)


build_and_find_binaries('',7,0,0,0)