#!/usr/bin/python3

def gen_field(str_in):
    list_1 =  [step.split(' ') for step in str_in.split(':')]
    print(list_1)
    return list_1

gen_field('12:12 13 1 4:43 45:23 45 56 67:23 21:56 78 94')