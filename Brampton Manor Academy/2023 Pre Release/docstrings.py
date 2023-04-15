# Skeleton Program for the AQA AS Summer 2023 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA Programmer Team
# developed in a Python 3 environment

# Version number: 0.0.0


EMPTY_STRING = ""
HI_MEM = 20
MAX_INT = 127  # 8 bits available for operand (two's complement integer)
PC = 0
ACC = 1
STATUS = 2
TOS = 3
ERR = 4


class AssemblerInstruction:
    def __init__(self):
        self.OpCode = EMPTY_STRING
        self.OperandString = EMPTY_STRING
        self.OperandValue = 0


def DisplayMenu():
    """
    description: displays menu
    """
    print()
    print("Main Menu")
    print("=========")
    print("L - Load a program file")
    print("D - Display source code")
    print("E - Edit source code")
    print("A - Assemble program")
    print("R - Run the program")
    print("X - Exit simulator")
    print()


def GetMenuOption():
    """
    description: retrieves the users option
    return type: string
    """
    Choice = EMPTY_STRING
    while len(Choice) != 1:
        Choice = input("Enter your choice: ")
    return Choice[0]


def ResetSourceCode(SourceCode):
    """
    parameters: array
    description: fills array with empty strings
    return type: array
    """
    for LineNumber in range(HI_MEM):
        SourceCode[LineNumber] = EMPTY_STRING
    return SourceCode


def ResetMemory(Memory):
    """
    parameters: array
    description: sets default values for every object in memory array
    return type: array
    """
    for LineNumber in range(HI_MEM):
        Memory[LineNumber].OpCode = EMPTY_STRING
        Memory[LineNumber].OperandString = EMPTY_STRING
        Memory[LineNumber].OperandValue = 0
    return Memory


def DisplaySourceCode(SourceCode):
    """
    parameters: array
    description: displays the assembly code
    return type:
    """
    print()
    NumberOfLines = int(SourceCode[0])
    for LineNumber in range(0, NumberOfLines + 1):
        print("{:>2d} {:<40s}".format(LineNumber, SourceCode[LineNumber]))
    print()


def LoadFile(SourceCode):
    """
    parameters: array
    description: retrieves file name from user and loads it. also sets the first index of SourceCode as the number of lines
    return type: array
    """
    FileExists = False
    SourceCode = ResetSourceCode(SourceCode)
    LineNumber = 0
    FileName = input("Enter filename to load: ")
    try:
        FileIn = open(FileName + ".txt", 'r')
        FileExists = True
        Instruction = FileIn.readline()
        while Instruction != EMPTY_STRING:
            LineNumber += 1
            SourceCode[LineNumber] = Instruction[:-1]
            Instruction = FileIn.readline()
        FileIn.close()
        SourceCode[0] = str(LineNumber)
    except:
        if not FileExists:
            print("Error Code 1")
        else:
            print("Error Code 2")
            SourceCode[0] = str(LineNumber - 1)
    if LineNumber > 0:
        DisplaySourceCode(SourceCode)
    return SourceCode


def EditSourceCode(SourceCode):
    """
    parameters: array
    description: allows user to edit line in code
    return type: array
    """
    LineNumber = int(input("Enter line number of code to edit: "))
    print(SourceCode[LineNumber])
    Choice = EMPTY_STRING
    while Choice != "C":
        Choice = EMPTY_STRING
        while Choice != "E" and Choice != "C":
            print("E - Edit this line")
            print("C - Cancel edit")
            Choice = input("Enter your choice: ")
        if Choice == "E":
            SourceCode[LineNumber] = input("Enter the new line: ")
        DisplaySourceCode(SourceCode)
    return SourceCode


def UpdateSymbolTable(SymbolTable, ThisLabel, LineNumber):
    """
    parameters:
    description:
    return type:
    """
    if ThisLabel in SymbolTable:
        print("Error Code 3")
    else:
        SymbolTable[ThisLabel] = LineNumber
    return SymbolTable


def ExtractLabel(Instruction, LineNumber, Memory, SymbolTable):
    """
    parameters: string, int, array, dict
    description: extracts the label
    return type: dict, array
    """
    if len(Instruction) > 0:
        ThisLabel = Instruction[0:5]
        ThisLabel = ThisLabel.strip()
        if ThisLabel != EMPTY_STRING:
            if Instruction[5] != ':':
                print("Error Code 4")
                Memory[0].OpCode = "ERR"
            else:
                SymbolTable = UpdateSymbolTable(SymbolTable, ThisLabel, LineNumber)
    return SymbolTable, Memory


