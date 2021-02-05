def find_largest(list_param):
  # base case:
  # if there is only one value, return the only value as the largest
  if len(list_param) == 1:
    return list_param[0]

  # recursive step:
  # compare the list_param[0] vs the largest among the rest n-1 values:
    # if the list_param[0] is larger, return it
    # otherwise, return the largest amount the rest n-1 values
  else:
    largest_of_the_rest = find_largest(list_param[1:])
    if list_param[0] > largest_of_the_rest:
      return list_param[0]
    else:
      return largest_of_the_rest
  