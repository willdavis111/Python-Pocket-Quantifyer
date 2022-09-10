import Onewall, Fourwalls, footercalc

start_over = 'true'
while start_over == 'true':
    print("""
Enter '1' for benching one direction
Enter '2' for benching four direction
Enter '3' for footer calculator""")
    oper = input("Desired operation: ")
# benching in one direction
    if oper == "1":
        Onewall.funcOne()

#benching the surrounding area
    elif oper == "2":
        Fourwalls.funcTwo()

    elif oper == "3":
        footercalc.funcThree()

    redo_program = input('Enter RS to restart:')
    if redo_program.lower == 'rs':
        start_over = 'true'