def ExtractOpCode(Instruction, LineNumber, Memory):
    """
    parameters: string, int, array
    description: extracts the opcode
    return type: array
    """
    if len(Instruction) > 9:
        OpCodeValues = ["LDA", "STA", "LDA#", "HLT", "ADD", "JMP", "SUB", "CMP#", "BEQ", "SKP", "JSR", "RTN", "   "]
        Operation = Instruction[7:10]
        if len(Instruction) > 10:
            AddressMode = Instruction[10:11]
            if AddressMode == '#':
                Operation += AddressMode
        if Operation in OpCodeValues:
            Memory[LineNumber].OpCode = Operation
        else:
            if Operation != EMPTY_STRING:
                print("Error Code 5")
                Memory[0].OpCode = "ERR"
    return Memory


def ExtractOperand(Instruction, LineNumber, Memory):
    """
    parameters: string, int, array
    description: extracts the operand
    return type: array
    """
    if len(Instruction) >= 13:
        Operand = Instruction[12:]
        ThisPosition = -1
        for Position in range(len(Operand)):
            if Operand[Position] == '*':
                ThisPosition = Position
        if ThisPosition >= 0:
            Operand = Operand[:ThisPosition]
        Operand = Operand.strip()
        Memory[LineNumber].OperandString = Operand
    return Memory


def PassOne(SourceCode, Memory, SymbolTable):
    """
    parameters: array, array, dict
    description:
    return type: array, dict
    """
    NumberOfLines = int(SourceCode[0])
    for LineNumber in range(1, NumberOfLines + 1):
        Instruction = SourceCode[LineNumber]
        SymbolTable, Memory = ExtractLabel(Instruction, LineNumber, Memory, SymbolTable)
        Memory = ExtractOpCode(Instruction, LineNumber, Memory)
        Memory = ExtractOperand(Instruction, LineNumber, Memory)
    return Memory, SymbolTable


def PassTwo(Memory, SymbolTable, NumberOfLines):
    """
    parameters: array, dict, int
    description:
    return type: array
    """
    for LineNumber in range(1, NumberOfLines + 1):
        Operand = Memory[LineNumber].OperandString
        if Operand != EMPTY_STRING:
            if Operand in SymbolTable:
                OperandValue = SymbolTable[Operand]
                Memory[LineNumber].OperandValue = OperandValue
            else:
                try:
                    OperandValue = int(Operand)
                    Memory[LineNumber].OperandValue = OperandValue
                except:
                    print("Error Code 6")
                    Memory[0].OpCode = "ERR"
    return Memory


def DisplayMemoryLocation(Memory, Location):
    """
    parameters: array, int
    description: displays the memory of the value
    return type: 
    """
    print("*  {:<5s}{:<5d} |".format(Memory[Location].OpCode, Memory[Location].OperandValue), end='')


def DisplaySourceCodeLine(SourceCode, Location):
    """
    parameters: array, int
    description: displays the code
    """
    print(" {:>3d}  |  {:<40s}".format(Location, SourceCode[Location]))


def DisplayCode(SourceCode, Memory):
    """
    parameters: array, array
    description: displays the given code
    """
    print("*  Memory     Location  Label  Op   Operand Comment")
    print("*  Contents                    Code")
    NumberOfLines = int(SourceCode[0])
    DisplayMemoryLocation(Memory, 0)
    print("   0  |")
    for Location in range(1, NumberOfLines + 1):
        DisplayMemoryLocation(Memory, Location)
        DisplaySourceCodeLine(SourceCode, Location)


def Assemble(SourceCode, Memory):
    """
    parameters: array, array
    description: idk
    return type: array
    """
    Memory = ResetMemory(Memory)
    NumberOfLines = int(SourceCode[0])
    SymbolTable = {}
    Memory, SymbolTable = PassOne(SourceCode, Memory, SymbolTable)
    if Memory[0].OpCode != "ERR":
        Memory[0].OpCode = "JMP"
        if "START" in SymbolTable:
            Memory[0].OperandValue = SymbolTable["START"]
        else:
            Memory[0].OperandValue = 1
        Memory = PassTwo(Memory, SymbolTable, NumberOfLines)
    return Memory


def ConvertToBinary(DecimalNumber):
    """
    parameters:
    description:
    return type:
    """
    BinaryString = EMPTY_STRING
    while DecimalNumber > 0:
        Remainder = DecimalNumber % 2
        Bit = str(Remainder)
        BinaryString = Bit + BinaryString
        DecimalNumber = DecimalNumber // 2
    while len(BinaryString) < 3:
        BinaryString = '0' + BinaryString
    return BinaryString


