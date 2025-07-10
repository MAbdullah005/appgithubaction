from src.math import add,sub

def test_add():
    assert add(1,2)==3
    assert add(9,0)==9
    assert add(8,7)==15
def test_sub():
    assert sub(1,2)==-1
    assert sub(9,8)==1
    assert sub(6,2)==4