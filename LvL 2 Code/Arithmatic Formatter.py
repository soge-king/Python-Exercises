import re
# this is an import for regular expressions, we will use that to recognize patterns within the strings

def arithmetic_arranger(problems, resuelve=False):\
# this is the function class the will recognize, analyze and format the input problems

# some of the vars and errors were in spanish (native tongue), but was switched to english due to the format fo the test
    if len(problems) > 5:
    # Error 1, if the problem has too many numbers, we return with this
    return "Error: Too many problems."
# here are the vars that will hold the first number, second and the line seperating it. 
# because they are placeholders they are assigned an empty string
# suma is just sum in spanish
    primero = ""
    segundo = ""
    rallas = ""
    suma = ""

#this section will avoid the error of placing symbols instead of digits
    for problem in problems:
        if re.search("[^\s0-9.+-]", problem):
            if re.search("[/]", problem) or re.search("[*]", problem):
                return "Error: Operator must be '+' or '-'."
# only + and - is needed for this test so any other operator will trigger an error
            return "Error: Numbers must only contain digits."
#this will ensure we only use numbers


        primerNum = problem.split()[0]
        operador = problem.split()[1]
        segundoNum = problem.split()[2]
# here we split the string
        if len(primerNum) > 4 or len(segundoNum) > 4:
            return "Error: Numbers cannot be more than four digits."
#this line is to reduce the complexity of the functions



        if operador == "+":
            resultado = str(int(primerNum) + int(segundoNum))
        elif operador == "-":
            resultado = str(int(primerNum) - int(segundoNum))
# this is the section where the functions are executed, i.e. where the math, maths
        largo = max(len(primerNum), len(segundoNum)) + 2
        arriba = primerNum.rjust(largo)
        abajo = operador + segundoNum.rjust(largo - 1)
        ralla = "-" * largo
        res = resultado.rjust(largo)
#formatting of the equation

        if problem != problems[-1]:
            espacio = '    '
            primero += arriba + espacio
            segundo += abajo + espacio
            rallas += ralla + espacio
            suma += res + espacio
        else:
            primero += arriba
            segundo += abajo
            rallas += ralla
            suma += res
# we ensure the output is formatted
    if resuelve:
        arranged_problems = primero + "\n" + segundo + "\n" + rallas + "\n" + suma
    else:
        arranged_problems = primero + "\n" + segundo + "\n" + rallas
# here the solution is arranged
    return arranged_problems
#prints result


# Test cases
print(arithmetic_arranger(["3801 - 2", "123 + 49"]))
print(arithmetic_arranger(["1 + 2", "1 - 9380"]))
print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]))
print(arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["3 + 855", "988 + 40"], True))
print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True))
