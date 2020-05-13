import re
from unicodedata import normalize

def checkio(in_string):

    s = in_string
    # -> NFD y eliminar diacríticos
    s = re.sub(
        r"([^n\u0300-\u036f]|)[\u0300-\u036f]+", r"\1",
        normalize("NFD", s), 0, re.I
    )

    # -> NFC
    s = normalize('NFC', s)

    return s


if __name__ == '__main__':
    assert checkio(u"préfèrent") == u"preferent"
    assert checkio(u"loài trăn lớn") == u"loai tran lon"
    print('Done')
