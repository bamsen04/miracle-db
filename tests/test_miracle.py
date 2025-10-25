from miracle_db import insert, get_data

def test_insertion():
    assert insert("data") is None

def test_retrieval():
    assert get_data() is None
