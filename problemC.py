# (c) 2025 Renz Leonard Sabando and Jadiel Peseral 
#  Concrete Volume Calculation

def main(): 
    
    L = float(input("Enter the value of length (m): "))
    W = float(input("Enter the value of width (m): "))
    D = float(input("Enter the value of depth (m): "))
     
    V = L * W * D
     
    print(f"So, you need {V:,.2f} cubic meters of concrete.  ")
     
   
	
if __name__ == "__main__": 
    main()