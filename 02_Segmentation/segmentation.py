import sys
import re

line = sys.stdin.readline()

irabb = ['.i.', 'm.sh.', 'srl.', 'Br.']

while line:
    for token in line.strip().split(' '):
        if not token:
            continue
        if token[-1] in '!?':
            sys.stdout.write(token + '\n')
        elif token[-1] == '.':
            cleantoken = token.strip('()')
            if cleantoken in ['etc.', 'i.e.', 'e.g.', 'a.m.', 'p.m.']:
                sys.stdout.write(token + ' ')
            elif cleantoken in irabb:
                sys.stdout.write(token + ' ')
            elif re.match('[0-9a-zA-ZÁÉÍÓÚáéíóú]\.', token):
                sys.stdout.write(token + ' ')
            else:
                sys.stdout.write(token + '\n')
        else:
            sys.stdout.write(token + ' ')
            
    line = sys.stdin.readline()