# %%
flowerbed = [1,0,0,0,1,0,0,0]
my_list = [0]
my_list.extend(flowerbed)
my_list.append(0)
my_list

for i in range(1, len(my_list)-1):
    pass
    
def canPlaceFlowers(my_flowers: list[int], n: int) -> bool:
    my_list = [0]
    my_list.extend(my_flowers)
    my_list.append(0)
    for i in range(1, len(my_list) - 1):
        if my_list[i] == my_list[i-1] == my_list [i+1] == 0:
            my_list[i] = 1
            n -= 1
        if n == 0:
            return True
    return False

canPlaceFlowers(flowerbed, 4)
# %%
