def generateNumber(i):
  return (i * (3 + i)) * (1 if i % 2 == 0 else -1)

def calc(m):
  nums = [generateNumber(i) for i in range(m)]

  return (
    f"Middle item: {nums[m // 2]}\n"
    f"Min item: {min(nums)}\n"
    f"Max item: {max(nums)}\n"
    f"Sum: {sum(nums)}"
  )

if __name__ == '__main__':
  print(calc(int(input("Choose a number: "))))
