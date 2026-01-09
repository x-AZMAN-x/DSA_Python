def towerOfHanoi(num, from_rod, to_rod, aux_rod):
    if num == 0:
        return
    towerOfHanoi(num - 1, from_rod, to_rod, aux_rod)
    print("Move disk", num, "from rod" ,from_rod, "to rod", to_rod)
    towerOfHanoi(num - 1, from_rod, to_rod, aux_rod)

n = 3
towerOfHanoi(n, "A", "B", "C")