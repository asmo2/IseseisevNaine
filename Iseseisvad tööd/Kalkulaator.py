class Calculator:   
    def liida(self, a, b):  
        return a + b      

    def lahuta(self, a, b):   
        return a - b          

    def korruta(self, a, b):  
        return a * b          

    def jaga(self, a, b):  
        return a / b      

mu_kalku = Calculator() 

while True: 
    print("1: Liitmine")
    print("2: Lahutamine")
    print("3: Korrutamine")
    print("4: Jagamine")
    print("5: Cancel")

    ch = int(input("valige toiming: "))
    
  
    if ch in (1, 2, 3, 4, 5):
        

        if(ch == 5):
            break   
           
        a = int(input("Sisetage esimene arv: "))
        b = int(input("Sisestage teine arv: "))
        
        if(ch == 1): 
            print(a, "+", b, "=", mu_kalku.liida(a, b))
        elif(ch == 2): 
            print(a, "-", b, "=", mu_kalku.lahuta(a, b)) 
        elif(ch == 3): 
            print(a, "*", b, "=", mu_kalku.korruta(a, b)) 
        elif(ch == 4): 
            print(a, "/", b, "=", mu_kalku.jaga(a, b)) 
    
    else: 
        print("Vigane sisestus") 