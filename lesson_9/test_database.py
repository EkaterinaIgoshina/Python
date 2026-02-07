from sqlalchemy import create_engine
from UserTable import UserTable

with open("pass.txt", "r") as file:
    connection_string = file.read()

db = create_engine(connection_string)
usbd = UserTable()

def test_insert_new():
    usbd = UserTable()
    usbd.get_tables()
    len_before = usbd.get_list()
    new_email = "igosh-ter@email.ru"
    usbd.insert_new({"new_user_email": new_email})
    len_after = usbd.get_list()
    assert len_after == len_before + 1
    assert new_email == "igosh-ter@email.ru"
    max_id = usbd.get_max_id()
    value_id = {"new_user_id": max_id + 1, "new_user_email": new_email}
    usbd.update_new(value_id)
    usbd.delete_new({"new_user_email": new_email})

















