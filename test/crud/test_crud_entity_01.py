from BACKEND_NAME_PLACEHOLDER.crud import Crud
from BACKEND_NAME_PLACEHOLDER.engine import get_engine
from BACKEND_NAME_PLACEHOLDER.schema import (EntityBase, EntityFilter,
                                             EntityFull)

NAME_01 = "Entity01"
NAME_02 = "Entity02"
NAME_03 = "EntityWithSearchString01"
NAME_04 = "EntityWithSearchString02"
NAME_05 = "EntityJohnDoe"

TEST_ENTITIES = [
    NAME_01,
    NAME_02,
    NAME_03,
    NAME_04,
    NAME_05,
]
TEST_FILTERS: list[EntityFilter] = [
    EntityFilter(name="Entity%", id=None),
    EntityFilter(name="%WithSearchString%", id=None),
    EntityFilter(name="%WithSearchString%", id=3),
    EntityFilter(name="%NotFound%", id=None),
    EntityFilter(name=None, id=1),
]
TEST_RESULTS: list[list[EntityFull]] = [
    [
        EntityFull(name=NAME_01, id=1),
        EntityFull(name=NAME_02, id=2),
        EntityFull(name=NAME_03, id=3),
        EntityFull(name=NAME_04, id=4),
        EntityFull(name=NAME_05, id=5),
    ],
    [
        EntityFull(name=NAME_03, id=3),
        EntityFull(name=NAME_04, id=4),
    ],
    [
        EntityFull(name=NAME_03, id=3),
    ],
    [],
    [
        EntityFull(name=NAME_01, id=1),
    ],
]


def test_crud_00():
    crud = Crud(get_engine())
    assert EntityBase
    assert crud


def test_crud_entity_search_with_filter():
    crud = Crud(get_engine())
    for test_entity in TEST_ENTITIES:
        entity_full = crud.create_entity(EntityBase(name=test_entity))
        assert entity_full.id
    assert len(TEST_FILTERS) == len(TEST_RESULTS)
    for filter_id in range(len(TEST_FILTERS)):
        result = crud.get_entities(TEST_FILTERS[filter_id])
        assert result == TEST_RESULTS[filter_id]
