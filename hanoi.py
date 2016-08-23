#!py_env/bin/python
# python3

'''
Solver for the Tower of Hanoi

Created on Aug 7, 2016
'''

class Peg(object):
    def __init__(self, name, disks):
        self.name = name
        self.disks = disks[:]
    
    def pop(self):
        return self.disks.pop()
    
    def put(self, item):
        return self.disks.append(item)
    
    def get_name(self):
        return self.name
    
    def get_height(self):
        return len(self.disks)
    
    def get_state(self):
        return self.disks

class Disk(object):
    def __init__(self, size):
        self.size = size
    def get_size(self):
        return self.size

def move_tower(height, init_peg, dest_peg, aux_peg):
    if height >= 1:
        move_tower(height-1, init_peg, aux_peg, dest_peg)
        move_disk(init_peg, dest_peg)
        move_tower(height-1, aux_peg, dest_peg, init_peg)

def move_disk(ip, dp):
    print("moving disk from %s: %s to %s: %s" % (ip.get_name(), ip.get_state(), \
                                                 dp.get_name(), dp.get_state()))
    dp.put(ip.pop())

height = int(input("Number of disks: "))

init_peg = Peg("A", [height - x for x in range(height)])
dest_peg = Peg("B", [])
aux_peg = Peg("C", [])

move_tower(init_peg.get_height(), init_peg, dest_peg, aux_peg)

# TODO: draw images
tower_image = ["     |     ",
               "     |     ",
               "     |     ",
               "     |     ",
               "     |     ",
               "==========="]
for row in tower_image:
    print(row)
