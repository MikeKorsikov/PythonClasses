from person import Person, Manager  # Load our classes
import shelve
import glob

bob = Person('Bob Smith')  # Re-create objects to be stored
sue = Person('Sue Jones', job='dev', pay=100000)
tom = Manager('Tom Jones', 50000)

db = shelve.open('persondb')  # Filename where objects are stored
for obj in (bob, sue, tom):  # Use object's name attr as key
    db[obj.name] = obj  # Store object on shelve by key
db.close()  # Close after making changes

print(glob.glob('person*'))

db = shelve.open('persondb')
print(len(db))
print(list(db.keys()))

bob = db['Bob Smith']
print(bob)
print(bob.lastName())

for key in db:  # Iterate, fetch, print
    print(key, '=>', db[key])
