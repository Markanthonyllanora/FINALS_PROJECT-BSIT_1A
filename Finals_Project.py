from Activity1 import act1
from Activity2 import act2
from Activity3 import act3
from Activity4 import act4
from Activity5 import act5
from Activity6 import act6
from Activity7 import act7
from Activity8 import act8
from Activity9 import act9
from Activity10 import act10
from Activity11 import act11
from Activity12 import act12
from Activity13 import act13
from Activity14 import act14
from Activity15 import act15
from Activity16 import act16
from Activity17 import act17
from Activity18 import act18
from Activity19 import act19
from Activity20 import act20
from Activity21 import act21
from Activity22 import act22
from Activity23 import act23
from Activity24 import act24
from Activity25 import act25
from CodeChallenge1 import cc1
from CodeChallenge2 import cc2
from CodeChallenge3 import cc3
from CodeChallenge4 import cc4
from CodeChallenge5 import cc5
from CodeChallenge6 import cc6
from CodeChallenge7 import cc7
from CodeChallenge8 import cc8
from CodeChallenge9 import cc9
from CodeChallenge10 import cc10
from CodeChallenge11 import cc11
from CodeChallenge12 import cc12
from CodeChallenge13 import cc13
from CodeChallenge14 import cc14
from CodeChallenge15 import cc15
from CodeChallenge16 import cc16
import os

def main():
    while True:
        print("Choose what you want:")
        print("A. Activity (1-25)")
        print("B. Code Challenge (1-16)")
        print("C. Exit")
        
        
        choice = input("Choose letter (A/B/C): ")

        if choice.lower() == "a":  
            act_choice = input("Choose activity number (1-25): ")
            
            if act_choice == '1': act1()
            elif act_choice == '2': act2()
            elif act_choice == '3': act3()
            elif act_choice == '4': act4()
            elif act_choice == '5': act5()
            elif act_choice == '6': act6()
            elif act_choice == '7': act7()
            elif act_choice == '8': act8()
            elif act_choice == '9': act9()
            elif act_choice == '10': act10()
            elif act_choice == '11': act11()
            elif act_choice == '12': act12()
            elif act_choice == '13': act13()
            elif act_choice == '14': act14()
            elif act_choice == '15': act15()
            elif act_choice == '16': act16()
            elif act_choice == '17': act17()
            elif act_choice == '18': act18()
            elif act_choice == '19': act19()
            elif act_choice == '20': act20()
            elif act_choice == '21': act21()
            elif act_choice == '22': act22()
            elif act_choice == '23': act23()
            elif act_choice == '24': act24()
            elif act_choice == '25': act25()
            else:
                print("Invalid number. Choose correct activity number (1-25).")
                
        elif choice.lower() == "b":  
            cc_choice = input("Choose Code Challenge number (1-16): ")
            
            if cc_choice == '1': cc1()
            elif cc_choice == '2': cc2()
            elif cc_choice == '3': cc3()
            elif cc_choice == '4': cc4()
            elif cc_choice == '5': cc5()
            elif cc_choice == '6': cc6()
            elif cc_choice == '7': cc7()
            elif cc_choice == '8': cc8()
            elif cc_choice == '9': cc9()
            elif cc_choice == '10': cc10()
            elif cc_choice == '11': cc11()
            elif cc_choice == '12': cc12()
            elif cc_choice == '13': cc13()
            elif cc_choice == '14': cc14()
            elif cc_choice == '15': cc15()
            elif cc_choice == '16': cc16()
            else:
                print("Invalid number. Choose correct Code Challenge number (1-16).")
                
        elif choice.lower() == "c":  
            print("Program terminated.")
            break
        
        else:
            print("Invalid choice. choose ulit.")


        input("Press Enter to continue...")

       
        os.system("cls")

main()

