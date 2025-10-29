from random import shuffle

def create_vars():
    p = [1,2,3,4,5,6,7,8,9]
    a, b, c, d, e, f, g, h, i = p
    var: list = [a,b,c,d,e,f,g,h,i]
    TARGET_VALUE: int = 66
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
            print(f"Reached maximum calculations: {count}\nExiting..")  
            break
        elif mathm_expression == TARGET_VALUE:
            print(f"Found a fitting variation in run {count}:\n{' '.join(map(str,var))}")
            print(f"{mathm_expression:g}")
            break
            
                
if __name__ == '__main__':
    var, TARGET_VALUE, MAX_COUNTS = create_vars()
    calculate_permutation(var, TARGET_VALUE, MAX_COUNTS)