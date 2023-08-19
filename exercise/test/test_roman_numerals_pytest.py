from pytest import mark
from app.roman_numerals import parse

@mark.parametrize("noman_num,expected", [('IX', 9), ('X', 10), ("IX", 9), ("XI",	11), ("XIV",	14),
("XIX",	19),("XX",	20),("XXXIV",	34),("XLI",	41),("L",	50),("XCIX",	99),("C",	100),
("CCCXXXIII",	333),("DLV",	555),("CDXLIX",	449),("MCMLXXII",	1972)])
def test_roman_numeral_parser(noman_num, expected):
    result = parse(noman_num)
    assert result == expected
