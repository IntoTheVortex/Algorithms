import sys 

def main():
  string1 = sys.argv[1]
  string2 = sys.argv[2]

  str_list1 = make_permutations(string1)
  str_list2 = make_permutations(string2)
  answer = lcs(str_list1, str_list2)

  print("The longest subsequence is:")
  print(answer)

  
def lcs(str_list1, str_list2):
  max = 0

  outer_length = len(str_list1)
  inner_length = len(str_list2)

  for i in range(outer_length):
    for j in range(inner_length):
      if str_list1[i] == str_list2[j]:
        if len(str_list1[i]) > max:
          max = len(str_list1[i])
          longest_subsequence = str_list1[i]

  return longest_subsequence


def make_permutations(start_str):
  curr_str = ""
  str_list = [""]

  for i in range(len(start_str)):
    recursive_permute(i, 0, start_str, curr_str, str_list)

  #print("String permutation list is: ")
  #print(str_list)
  return str_list


def recursive_permute(stop_i, curr_i, start_str, curr_str, str_list):
  #base case
  if len(curr_str) > stop_i or curr_i > stop_i:
    str_list.append(curr_str)
    return

  #new str object for rec calls 
  #first, don't include curr index item
  new_str = curr_str
  recursive_permute(stop_i, curr_i+1, start_str, new_str, str_list)
  #next, include curr index item  
  new_str += start_str[curr_i]
  recursive_permute(stop_i, curr_i+1, start_str, new_str, str_list)
  return
  



if __name__ == "__main__":
  main()
