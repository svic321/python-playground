class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        for i,j in enumerate(flowerbed):
            if (
                j == 0
                and (i == 0 or flowerbed[i-1] == 0)
                and (i == len(flowerbed)-1 or flowerbed[i+1] == 0 )
            ):
                flowerbed[i] = 1
                n -= 1
            if n <= 0:
                return True
        return False

    def canPlaceFlowers_1(self, flowerbed: list[int], n: int) -> bool:
        if not n:
            return True

        flowerbed = [0] + flowerbed + [0]

        for idx in range(1, len(flowerbed) - 1):
            if flowerbed[idx] == flowerbed[idx - 1] == flowerbed[idx + 1] == 0:
                flowerbed[idx] = 1
                n -= 1

            if n == 0:
                return True

        return False

    def canPlaceFlowers_2(self, my_flowers: list[int], n: int) -> bool:
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