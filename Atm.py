class Atm(object):
    def __init__(self, pin, cardNum, amountDrawn ):
        self.pin = pin
        self.cardNum = cardNum
        self.amountDrawn = amountDrawn

    def access(self):
        print("accepted")
    
    def dispensing(self):
        print("yes")
    
    
icici = Atm("9044", "1739460946446859", "5000 rupees")

print(icici.cardNum)

icici.access()
icici.dispensing()