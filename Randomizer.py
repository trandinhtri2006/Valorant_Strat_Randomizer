import random

# T side Strat
slow_fast = -1
split = -1
fake = -1
ending_a_b_c = -1

# CT side strat
take_control = -1

# T side
with open("Output.txt", "w", encoding="utf-8") as file:
    file.write("Attacker:\n")
    for i in range(12):
        # Round Number
        file.write(f"ROUND {i}: ")

        # Generating random strats
        slow_fast = random.randint(1,2)
        split = random.randint(1,2)
        fake = random.randint(1,3)
        ending_a_b_c = random.randint(1,3)


        # Fake or Real
        if fake % 2 == 0:
            file.write("Fake-")
        else:
            file.write("Real-")

        # Slow or Fast
        if slow_fast % 2 == 0:
            file.write("Fast-")
        else:
            file.write("Slow-")

        # Split or No Split
        if split % 2 == 0:
            file.write("Split-")
        else:
            file.write("Group-")

        # Ending A, B, C
        if ending_a_b_c % 3 == 0:
            file.write("Ending A\n")
        elif ending_a_b_c % 3 == 1:
            file.write("Ending B\n")
        else:
            file.write("Ending C\n")
        


        
    # CT side
    
