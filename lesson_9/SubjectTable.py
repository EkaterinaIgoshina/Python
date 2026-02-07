from sqlalchemy import create_engine, inspect, text


with open("pass.txt", "r") as file:
    connection_string = file.read()

class SubjectTable:
    scripts = {
        "select": text("SELECT * FROM subject"),
        "select_max_id": text("SELECT MAX(subject_id) FROM subject"),
        "delete_by_title": text("DELETE FROM subject WHERE subject_title = :new_subject_title"),
        "insert_new": text("INSERT INTO subject(subject_title) VALUES (:new_subject_title)"),
        "update_title": text("UPDATE subject SET subject_title = :new_title WHERE subject_id = :subject_id"),
    }

    def __init__(self):
        with open("pass.txt", "r") as file:
            self.connection_string = file.read()
        self.db = create_engine(self.connection_string)

    def get_tables(self):
        inspector = inspect(self.db)
        res = inspector.get_table_names()
        print("Существующие таблицы:", res)
        assert 'subject' in res

    def insert_new(self, value_new):
        conn = self.db.connect()
        transaction = conn.begin()
        conn.execute(self.scripts["insert_new"], value_new)
        transaction.commit()

    def delete_new(self, value_deleted):
        conn = self.db.connect()
        transaction = conn.begin()
        conn.execute(self.scripts["delete_by_title"], value_deleted)
        transaction.commit()

    def get_list(self):
        conn = self.db.connect()
        result = conn.execute(self.scripts["select"])
        rows = result.mappings().all()
        return rows

