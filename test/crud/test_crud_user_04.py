from .. import test_module

Crud = test_module.crud.Crud
EntityBase = test_module.schema.EntityBase
EntityFull = test_module.schema.EntityFull
UserBase = test_module.schema.UserBase
UserFull = test_module.schema.UserFull
UserFilter = test_module.schema.UserFilter

get_engine = test_module.engine.get_engine


def test_crud_user_01():
    """
    Test creating and deleting User.
    """
    crud = Crud(get_engine())

    user_base = UserBase(user_name="ulmer", name="Robert Ulmer", password_hash="secret")
    user = crud.create_user(user_base)

    assert user
    assert "Robert Ulmer" == user.name
    assert "ulmer" == user.user_name
    assert "secret" == user.password_hash

    assert 1 == len(crud.get_users())

    user.name = "Robert Felix Ulmer"
    crud.change_user(user)
    change_user =crud.get_users(UserFilter(id=user.id))
    assert len(change_user)==1
    assert change_user[0].name==user.name
