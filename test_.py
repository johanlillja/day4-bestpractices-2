import simple_math

def test_simple_math():
    assert  simple_math.simple_add(1337,69) == 1406
    assert  simple_math.simple_sub(420,1337)==-917
    assert  simple_math.simple_mult(420,247)==103740
    assert  simple_math.simple_div(194,4)==48.5
    assert  simple_math.poly_first(9,11,3)==38
    assert  simple_math.poly_second(9,1,1,2003)==162253