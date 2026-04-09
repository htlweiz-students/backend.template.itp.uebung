import re
import pytest
from .. import test_module

Crud = test_module.crud.Crud
EntityBase = test_module.schema.EntityBase
EntityFull = test_module.schema.EntityFull
EntityFilter = test_module.schema.EntityFilter

get_engine = test_module.engine.get_engine


def test_crud_00():
    crud = Crud(get_engine())
    assert EntityBase
    assert crud


def test_crud_entity_01():
    TEST_ENTITY_NAME = "John Doe"
    TEST_ENTITY_CHANGE_NAME = "Jane Doe"
    crud = Crud(get_engine())
    entity_base = EntityBase(name=TEST_ENTITY_NAME)
    entity_full = crud.create_entity(entity_base)
    assert type(entity_full) == EntityFull
    assert entity_full.id
    assert entity_full.name == TEST_ENTITY_NAME
    assert len(crud.get_entities()) == 1
    entity_full.name=TEST_ENTITY_CHANGE_NAME
    crud.change_entity(entity_full)
    filter=EntityFilter(id=entity_full.id)
    entity_check = crud.get_entities(filter)
    assert 1==len(entity_check)
    assert entity_full == entity_check[0]


def test_crud_entity_02():
    TEST_ENTITY_NAME = "John Doe"
    TEST_ENTITY_CHANGE_NAME = "Jane Doe"
    crud = Crud(get_engine())
    entity_base = EntityBase(name=TEST_ENTITY_NAME)
    entity_full = crud.create_entity(entity_base)
    assert type(entity_full) == EntityFull
    assert entity_full.id
    assert entity_full.name == TEST_ENTITY_NAME
    assert len(crud.get_entities()) == 1
    entity_full.name=TEST_ENTITY_CHANGE_NAME
    entity_full.id+=1
    with pytest.raises(AttributeError, match=re.escape("No such Entity(id: 2, ...)!")):
        crud.change_entity(entity_full)
