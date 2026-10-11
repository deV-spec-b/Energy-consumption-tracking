from objects import create_object, find_object_by_id, find_objects_by_address


def test_create_object() -> None:
    objects: list = []
    accounting_object = create_object(
        objects,
        "ул. Ленина, д. 10",
        "квартира",
        54.2
    )
    assert accounting_object["id"] == 1
    assert len(objects) == 1


def test_find_object_by_id() -> None:
    objects: list = []
    create_object(objects, "ул. Мира, д. 1", "офис", 80.0)
    found = find_object_by_id(objects, 1)
    assert found is not None
    assert found["address"] == "ул. Мира, д. 1"


def test_find_objects_by_address() -> None:
    objects: list = []
    create_object(objects, "ул. Ленина, д. 10", "квартира", 40.0)
    found = find_objects_by_address(objects, "ленина")
    assert len(found) == 1
