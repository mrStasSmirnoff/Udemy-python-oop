class InstanceCounter(object):
    cnt = 0

    def __init__(self, val):
        self.val = val
        InstanceCounter.cnt += 1

    def set_val(self, newval):
        self.val = newval

    def get_val(self):
        return self.val 

    def get_count(self):
        return InstanceCounter.cnt

a = InstanceCounter(5)
b = InstanceCounter(13)
c = InstanceCounter(17)

for obj in (a,b,c):
    print(f'val of obj: {obj.get_val()}')
    print(f'count: {obj.get_count()}')
    print(f'count from instance: {obj.cnt}')

