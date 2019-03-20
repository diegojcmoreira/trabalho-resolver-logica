A = True
B = False
C = False

def main():
    logic = input('Digite a logica: ')
    logic = str.replace(logic, "v", " or ")
    logic = str.replace(logic, "^", " and ")
    logic = str.replace(logic, "~", " not ")
    return eval(logic)

if __name__ == "__main__":
    print(main())
