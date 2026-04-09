from .. import test_module

Crud = test_module.crud.Crud
EntityBase = test_module.schema.EntityBase
EntityFull = test_module.schema.EntityFull
UserBase = test_module.schema.UserBase
UserFull = test_module.schema.UserFull

get_engine = test_module.engine.get_engine


def test_crud_00():
    crud = Crud(get_engine())
    assert EntityBase
    assert crud


def test_crud_user_01():
    TEST_USER_USERNAME = "test_user_00"
    TEST_USER_NAME = "John Doe"
    TEST_USER_PASS = "hashed_secret"
    crud = Crud(get_engine())
    assert EntityBase
    assert crud
    user_base = UserBase(
        user_name=TEST_USER_USERNAME, name=TEST_USER_NAME, password_hash=TEST_USER_PASS
    )
    full_user = crud.create_user(user_base)
    assert type(full_user) == UserFull
    assert full_user.id
    assert full_user.user_name == TEST_USER_USERNAME
    assert full_user.password_hash == TEST_USER_PASS
    assert full_user.name == TEST_USER_NAME


def test_crud_user_02():
    TEST_USER_USERNAME = "test_user_00"
    TEST_USER_NAME = "John Doe"
    TEST_USER_PASS = "hashed_secret"

    crud = Crud(get_engine())
    user_base = UserBase(
        user_name=TEST_USER_USERNAME, name=TEST_USER_NAME, password_hash=TEST_USER_PASS
    )
    full_user = crud.create_user(user_base)
    assert type(full_user) == UserFull
    assert full_user.id
    id = full_user.id
    assert full_user.user_name == TEST_USER_USERNAME
    assert full_user.password_hash == TEST_USER_PASS
    assert full_user.name == TEST_USER_NAME

    all_users = crud.get_users()
    assert len(all_users) == 1
    full_user = all_users[0]
    assert full_user.id == id
    assert full_user.user_name == TEST_USER_USERNAME
    assert full_user.password_hash == TEST_USER_PASS
    assert full_user.name == TEST_USER_NAME
