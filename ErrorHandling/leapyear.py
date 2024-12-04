def is_leap_year(year):

    if year<0:

        return False

    if (year % 4 == 0 and year % 100 != 0) or (year%100==0 and year % 400 == 0):

        return True
    
    else:

        return False
    
def test_is_leap_year():

    assert is_leap_year(2024)==True,"non century yr chck failed"

    assert is_leap_year(2025)==False,"invalid non centry chck failed"

    assert is_leap_year(2000)==True,"centry leap yr chck failed"

    assert is_leap_year(1900)==False,"invalid non centry yr chck failed"

    assert is_leap_year(-2024)==False,"invalid yr chck fatry"

try:

    test_is_leap_year()
    print("test case pass")

except Exception as e:

    print("test failed",e)