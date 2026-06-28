def safe_division(a,b):
  if b == 0:
    return "Division by zero is not allowed"
  return a/b


def safe_multiply(a,b):
  if a == 0 or b == 0:
    return "Answer is zero."
  return a * b  
print(safe_division(10,2))
print(safe_division(10,0))

print(safe_multiply(0,0))
print(safe_multiply(10,1))
print(safe_multiply(11,0))
