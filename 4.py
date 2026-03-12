while True:
    
    a = float(input("Unesi prvi broj: "))
    b = float(input("Unesi drugi broj: "))

    if b==0:
        print("Zbroj je ", a+b)
        print("Razlika je ",a-b)
        print("Umnozak je ", a*b)
        print("Nije moguce dijeljenje s nulom!")
    else:    
        print("Zbroj je ", a+b)
        print("Razlika je ",a-b)
        print("Umnozak je ", a*b)
        print("Kolicnik je ", a/b)
    
    opet = input("Zelis li opet unijeti?(da/ne)")
    if opet == "ne":
        break


