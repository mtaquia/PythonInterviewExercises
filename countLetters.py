def countLetters(chain):
    '''https://www.linkedin.com/groups/25827/25827-6166706414627627011
    countLetters('aaaaabbbbccccccaaaaaaa') -> 5a4b6c7a '''
    result = ''
    cont = 1
    previous = ''
    for char in chain:
        if previous == '':
            previous = char
        elif char == previous:
            cont += 1
        else:
            result += str(cont) + previous
            cont = 1
            previous = char
    result += str(cont) + char 
    return result

print(countLetters('aaaaabbbbccccccaaaaaaa'))
