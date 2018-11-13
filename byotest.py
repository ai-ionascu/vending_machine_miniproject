def test_are_equal(a,e):
    assert e==a, "Expected {1} to be equal to {0}".format(a,e)
    
def test_are_not_equal(a,e):
    assert e!=a, "Did not expect {1} to be equal to {0}".format(a,e)
    
def test_is_in(collection,item):
    assert item in collection, "Expected {1} to be in {0}".format(collection,item)
    
def test_is_not_in(collection,item):
    assert item not in collection, "Did not expect {1} to be in {0}".format(collection,item)
    
def test_is_between(u,l,item):
    assert l<=item<=u, "{2} is not between {1} and {0}".format(u,l,item)