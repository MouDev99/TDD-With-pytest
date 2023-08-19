
def parse(roman_num):
    special = {'IV': 4, 'IX': 9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
    usual = {'I': 1, 'V': 5, 'X': 10, 'L':50, 'C':100, 'D':500, 'M': 1000}
    ans = 0
    i = 0

    while i < len(roman_num):
        print(i)
        if roman_num[i:i+2] in special:
            print ('---sp')
            ans += special[roman_num[i:i+2]]
            i += 2
        elif roman_num[i] in usual:
            ans += usual[roman_num[i]]
            i += 1
        else:
            raise Exception(f'Not a roman symbol: {roman_num[i]}')
    return ans
