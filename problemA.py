# (c) 2025 Renz Leonard Sabando and Jadiel Peseral 
#  Cement Slurry Dilution

def main(): 
    
    v2 = float(input("Enter the value of  slurry (L): "))
    c1 = float(input("Enter the value of cement concentration 1 (g/L): "))
    c2 = float(input("Enter the value of cement concentration  (g/L): "))
     
    v1 = c2 * v2 / c1
     
    print(f"So, you need {v1:,.2f} liters of the original slurry. ")
     
   
	
if __name__ == "__main__": 
    main()