from byotest import *
cn = 20
eur_coins = {key : cn for key in [100,50,20,10,5,2,1]}
usd_coins = {key : cn for key in [100,50,25,10,5,2,1]}
def get_change(amount, coins = eur_coins):
    change = []
    coins_list = sorted(list(coins), reverse = True)
    for coin in coins_list:
        while coin <= amount:
            amount -= coin
            change.append(coin)
            
    return change

test_are_equal(get_change(0),[])
test_are_equal(get_change(1),[1])
test_are_equal(get_change(2),[2])
test_are_equal(get_change(3),[2,1])
test_are_equal(get_change(4),[2,2])
test_are_equal(get_change(9),[5,2,2])
test_are_equal(get_change(35, usd_coins),[25,10])
print("All tests passed")