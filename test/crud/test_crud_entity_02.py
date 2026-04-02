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
    assert len(crud.get_entities()) == 1
    crud.delete_entity(entity_full.id)
    assert len(crud.get_entities()) == 0


def test_crud_entity_02():
    TEST_ENTITY_NAME_01 = "John Doe"
    crud = Crud(get_engine())
    entity_base = EntityBase(name=TEST_ENTITY_NAME_01)
    entity_full = crud.create_entity(entity_base)
    assert entity_full.name == TEST_ENTITY_NAME_01
    assert entity_full.id

    TEST_ENTITY_NAME_02 = "Jane Doe"
    entity_base = EntityBase(name=TEST_ENTITY_NAME_02)
    entity_full = crud.create_entity(entity_base)
    assert type(entity_full) == EntityFull
    assert entity_full.id

    assert len(crud.get_entities()) == 2
    crud.delete_entity(entity_full.id)
    assert len(crud.get_entities()) == 1


def test_crud_entity_03() -> None:
    """Test if a deletion of a nonexistent entity, does raise correct error."""
    TEST_ENTITY_NAME_01 = "John Doe"
    crud: Crud = Crud(engine=get_engine())
    entity_base: EntityBase = EntityBase(name=TEST_ENTITY_NAME_01)
    entity_full: EntityFull = crud.create_entity(new_entity=entity_base)
    assert entity_full.id
    assert len(crud.get_entities()) == 1
    try:
        crud.delete_entity(entity_full.id + 1)
        assert None == "This should have raised an exception"
    except AttributeError as e:
        assert str(e) == f"No such Entity(id: {entity_full.id+1}, ...)!"
    except Exception as e:
        raise
