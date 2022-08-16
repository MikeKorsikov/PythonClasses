# CLASSES share behaviour (methods) and state (attributes)
# behaviour == methods == functions
# state == attributes == variables

class CountFromBy:
    # dunders are class __methods__ to modify object's default behaviour (?)
    def __init__(self, v: int = 0, i: int = 1) -> None:
        self.val = v
        self.incr = i

    def increase(self) -> None:
        self.val += self.incr

    def __repr__(self) -> str:
        return str(self.val)


h = CountFromBy(100, 10)
print('Object:', h)
print('Type of object:', type(h))
print('Object ID:', id(h))
print('Object hex:', hex(id(h)))

print('\nValue is:', h.val)
print('Increment by:', h.incr)



h.increase()

print('\nValue after calling increase() is:', h.val)
