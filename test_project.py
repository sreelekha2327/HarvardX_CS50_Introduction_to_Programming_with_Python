import project as p
import pytest


def test_Student():
    assert p.Student("14001A0123", "Sree ram", "M", "85", "75", "94", "86", "100").__str__() == {
        "hallTicket": "14001A0123",
        "fn": "Sree Ram",
        "ln": "M",
        "eng": "85",
        "maths": "75",
        "sci": "94",
        "ss": "86",
        "cs": "100",
    }
    with pytest.raises(Exception) as e:
        xyz=p.Student("14001A0123", "Sree ram@#", "M", "85", "75", "94", "86", "100")
        assert e.type == ValueError
    with pytest.raises(Exception) as e:
        p.Student("14001A0123", "Sree ram", "M", "cat", "75", "94", "86", "100")
        assert e.type == ValueError
    with pytest.raises(Exception) as e:
        p.Student("14001A0123", "Sree ram", "M", "102", "75", "94", "86", "100")
        assert e.type == ValueError

def test_totalScore() :
    data = {
        "hallTicket": "14001A0123",
        "fn": "Sree Ram",
        "ln": "M",
        "eng": "85",
        "maths": "75",
        "sci": "94",
        "ss": "86",
        "cs": "100",
    }
    assert p.totalScore(**data) == {"total": 440, "grade": "A"}
    data["cs"] = 10
    assert p.totalScore(**data) == {"total": 350, "grade": "C"}

def test_subjectGrade() :
    assert p.subjectGrade(95) == "A"
    assert p.subjectGrade(80) == "B"
    assert p.subjectGrade(10) == "E"
    assert p.subjectGrade(60) == "C"
    assert p.subjectGrade(90) == "B"
    assert p.subjectGrade(40) == "D"





