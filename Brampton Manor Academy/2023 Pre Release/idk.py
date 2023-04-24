def ConvertToDecimal(BinaryString):
    DecimalNumber = 0
    for Bit in BinaryString:
        BitValue = int(Bit)
        DecimalNumber = DecimalNumber * 2 + BitValue
    return DecimalNumber


def ConvertToBinary(DecimalNumber):
    BinaryString = ''
    while DecimalNumber > 0:
        Remainder = DecimalNumber % 2
        Bit = str(Remainder)
        BinaryString = Bit + BinaryString
        DecimalNumber = DecimalNumber // 2
    while len(BinaryString) < 4:
        BinaryString = '0' + BinaryString
    return BinaryString

a = 39
b = ~a

print(a, ConvertToBinary(a))
print(b, ConvertToBinary(b))