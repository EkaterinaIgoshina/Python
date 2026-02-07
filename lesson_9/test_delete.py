from sqlalchemy import create_engine
from SubjectTable import SubjectTable

with open("pass.txt", "r") as file:
    connection_string = file.read()

    db = create_engine(connection_string)
    usbd = SubjectTable()


def test_insert_and_delete_subject():
    usbd = SubjectTable()
    usbd.get_tables()
    len_before = len(usbd.get_list())
    new_subject_title = "Astrology"
    usbd.insert_new({"new_subject_title": new_subject_title})
    len_after = len(usbd.get_list())
    assert len_after == len_before + 1, f"Expected {len_before + 1}, but got {len_after}"
    assert new_subject_title in [row['subject_title'] for row in
    usbd.get_list()], "New subject not found in the list."
    usbd.delete_new({"new_subject_title": new_subject_title})
    assert new_subject_title not in [row['subject_title'] for row in usbd.get_list()], "Subject was not deleted."

