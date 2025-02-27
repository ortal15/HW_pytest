import pytest
from hw_file import calculator

"""d. הוסף פונקציית טסט הבודקת את פונקצית power, בטסט שלח את המספר 2 ו 4-
לפונקציית power ובצע assert לבדוק שחזרה התוצאה 16 מהפונקציה )assert )"""


def test_power_d():
    # arrange
    a: int = 2
    b: int = 4
    expected: int = 16

    # act
    actual: int = calculator.power(a, b)

    # assert
    assert actual == expected


"""e. כמו בסעיף הקודם, בדוק בטסט שב - power עבור 3 ו- 2 חזר 9 )assert )"""


def test_power_e():
    # arrange
    a: int = 3
    b: int = 2
    expected: int = 9

    # act
    actual: int = calculator.power(a, b)

    # assert
    assert actual == expected


"""f. בדוק בטסט שב- sqrt עבור 25 חזר 5 )השתמש ב assert )"""


def test_sqrt_f():
    # arrange
    a: int = 25
    expected: int = 5
    # act
    actual: int = calculator.sqrt(a)
    # assert
    assert actual == expected


"""g. בדוק בטסט שב- sqrt עבור מינוס 5 התרחשה שגיא ה מסוג ValueError
רמז: (ValueError(raises.pytest with( ראה קוד מהשיעור("""


def test_sqrt_minos():
    with pytest.raises(ValueError) as ex:
        calculator.sqrt(-5)


"""בדוק בטסט שב- factorial עבור 4 חזר 24 )השתמש ב assert )"""


def test_factorial_h():
    # arrange
    a: int = 4
    expected: int = 24

    # act
    actual: int = calculator.factorial(a)

    # assert
    assert actual == expected


"""i. בדוק בטסט שב- factorial עבור 5 חזר 120 )השתמש ב assert )"""


def test_factorial_i():
    # arrange
    a: int = 5
    expected: int = 120

    # act
    actual: int = calculator.factorial(a)

    # assert
    assert actual == expected


"""j. בדוק בטסט שב- factorial עבור מינוס 3 התרחשה שגיאה מסוג ValueError"""


def test_factorial_minos():
    with pytest.raises(ValueError) as ex:
        calculator.sqrt(-3)
