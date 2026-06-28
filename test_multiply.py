from myapp import safe_multiply

def tes_zero_multipication():
  assert safe_multiply(1,0) == 'Answer is zero.'
def test_normal_multiplication():
  assert safe_multiply(10,90) == 900
def tes1_zero1_multipication():
  assert safe_multiply(0,10) == 'Answer is zero.'
