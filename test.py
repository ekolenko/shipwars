#!/usr/bin/python3

def order(sentence):
  # code here
    if sentence == '':
        return ''
    else:
        dict ={}
        lst = sentence.split()
        for elem in lst:
            for char in elem:
                if 30<ord(char)<40:
                    dict[char] = elem
                    break
                elif ord(char) == 30:
                    dict[':'] = elem
        return ' '.join([dict[key] for key in sorted(dict.keys())])

print(order("is2 Thi1s T4est 3a"))

