import pytest

from .. import test_module

Crud = test_module.crud.Crud
EntityBase = test_module.schema.EntityBase
EntityFull = test_module.schema.EntityFull
UserBase = test_module.schema.UserBase
UserFull = test_module.schema.UserFull

get_engine = test_module.engine.get_engine


def test_crud_user_01():
    """
    Test creating an entity, and then adding a new user to this entity
    """
    crud = Crud(get_engine())
    entity_base = EntityBase(name="Robert")
    entity = crud.create_entity(entity_base)

    assert entity.id

    user_base = UserBase(user_name="ulmer", name="", password_hash="secret")
    user = crud.create_user(user_base, entity)

    assert user
    assert user.id == entity.id
    assert "Robert" == user.name
    assert "ulmer" == user.user_name
    assert "secret" == user.password_hash


def test_crud_user_02():
    """
    Test creating user binding it to a non existent entity
    """
    crud = Crud(get_engine())
    entity_base = EntityBase(name="Robert")
    entity = crud.create_entity(entity_base)

    assert entity.id
    entity.id += 1

    with pytest.raises(AttributeError, match="Entity with id 2 does not exist!"):
        user_base = UserBase(user_name="ulmer", name="", password_hash="secret")
        _user = crud.create_user(user_base, entity)


def test_crud_user_03():
    """
    Test creating an entity, and then adding a new user to this entity
    Specially test, an overwriting of the name property in entity.
    """
    crud = Crud(get_engine())
    entity_base = EntityBase(name="robert")
    entity = crud.create_entity(entity_base)

    assert entity.id

    user_base = UserBase(user_name="ulmer", name="Robert Ulmer", password_hash="secret")
    user = crud.create_user(user_base, entity)

    assert user
    assert user.id == entity.id
    assert "Robert Ulmer" == user.name
    assert "ulmer" == user.user_name
    assert "secret" == user.password_hash
