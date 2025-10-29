from random import shuffle

a, b, c, d, e, f, g, h, i = 0, 0, 1, 0, 0, 0, 1, 0, 1

num_list: list = [1,2,3,4,5,6,7,8,9]
var: list = [a,b,c,d,e,f,g,h,i]
mathm_expression = var[0] + 13 * var[1] / var[2] + var[3] / 12 * var[4] - var[5] - 11 / var[6] * var[7] / var[8] - 10

while mathm_expression != 66:
    count = 0
    shuffle(num_list)
    for j in num_list:
        for k in var:
            var[k - 1] = j
            if mathm_expression != 66:
                count += 1
                print(f"{count}: Testing number variation on expression.")
            else:
                print(f"Found a fitting variation:\n{num_list}")
                print(eval(mathm_expression))
                break