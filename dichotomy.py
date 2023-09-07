print("Dichotomy paradox")
def dichotomy_paradox(d_tree):
    d_rock = 0
    step = d_tree / 2
    while True:
        d_rock += step 
        print('')
        print(f"Position of the rock: {d_rock}")
        print(f"Distance for the step: {step}")
        step /= 2
        if d_rock == d_tree:
            print("The rock reaches the tree !")
            break
dichotomy_paradox(8)

