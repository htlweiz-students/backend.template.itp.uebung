from BACKEND_NAME_PLACEHOLDER.schema import (EntityBase, EntityFilter,
                                             EntityFull)


def test_entity_00():
    entity_base = EntityBase(name="Ulmer")

    entity_base_copy: EntityBase = eval(  #  pyright: ignore [reportAny]
        repr(entity_base)
    )
    assert entity_base_copy.name == entity_base.name

    entity: EntityFull = EntityFull(id=1, name="Fritz")

    entity_copy: EntityFull = eval(repr(entity))  #  pyright: ignore [reportAny]

    assert entity_copy == entity


def test_entity_01():
    entity_filter = EntityFilter(name="%search_string%", id=1)
    entity_filter_copy = eval(repr(entity_filter))  # pyright: ignore [reportAny]
    assert entity_filter_copy == entity_filter

    entity_filter = EntityFilter(name=None, id=1)
    entity_filter_copy = eval(repr(entity_filter))  # pyright: ignore [reportAny]
    assert entity_filter_copy == entity_filter

    entity_filter = EntityFilter(name="%search_string%", id=None)
    entity_filter_copy = eval(repr(entity_filter))  # pyright: ignore [reportAny]
    assert entity_filter_copy == entity_filter


def test_fail():
    assert True