def ConvertToDecimal(BinaryString):
    """
    parameters: string
    description: converts binary to decimal
    return type: int
    """
    DecimalNumber = 0
    for Bit in BinaryString:
        BitValue = int(Bit)
        DecimalNumber = DecimalNumber * 2 + BitValue
    return DecimalNumber


def DisplayFrameDelimiter(FrameNumber):
    """
    parameters: int
    description: displays frame borders
    """
    if FrameNumber == -1:
        print("***************************************************************")
    else:
        print("****** Frame", FrameNumber, "************************************************")


def DisplayCurrentState(SourceCode, Memory, Registers):
    """
    parameters: array, array, array
    description: displays the source code along with the state of all registers
    """
    print("*")
    DisplayCode(SourceCode, Memory)
    print("*")
    print("*  PC: ", Registers[PC], " ACC: ", Registers[ACC], " TOS: ", Registers[TOS])
    print("*  Status Register: ZNV")
    print("*                  ", ConvertToBinary(Registers[STATUS]))
    DisplayFrameDelimiter(-1)


def SetFlags(Value, Registers):
    """
    parameters: int, array
    description: sets the value of the status register
    return type: array
    """
    if Value == 0:
        Registers[STATUS] = ConvertToDecimal("100")
    elif Value < 0:
        Registers[STATUS] = ConvertToDecimal("010")
    elif Value > MAX_INT or Value < -(MAX_INT + 1):
        Registers[STATUS] = ConvertToDecimal("001")
    else:
        Registers[STATUS] = ConvertToDecimal("000")
    return Registers


def ReportRunTimeError(ErrorMessage, Registers):
    """
    parameters: string, array
    description: displays error message and sets ERR register to 1
    return type: array
    """
    print("Run time error:", ErrorMessage)
    Registers[ERR] = 1
    return Registers


def ExecuteLDA(Memory, Registers, Address):
    """
    parameters: array, array, int
    description: executes LDA function
    return type: array
    """
    Registers[ACC] = Memory[Address].OperandValue
    Registers = SetFlags(Registers[ACC], Registers)
    return Registers


def ExecuteSTA(Memory, Registers, Address):
    """
    parameters: array, array, int
    description: executes STA function
    return type: array
    """
    Memory[Address].OperandValue = Registers[ACC]
    return Memory


def ExecuteLDAimm(Registers, Operand):
    """
    parameters: array, int
    description: executes immediate LDA function
    return type: array
    """
    Registers[ACC] = Operand
    Registers = SetFlags(Registers[ACC], Registers)
    return Registers


def ExecuteADD(Memory, Registers, Address):
    """
    parameters: array, array, int
    description: executes ADD function
    return type: array
    """
    Registers[ACC] = Registers[ACC] + Memory[Address].OperandValue
    Registers = SetFlags(Registers[ACC], Registers)
    if Registers[STATUS] == ConvertToDecimal("001"):
        ReportRunTimeError("Overflow", Registers)
    return Registers


def ExecuteSUB(Memory, Registers, Address):
    """
    parameters: array, array, int
    description: executes SUB function
    return type: array
    """
    Registers[ACC] = Registers[ACC] - Memory[Address].OperandValue
    Registers = SetFlags(Registers[ACC], Registers)
    if Registers[STATUS] == ConvertToDecimal("001"):
        ReportRunTimeError("Overflow", Registers)
    return Registers


def ExecuteCMPimm(Registers, Operand):
    """
    parameters: array, int
    description: executes immediate CMP function
    return type: array
    """
    Value = Registers[ACC] - Operand
    Registers = SetFlags(Value, Registers)
    return Registers


def ExecuteBEQ(Registers, Address):
    """
    parameters: array, int
    description: executes a BEQ function
    return type: array
    """
    StatusRegister = ConvertToBinary(Registers[STATUS])
    FlagZ = StatusRegister[0]
    if FlagZ == "1":
        Registers[PC] = Address
    return Registers


def ExecuteJMP(Registers, Address):
    """
    parameters: array, int
    description: sets the value of the PC register to the current address
    return type: array
    """
    Registers[PC] = Address
    return Registers


def ExecuteSKP():
    """
    description:
    """
    return


