extra = ''

def show():
    for i in range(127):
        if len(format(i,'b')) < 8:
            extra = '0'*(8-len(format(i,'b')))
        print('Binary:', '-->', str(extra + format(i,'b')), '|', 'Hex:', '-->', hex(i), '|', 'Decimal:', '-->', i, '|' "Char:", "-->", chr(i))

def search(index):
    for i in range(127):
        if len(format(i,'b')) < 8:
            extra = '0'*(8-len(format(i,'b')))
        line = ('Binary:', '-->', str(extra + format(i,'b')), '|', 'Hex:', '-->', hex(i), '|', 'Decimal:', '-->', i, '|' "Char:", "-->", chr(i))
        if index in line:
            print(line)

def text(w):
    for l in w:
        for i in range(127):
            if len(format(i,'b')) < 8:
                extra = '0'*(8-len(format(i,'b')))
            line = ('Binary:', '-->', str(extra + format(i,'b')), '|', 'Hex:', '-->', hex(i), '|', 'Decimal:', '-->', i, '|' "Char:", "-->", chr(i))
            if l in line:
                print(line)

def convert(w):
    for l in w.lower().split():
        for i in range(0,127):
            if len(format(i,'b')) < 8:
                extra = '0'*(8-len(format(i,'b')))
            line = ('Binary:', '-->', str(extra + format(i,'b')), '|', 'Hex:', '-->', hex(i), '|', 'Decimal:', '-->', i, '|' "Char:", "-->", chr(i))
            if l in line:
                print(line)

def convertd(w):
    for l in w.split():
        for i in range(127):
            if len(format(i,'b')) < 8:
                extra = '0'*(8-len(format(i,'b')))
            line = ('Binary:', '-->', str(extra + format(i,'b')), '|', 'Hex:', '-->', hex(i), '|', 'Decimal:', '-->', i, '|' "Char:", "-->", chr(i))
            if int(l) in line:
                print(line)
