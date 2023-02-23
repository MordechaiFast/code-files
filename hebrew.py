import unicodedata

א_ב = "אבגדהוזחטיכלמנסעפצקרשתךםןףץ"
for letter in א_ב:
    print(f"{letter}: {letter.encode()}")
'''for i in range(1424, 1536):
    letter = chr(i)
    try:
        print(f"{letter}: {ord(letter)} \\u{ord(letter):04x} {unicodedata.name(letter)}")
    except ValueError:
        print(f"{letter}: {ord(letter)} \\u{ord(letter):04x} -----")
'''
