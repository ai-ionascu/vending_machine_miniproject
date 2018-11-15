from byotest import *
coins_number = 5
eur_coins = {key : coins_number for key in [100,50,20,10,5,2,1]}
usd_coins = {key : coins_number for key in [100,50,25,10,5,2,1]}

def get_change(amount, coins = eur_coins):
    change = []
    coin_list = sorted(coins.items(),reverse = True)

    for coin, available in coin_list:
        while coin <= amount and available > 0:
            amount -= coin
            change.append(coin)
            available-=1
            
    if amount > 0:
        return "Error, you dont have enough change!"  
        
    return change

test_are_equal(get_change(0),[])
test_are_equal(get_change(1),[1])
test_are_equal(get_change(2),[2])
test_are_equal(get_change(3),[2,1])
test_are_equal(get_change(4),[2,2])
test_are_equal(get_change(9),[5,2,2])
test_are_equal(get_change(651),[100,100,100,100,100,50,50,50,1])
test_are_equal(get_change(899),[100,100,100,100,100,50,50,50,50,50,20,20,20,20,20,10,10,10,10,5,2,2])
test_are_equal(get_change(35, usd_coins),[25,10])
test_are_equal(get_change(3587),"Error, you dont have enough change!")
test_are_equal(get_change(941),"Error, you dont have enough change!")
print("All tests passed")