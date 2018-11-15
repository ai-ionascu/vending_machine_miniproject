from byotest import *
eur_coins = {100:20,50:20,20:20,10:20,5:20,2:20,1:20}
usd_coins = {100:20,50:20,25:20,10:20,5:20,2:20,1:20}
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