import pytest
from person import Person

@pytest.fixture
def person():
    return Person('Peter', 'secrät', 7.00)

def test_person_valid():
    person = Person('Peter', 'secrät', 7.00)
    assert person.__str__() == "Person(givenname='Peter', password='secrät', balance=7.0)"

def test_get_givenname(person):
    assert person.givenname == 'Peter'

def test_get_password(person):
    assert person.password == 'secrät'

def test_set_givenname(person):
    person.givenname = 'Adam'
    assert person.givenname == 'Adam'

def test_set_password(person):
    person.password = '<PASSWORD>'
    assert person.password == '<PASSWORD>'

def test_get_balance(person):
    assert person.balance == 7.0

def test_set_balance_valid(person):
    person.balance = 9.0
    assert person.balance == 9.0

@pytest.mark.xfail
def test_set_balance_invalid(person):
    with pytest.raises(ValueError):
        person.balance = "abc"
