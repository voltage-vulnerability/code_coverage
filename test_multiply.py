from myapp import safe_multiply

def zero_multipication():
  assert safe_multiply(0,0) == 'Answer is zero.'
def normal_multiplication():
  assert safe_multiply(10,90) == 900
