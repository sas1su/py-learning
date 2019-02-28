class LogicGate:
    #define the label for identification
    def __init__(self, n):
        self.label = n
        self.output = None
    # additionaly we need to ask for label
    def getLabel(self):
        return self.label
    # single output line
    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

'''LogicGates are of two type 
BinaryGate (two input line) , subclass of LogicGate
UnaryGate (single input line), subclass of LogicGate'''
class BinaryGate(LogicGate):
    def __init__(self, n):
        LogicGate.__init__(self, n)

        self.pinA = None
        self.pinB = None
    
    def getPinA(self):
        return int(input("Enter pin A input for "+ self.getLabel() +"-->"))

    def getPinB(self):
        return int(input("Enter pin B input for "+ self.getLabel() +"-->"))

class UnaryGate(LogicGate):
    def __init__(self, n):
        LogicGate.__init__(self, n)

        self.pin = None
    
    def getPin(self):
        return int(input("Enter pin input for "+ self.getLabel() +"-->"))

'''gatelogic need to be with each gateclass
this need input which inherit from BinaryGate or UnaryGate
label and output inherit from LogicGate class'''
class AndGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):
        pinA = self.getPinA()
        pinB = self.getPinB()

        if pinA == 1 and pinB == 1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):
        pinA = self.getPinA()
        pinB = self.getPinB()

        if pinA == 1 or pinB ==1:
            return 1
        else:
            return 0

class NotGate(UnaryGate):
    def __init__(self, n):
        UnaryGate.__init__(self, n)

    def performGateLogic(self):
        pin = self.getPin()

        if pin == 0:
            return 1
        else:
            return 0

def main():
    #g1 = AndGate("G1")
    #print(g1.getOutput())

    #g2 = OrGate('G2')
    #print(g2.getOutput())

    g3 = NotGate("G3")
    print(g3.getOutput())
main()
