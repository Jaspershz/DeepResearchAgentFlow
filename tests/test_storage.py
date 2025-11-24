from app.storage import InMemoryStorage

memStorage = InMemoryStorage()


def test_storage_save():
    memStorage.save(key="01", value={"chat_id": "01", "msg": "hello world"})


def test_load_storage():
    mem = memStorage.load(key="01")
    assert mem["chat_id"] == "01"
    assert mem["msg"] == "hello world"
