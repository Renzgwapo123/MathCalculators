# (c) 2025 Renz Leonard Sabando and Jadiel Peseral 
# Material Strength Calculation for Steel

def main(): 
    
    Fy = float(input("Enter the value of  force applied to the beam (N): "))
    A = float(input("Enter the value of cross sectional area (m): "))
     
    sigma = Fy / A
     
    print(f" So, the stress on the beam is {sigma:,.2f} Pa.  ")
     
   
	
if __name__ == "__main__": 
    main()