from operator import contains
from pythonisms.pythonisms import Animal


def test_init():
    assert Animal
    
def test_object():
    kingKong = Animal('gorilla', 'King Kong')
    assert str(kingKong) == 'I am a gorilla my name is King Kong'
    
def test_object_len():
    kingKong = Animal('gorilla', 'King Kong')
    assert len(kingKong) == 9
    