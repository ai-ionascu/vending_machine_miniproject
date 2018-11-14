'''
def even_number_of_evens(list):
    return 0
'''

def test_are_equal(a,e):
    assert e==a, "Expected {1} but got {0}".format(a,e)
    
def test_are_not_equal(a,e):
    assert e!=a, "Did not expect {1} but got {0}".format(a,e)
    
def test_is_in(collection,item):
    assert item in collection, "Expected {1} to be in {0}".format(collection,item)
    
def test_is_not_in(collection,item):
    assert item not in collection, "Did not expect {1} to be in {0}".format(collection,item)
    
def test_is_between(u,l,item):
    assert l<=item<=u, "{2} is not between {1} and {0}".format(u,l,item)
    
#test_are_equal(1,even_number_of_evens([2,4,6]))
#test_are_not_equal(even_number_of_evens([]),0)
#test_is_in([1,2,3],5)
#test_is_not_in([1,2,3,4,5],2)
#test_is_between(10,1,25)
#print("All tests passed")
