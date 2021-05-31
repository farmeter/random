/**
배열 array가 주어지고, [i, j, k]를 원소로 가지는 2차원 배열 commands가 주어집니다.
주어진 배열을 먼저 i부터 j까지 자릅니다.
자른 배열을 오름차순으로 정렬하여 k번째의 수를 answer에 추가합니다.
위의 방법을 commands의 주어진 수만큼 반복하여 answer를 채워서 리턴합니다.
**/

def solution(array, comands):
  def com(arr, a, b, c):
    arr = arr[a-1:b]
    arr.sort()
    return arr[c-1]
    
  answer = []
  for x, y, z in commands:
    answer.append(com(array, x, y, z))
    
  return answer
