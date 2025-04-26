from securepasslib.breach_checker import BreachChecker

def test_hash_password():
    assert BreachChecker.hash_password("password123") == "CBFDAC6008F9cab4083784CBD1874F76618D2A97".upper()

def test_is_breached_safe_password():
    # This password is weak and almost certainly breached
    assert BreachChecker.is_breached("password123")
    