def DisplayStack(Memory, Registers):
    """
    parameters: array, array
    description: displays the contents of the stack
    return type:
    """
    print("Stack contents:")
    print(" ----")
    for Index in range(Registers[TOS], HI_MEM):
        print("|{:>3d} |".format(Memory[Index].OperandValue))
    print(" ----")


def ExecuteJSR(Memory, Registers, Address):
    """
    parameters: array, array, int
    description: executes the JSR function
    return type: array, array
    """
    StackPointer = Registers[TOS] - 1
    Memory[StackPointer].OperandValue = Registers[PC]
    Registers[PC] = Address
    Registers[TOS] = StackPointer
    DisplayStack(Memory, Registers)
    return Memory, Registers


def ExecuteRTN(Memory, Registers):
    """
    parameters: array, array
    description: executes RTN function
    return type: array
    """
    StackPointer = Registers[TOS]
    Registers[TOS] += 1
    Registers[PC] = Memory[StackPointer].OperandValue
    return Registers


def Execute(SourceCode, Memory):
    """
    parameters: array, array
    description: executes code
    """
    Registers = [0, 0, 0, 0, 0]
    Registers = SetFlags(Registers[ACC], Registers)
    Registers[PC] = 0
    Registers[TOS] = HI_MEM
    FrameNumber = 0
    DisplayFrameDelimiter(FrameNumber)
    DisplayCurrentState(SourceCode, Memory, Registers)
    OpCode = Memory[Registers[PC]].OpCode
    while OpCode != "HLT":
        FrameNumber += 1
        print()
        DisplayFrameDelimiter(FrameNumber)
        Operand = Memory[Registers[PC]].OperandValue
        print("*  Current Instruction Register: ", OpCode, Operand)
        Registers[PC] = Registers[PC] + 1
        if OpCode == "LDA":
            Registers = ExecuteLDA(Memory, Registers, Operand)
        elif OpCode == "STA":
            Memory = ExecuteSTA(Memory, Registers, Operand)
        elif OpCode == "LDA#":
            Registers = ExecuteLDAimm(Registers, Operand)
        elif OpCode == "ADD":
            Registers = ExecuteADD(Memory, Registers, Operand)
        elif OpCode == "JMP":
            Registers = ExecuteJMP(Registers, Operand)
        elif OpCode == "JSR":
            Memory, Registers = ExecuteJSR(Memory, Registers, Operand)
        elif OpCode == "CMP#":
            Registers = ExecuteCMPimm(Registers, Operand)
        elif OpCode == "BEQ":
            Registers = ExecuteBEQ(Registers, Operand)
        elif OpCode == "SUB":
            Registers = ExecuteSUB(Memory, Registers, Operand)
        elif OpCode == "SKP":
            ExecuteSKP()
        elif OpCode == "RTN":
            Registers = ExecuteRTN(Memory, Registers)
        if Registers[ERR] == 0:
            OpCode = Memory[Registers[PC]].OpCode
            DisplayCurrentState(SourceCode, Memory, Registers)
        else:
            OpCode = "HLT"
    print("Execution terminated")


def AssemblerSimulator():
    """
    description: main function
    """
    SourceCode = [EMPTY_STRING for Lines in range(HI_MEM)]
    Memory = [AssemblerInstruction() for Lines in range(HI_MEM)]
    SourceCode = ResetSourceCode(SourceCode)
    Memory = ResetMemory(Memory)
    Finished = False
    while not Finished:
        DisplayMenu()
        MenuOption = GetMenuOption()
        if MenuOption == 'L':
            SourceCode = LoadFile(SourceCode)
            Memory = ResetMemory(Memory)
        elif MenuOption == 'D':
            if SourceCode[0] == EMPTY_STRING:
                print("Error Code 7")
            else:
                DisplaySourceCode(SourceCode)
        elif MenuOption == 'E':
            if SourceCode[0] == EMPTY_STRING:
                print("Error Code 8")
            else:
                SourceCode = EditSourceCode(SourceCode)
                Memory = ResetMemory(Memory)
        elif MenuOption == 'A':
            if SourceCode[0] == EMPTY_STRING:
                print("Error Code 9")
            else:
                Memory = Assemble(SourceCode, Memory)
        elif MenuOption == 'R':
            if Memory[0].OperandValue == 0:
                print("Error Code 10")
            elif Memory[0].OpCode == "ERR":
                print("Error Code 11")
            else:
                Execute(SourceCode, Memory)
        elif MenuOption == 'X':
            Finished = True
        else:
            print("You did not choose a valid menu option. Try again")
    print("You have chosen to exit the program")


if __name__ == "__main__":
    AssemblerSimulator()
