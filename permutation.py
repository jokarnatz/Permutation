from random import shuffle
from time import sleep
from sys import exit

def get_input(prompt, datatype):
    while True:
        try:
            value = datatype(input(prompt))
            return value
        except (ValueError, TypeError):
            print("Invalid input.")
        except KeyboardInterrupt:
            print("Exiting..")
            sleep(0.5)
            exit(0)
        except Exception as e:
            print(f"An error occurred: {e}")

def create_vars(usr_choice):
    p = [1,2,3,4,5,6,7,8,9]
    a, b, c, d, e, f, g, h, i = p
    var: list = [a,b,c,d,e,f,g,h,i]
    TARGET_VALUE: int = usr_choice
    MAX_COUNTS = 300_000
    return var, TARGET_VALUE, MAX_COUNTS

def calculate_expression(var: list):
    return var[0] + 13 * var[1] / var[2] + var[3] / 12 * var[4] - var[5] - 11 / var[6] * var[7] / var[8] - 10

def calculate_permutation(var: list, TARGET_VALUE: int, MAX_COUNTS):
    count = 0
    while True:
        shuffle(var)
        count += 1
        mathm_expression = calculate_expression(var)
        print(f"Testing {count}. permutation variation on expression.")
        if MAX_COUNTS == count:
            print(f"Reached maximum calculations without result.\nExiting..")  
            break
        elif mathm_expression == TARGET_VALUE:
            print(f"Found a fitting variation in run {count}:\n{' '.join(map(str,var))}")
            print(f"{mathm_expression:g}")
            break
            
                
if __name__ == '__main__':
    usr_choice = get_input("Choose a result number. Should be a small number: ", int)
    var, TARGET_VALUE, MAX_COUNTS = create_vars(usr_choice)
    calculate_permutation(var, TARGET_VALUE, MAX_COUNTS)