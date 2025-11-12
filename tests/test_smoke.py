from calculator import calculate_exp
from text_checking import checking


def test_smoke():
    assert True

def test_is_empty():
    assert  checking("123")['Symbols']>0

def test_is_only_digits():
    assert  checking("123")['Numbers']==3

def test_is_only_small_letters():
    assert  checking("abcd")['SMALLS letters']==4

def test_is_only_big_letters():
    assert  checking("ABCD")['BIG letters']==4

def test_is_only_letters():
    assert  checking("abcd")['Numbers']==0

def test_is_checking_symbols_also():
    assert checking("abcd,./ ,.")['SMALLS letters']==4
    assert checking("abcd,./ ,.")['Symbols']==10

def test_non_latin_letters():
    assert checking('Привет123')["Numbers"] == 3
    assert checking('Привет123')["Symbols"] == 9

def test_is_only_punctuation_symbols():
    assert  checking(",./,./,./")['Letters']==0

def test_long_string():
    text = "Ab1!" * 25
    assert checking(text)["Symbols"] == 100
    assert checking(text)["Numbers"] == 25
    assert checking(text)["Letters"] == 50

def test_of_all():
    assert  checking("abcdABCD123")['SMALLS letters']==4
    assert  checking("abcdABCD123")['BIG letters']==4
    assert  checking("abcdABCD123")['Numbers letters']==3