# (c) 2025 Renz Leonard Sabando and Jadiel Peseral 
#  Slope of a Road

def main():
    
    rise = float(input("Enter the value of rise (m): "))
    run = float(input("Enter the value of horizontal distance (m): "))
    
    S = (rise / run) * 100
     
    print(f"So, the slope of the road is {S} %.  ")
     
   
	
if __name__ == "__main__": 
    main()