from src.math import add,sub,mul

def test_add():
    assert add(1,2)==3
    assert add(9,0)==9
    assert add(8,7)==15
def test_sub():
    assert sub(1,2)==-1
    assert sub(9,8)==1
    assert sub(6,2)==4
def test_mul():
    assert mul(2,2)==4
    assert mul(4,5)==20
    assert mul(0,9)==1
