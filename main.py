def main(array):
    answer = False
    if array[1] == '^':
        answer = array[0] and array[2]
    if array[1] == 'v':
        answer = array[0] or array[2]
    if array[1] == '~':
        answer = not array[0]
    print (answer)

if __name__ == "__main__":
    A = True
    B = False
    C = True
    array = [A, '^', B]
    main(array)