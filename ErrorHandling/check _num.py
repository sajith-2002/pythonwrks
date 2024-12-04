def checknum(num):

    if num>0:

        return "+ve"
    
    elif num<0:

        return "-ve"
    
    elif num==0:

        return "0"
    
def test_checknum():

    assert checknum(10)=="+ve","+ve num chck failed"

    assert checknum(-10)=="-ve","-ve num chck failed"

    assert checknum(10)=="0","0 num chck failed"

test_checknum()
