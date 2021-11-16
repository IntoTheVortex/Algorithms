import sys

def main():
  string1 = sys.argv[1]
  string2 = sys.argv[2]

  string1 = '0'+string1;
  string2 = '0'+string2;
  C = [[0 for x in range(len(string2))] for y in range(len(string1))]

  answer = lcs(C, string1, string2)
  print()
  print(answer)


def lcs(C, string1, string2):
  for i in range(1,len(string1)):
    for j in range(1,len(string2)):
      if string1[i] == string2[j]:
        C[i][j] = C[i-1][j-1] + 1
      else:
        C[i][j] = max(C[i][j-1], C[i-1][j])
  
  answer = ""
  backtrack(C, string1, string2,i,j,answer)
  return C[len(string1)-1][len(string2)-1]


def backtrack(C, string1, string2, i, j, answer):

  if i == 0 or j == 0:
    print(answer)
    return ""
  if string1[i] == string2[j]:
    new_answer = string1[i] + answer
    return backtrack(C, string1, string2, i-1, j-1,new_answer) + string1[i]
  if C[i][j-1] > C[i-1][j]:
    return backtrack(C, string1, string2, i, j-1,answer)
  return backtrack(C, string1, string2, i-1, j,answer)
  


if __name__ == "__main__":
  main()