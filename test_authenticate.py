import sys

import pytest

from authenticate import load_people, login
from person import Person

@pytest.fixture
def people():
    """A fixture with people objects"""
    people_list = [
        Person('Inga', 'geheim', 14.00),
        Person('Peter', 'secrät', 7.00),
        Person('Beatrice', 'passWORT', 23.00)
    ]
    return people_list

def test_login_valid(capsys, monkeypatch, people):
    inputs = iter(["geheim","geheim"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    response = login()
    captured = capsys.readouterr().out
    assert captured == ""
    assert response.__str__() == "Person(givenname='Inga', password='geheim', balance=14.0)"

@pytest.mark.timeout(10)
def test_login_invalid(capsys, monkeypatch, people):
    def input_generator():
        yield "testing"
        yield "abc"
        raise KeyboardInterrupt
    inputs = input_generator()

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    try:
        login()
    except KeyboardInterrupt:
        pass

    captured = capsys.readouterr().out

    assert captured == "Passwort falsch\nPasswort falsch\nPasswort falsch\nPasswort falsch\nPasswort falsch\nPasswort falsch\n"


def test_load_people(people):
    a_people = load_people()
    assert people == a_people
