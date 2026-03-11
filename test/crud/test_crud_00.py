from BACKEND_NAME_PLACEHOLDER.crud import Crud
from BACKEND_NAME_PLACEHOLDER.engine import get_engine
from BACKEND_NAME_PLACEHOLDER.schema import EntityBase, UserBase, UserFull


def test_crud_00():
    crud = Crud(get_engine())
    assert EntityBase
    assert crud


def test_crud_01():
    TEST_USER_USERNAME="test_user_00"
    TEST_USER_NAME="John Doe"
    TEST_USER_PASS="hashed_secret"
    crud = Crud(get_engine())
    assert EntityBase
    assert crud
    user_base = UserBase(user_name=TEST_USER_USERNAME, name=TEST_USER_NAME, password_hash=TEST_USER_PASS) 
    full_user= crud.create_user(user_base)
    assert type(full_user)==UserFull
    assert full_user.id
    assert full_user.user_name == TEST_USER_USERNAME
    assert full_user.password_hash == TEST_USER_PASS
    assert full_user.name == TEST_USER_NAME


def test_crud_02():
    return
