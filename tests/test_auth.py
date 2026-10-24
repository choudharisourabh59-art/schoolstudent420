from services.auth_service import hash_password,verify_password
def test_password_hash():
    h=hash_password("correct-horse")
    assert verify_password("correct-horse",h)
    assert not verify_password("wrong",h)
