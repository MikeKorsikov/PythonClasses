# shelve allows working with files like with dictionary

import shelve

print('Importing and dumping data using "shelve":\n')
FILE_NAME = 'ch'
# c > w & r
with shelve.open(FILE_NAME) as f:
    f['id1'] = 'sdfs-eefcc'
    f['id2'] = 'grd-bhdtb'
    f['id3'] = 'tbdt-thth'

with shelve.open(FILE_NAME) as f:
    print(f['id1'])
    print(f['id2'])
    print(f['id3'])

with shelve.open(FILE_NAME) as f:
    key = f.get('id5', 'EMPTY')
    print(f'\nKey: {key}\n')

    for key, val in f.items():
        print(key, '>>>', val)