# euler 9
# KeyJect
def isPythagorean(a, b, c):
  temp = [a, b, c]
  temp.sort()
  a, b, c = temp
  if not a<b<c :
    return False
  if a**2 + b**2 == c**2:
    return True
  return False

def main():
  for i in range(1000):
    for j in range(1000 - i):
      k = 1000 - i - j
      if isPythagorean(i , j , k):
        print(int(i*j*k))
        return
main()
