from models.objects import (
    create_object,
    find_object_by_id,
    find_objects_by_address,
    sort_objects_by_area
)


def test_create_object() -> None:
    objects: list = []
    accounting_object = create_object(
        objects,
        "ул. Ленина, д. 10, кв. 15",
        "квартира",
        54.2
    )
    assert len(objects) == 1
    assert accounting_object.id == 1
    assert accounting_object.address == "ул. Ленина, д. 10, кв. 15"
    assert accounting_object.object_type == "квартира"


def test_find_object_by_id() -> None:
    objects: list = []
    create_object(objects, "ул. Мира, д. 1", "офис", 80.0)
    accounting_object = find_object_by_id(objects, 1)
    assert accounting_object is not None
    assert accounting_object.address == "ул. Мира, д. 1"


def test_object_not_found() -> None:
    objects: list = []
    assert find_object_by_id(objects, 10) is None


def test_find_objects_by_address() -> None:
    objects: list = []
    create_object(objects, "ул. Ленина, д. 10", "квартира", 40.0)
    create_object(objects, "ул. Гагарина, д. 5", "офис", 90.0)
    found = find_objects_by_address(objects, "ленина")
    assert len(found) == 1


def test_sort_objects_by_area() -> None:
    objects: list = []
    create_object(objects, "A", "квартира", 70.0)
    create_object(objects, "B", "квартира", 40.0)
    sorted_objects = sort_objects_by_area(objects)
    assert sorted_objects[0].area == 40.0
    assert sorted_objects[1].area == 70.0
