from sqlalchemy import create_engine
from UpdatingPage import Updating

with open("pass.txt", "r") as file:
    connection_string = file.read()

db = create_engine(connection_string)
usbd = Updating()


def test_insert_new():
    usbd = Updating()
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
    new_email = "KMZ@yandex.ru"
    usbd.delete_new({"new_user_email": new_email})

def test_update_email():
    usbd = Updating()
    usbd.get_tables()
    old_email = "igosh-ter@email.ru"
    new_email = "KMZ@yandex.ru"
    usbd.insert_new({"new_user_email": old_email})
    assert old_email in [row['user_email'] for row in usbd.get_list()]
    usbd.update_email(old_email, new_email)
    assert new_email in [row['user_email'] for row in usbd.get_list()]
    assert old_email not in [row['user_email'] for row in usbd.get_list()]
    usbd.delete_new({"new_user_email": new_email})


