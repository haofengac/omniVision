from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir('data') if isfile(join('data', f))]
print onlyfiles


ll = range(10)

print [k for k in ll if k != 1]