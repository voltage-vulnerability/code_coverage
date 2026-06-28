from myapp import safe_division

def test_normal_division():
  assert safe_division(100,5) == 20.0


def test_zero_division():
  assert safe_division(10,0) == 'Division by zero is not allowed'
