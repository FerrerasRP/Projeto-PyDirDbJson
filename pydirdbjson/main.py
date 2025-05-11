"""Projeto PyDirDbJson - main.py

Class to Database in JSON on directory project.

Main class:
    Pydirdbjson - Main class.

Functions:
    create_table() - Create a table.
    insert() - Insert a record on table.
    delete() - Delete a record on table.
    query() - Query a record on table.
    query_by_key_value() - Query a record by value and key on table.

"""
import os
import json

class Pydirdbjson:
    """Pydirdbjson class.

    Args:
        db_path (str): Path (directory) of database.

    Methods:
        create_table(): Create a table.
        insert(): Insert a record on table.
        delete(): Delete a record on table.
        query(): Query a record on table.
        query_by_key_value(): Query a record by value and key on table.

    """
    def __init__(self,
                 db_path: str):
        self.db_path = db_path
        if not os.path.exists(db_path):
            os.makedirs(db_path)

    def create_table(self,
                     table_name: str):
        """Create a table (subdirectory).

        Args:
            table_name (str): Table name (subdirectory).

        """
        table_path = os.path.join(self.db_path, table_name)
        if not os.path.exists(table_path):
            os.makedirs(table_path)

    def insert(self,
               table_name: str,
               record_id: str,
               record: dict):
        """Insert a record (file) on table (subdirectory).

        Args:
            table_name (str): Table name (subdirectoy).
            record_id (str): Record ID (file).
            record (dict): Data dictionary.

        Raises:
            FileNotFoundError: If table not found.

        """
        table_path = os.path.join(self.db_path, table_name)
        if not os.path.exists(table_path):
            raise FileNotFoundError(f"Table {table_name} does not exist.")
        record_path = os.path.join(table_path, f"{record_id}.json")
        with open(record_path, 'w', encoding='utf-8') as f:
            json.dump(record, f)

    def delete(self,
               table_name: str,
               record_id: str):
        """Delete a record (file) on table (subdirectory).

        Args:
            table_name (str): Table name (subdirectory).
            record_id (str): Record ID (file).

        Raises:
            FileNotFoundError: If table or record not found.

        """
        table_path = os.path.join(self.db_path, table_name)
        if not os.path.exists(table_path):
            raise FileNotFoundError(f"Table {table_name} does not exist.")
        record_path = os.path.join(table_path, f"{record_id}.json")
        if os.path.exists(record_path):
            os.remove(record_path)
        else:
            raise FileNotFoundError(f"Record {record_id} does not exist.")

    def query(self,
              table_name: str,
              record_id: str) -> dict:
        """Query a record id (file) on table (subdirectory).

        Args:
            table_name (str): Table name (subdirectory).
            record_id (str): Record ID (file).

        Returns:
            dict: Data Dictionary.

        Raise:
            FileNotFoundError: If table or record not found.

        """
        table_path = os.path.join(self.db_path, table_name)
        if not os.path.exists(table_path):
            raise FileNotFoundError(f"Table {table_name} does not exist.")
        record_path = os.path.join(table_path, f"{record_id}.json")
        if os.path.exists(record_path):
            with open(record_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            raise FileNotFoundError(f"Record {record_id} does not exist.")

    def query_by_key_value(self,
                           table_name: str,
                           key: str,
                           value: any,
                           keys_to_return: list = None) -> list:
        """Query a record by value and key on table (subdirectory).

        Args:
            table_name (str): Table name (subdirectory).
            key (str): Key on data dictionary.
            value (any): Value on data disctionary.
            keys_to_return (list): List of keys to return.

        Returns:
            list: List of data dictionary

        Raise:
            FileNotFoundError: If table or record not found.

        """
        table_path = os.path.join(self.db_path, table_name)
        if not os.path.exists(table_path):
            raise FileNotFoundError(f"Table {table_name} does not exist.")
        results = []
        for filename in os.listdir(table_path):
            if filename.endswith('.json'):
                record_path = os.path.join(table_path, filename)
                with open(record_path, 'r', encoding='utf-8') as f:
                    record = json.load(f)
                    if key in record and record[key] == value:
                        if keys_to_return:
                            filtered_record = {k: record[k] for k in keys_to_return if k in record}
                            results.append(filtered_record)
                        else:
                            results.append(record)
        return results
