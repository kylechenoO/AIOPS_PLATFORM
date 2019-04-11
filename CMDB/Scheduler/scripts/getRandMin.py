import os
from random import randint

workpath = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
file_name = '{}/scheduls/asset'.format(workpath)
with open(file_name, 'r') as fp:
    data = fp.read()

data = data.split('\n')
data.remove('')
data_new = []
for line in data:
    if line.find('Asset.py') > -1:
        print(line)
        task = line.split(' ')
        print(task)
        task[0] = str(randint(0, 59))
        line = ' '.join(task)

    data_new.append('{}\n'.format(line))

with open(file_name, 'w') as fp:
    fp.write(''.join(data_new))
