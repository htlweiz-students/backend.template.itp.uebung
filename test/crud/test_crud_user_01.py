from .. import test_module

Crud = test_module.crud.Crud
EntityBase = test_module.schema.EntityBase
EntityFull = test_module.schema.EntityFull
UserBase = test_module.schema.UserBase
UserFull = test_module.schema.UserFull
UserFilter = test_module.schema.UserFilter

get_engine = test_module.engine.get_engine

log = test_module.config.get_logger()

TEST_USER = [
    UserBase(user_name="root", name="Super administrator", password_hash=""),
    UserBase(user_name="admin", name="Local administrator", password_hash=""),
    UserBase(user_name="john", name="John Doe", password_hash=""),
    UserBase(user_name="jane", name="Jane Doe", password_hash=""),
    UserBase(user_name="jacob", name="Jacob Smith", password_hash=""),
]
count = 1
TEST_USER_FULL: list[UserFull] = []
for test_user in TEST_USER:
    test_user_full = UserFull(
        user_name=test_user.user_name,
        name=test_user.name,
        password_hash=test_user.password_hash,
        id=count,
    )
    TEST_USER_FULL.append(test_user_full)
    count += 1

TEST_USER_FILTER: list[tuple[UserFilter, list[UserFull]]] = [
    (UserFilter(user_name="%root"), [TEST_USER_FULL[0]]),
    (UserFilter(user_name="root", name="admin%"), []),
    (UserFilter(id=1), [TEST_USER_FULL[0]]),
    (UserFilter(user_name="j%", name="%Doe"), [TEST_USER_FULL[2], TEST_USER_FULL[3]]),
]


def test_crud_00():
    crud = Crud(get_engine())
    assert EntityBase
    assert crud


def test_crud_user_01():
    crud = Crud(get_engine())
    count = 0
    for user_base in TEST_USER:
        user = crud.create_user(user_base)
        assert TEST_USER_FULL[count] == user
        count += 1
    for filter, expected in TEST_USER_FILTER:
        result = crud.get_users(filter)
        log.debug(f"Check filter: {filter}")
        log.debug(f"Check expected: {expected}")
        log.debug(f"result: {result}")
        assert expected == result

