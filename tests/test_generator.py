from securepasslib.generator import PasswordGenerator

def test_generate_random_password():
    generator = PasswordGenerator()
    pwd = generator.generate_random_password(length=10)
    assert len(pwd) == 10

def test_generate_by_template_simple():
    generator = PasswordGenerator()
    pwd = generator.generate_by_template("simple")
    assert len(pwd) == 8  # LLLLDDDD (4 letters + 4 digits)

def test_generate_by_template_easy_remember():
    generator = PasswordGenerator()
    pwd = generator.generate_by_template("easy_remember")
    assert "-" in pwd


def test_generate_by_custom_template():
    generator = PasswordGenerator()
    pwd = generator.generate_by_template(custom_template="LL-DD-SS")
    print("pwd",pwd)
    assert "-" in pwd
    assert len(pwd.replace("-", "")) == 6  # 6 random characters, 2 per group
