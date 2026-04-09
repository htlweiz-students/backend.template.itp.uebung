from .. import test_module

Crud = test_module.crud.Crud
EntityBase = test_module.schema.EntityBase
EntityFull = test_module.schema.EntityFull

get_engine = test_module.engine.get_engine


def test_crud_00():
    crud = Crud(get_engine())
    assert EntityBase
    assert crud


def test_crud_entity_01():
    TEST_ENTITY_NAME = "John Doe"
    crud = Crud(get_engine())
    entity_base = EntityBase(name=TEST_ENTITY_NAME)
    entity_full = crud.create_entity(entity_base)
    assert type(entity_full) == EntityFull
    assert entity_full.id
    assert entity_full.name == TEST_ENTITY_NAME


def test_crud_entity_02():
    TEST_ENTITY_NAME = "John Doe"
    crud = Crud(get_engine())
    entity_base = EntityBase(name=TEST_ENTITY_NAME)
    entity_full = crud.create_entity(entity_base)
    assert type(entity_full) == EntityFull
    assert entity_full.id
    id = entity_full.id
    assert entity_full.name == TEST_ENTITY_NAME
    full_enties = crud.get_entities()
    assert len(full_enties) == 1
    full_entity = full_enties[0]
    assert full_entity.id == id
    assert TEST_ENTITY_NAME == full_entity.name
