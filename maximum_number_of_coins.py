class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        ##NaolJK
        if len(piles)%3 != 0:
            return 
        piles.sort()
        number_of_picked_coins = 0
        number_of_max_coins = 0
        for i in range (len(piles)-2,0 ,-2):
            number_of_max_coins+=piles[i]
            print(piles[i])
            number_of_picked_coins+=1
            if number_of_picked_coins == len(piles)/3:
                break
        return number_of_max_coins
        

            
            
        