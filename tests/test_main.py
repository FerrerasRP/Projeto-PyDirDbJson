"""Projeto-PyDirDbJson - setup.py

Script para criação do setup do pypi

"""
import sys
import os

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath('test_main.py'))
# Add the project root directory to the Python path
project_root = os.path.join(current_dir, "..")  # Adjust ".." based on your structure
sys.path.insert(0, project_root)

from pydirdbjson import Pydirdbjson

def test_create_database():
    """Test create database"""
    _db = Pydirdbjson(db_path='db_test')

    assert os.path.exists('db_test')
    assert os.path.isdir('db_test')

def test_create_table():
    """Test create table"""
    _db = Pydirdbjson(db_path='db_test')

    _db.create_table(table_name='test')

    assert os.path.exists('db_test/test')
    assert os.path.isdir('db_test/test')

def test_insert():
    """Test insert"""
    _db = Pydirdbjson(db_path='db_test')

    _db.create_table(table_name='test')
    _db.insert(table_name='test',
               record_id='987',
               record={'teste': 123, 'teste2': 'aaa'})

    assert os.path.exists('db_test/test')
    assert os.path.isfile('db_test/test/987.json')

def test_delete():
    """Test delete"""
    _db = Pydirdbjson(db_path='db_test')

    _db.create_table(table_name='test')
    _db.insert(table_name='test',
               record_id='987',
               record={'teste': 123, 'teste2': 'aaa'})

    assert os.path.exists('db_test/test')
    assert os.path.isfile('db_test/test/987.json')

    _db.delete(table_name='test',
               record_id='987')

    assert not os.path.isfile('db_test/test/987.json')

def test_query():
    """Test query"""
    _db = Pydirdbjson(db_path='db_test')

    _db.create_table(table_name='test')
    _db.insert(table_name='test',
               record_id='987',
               record={'teste': 123, 'teste2': 'aaa'})
    resultado = _db.query(table_name='test',
                          record_id='987')

    assert resultado == {'teste': 123, 'teste2': 'aaa'}

def test_query_by_key_value():
    """Test query"""
    _db = Pydirdbjson(db_path='db_test')

    _db.create_table(table_name='test')
    _db.insert(table_name='test',
               record_id='987',
               record={'teste': 123, 'teste2': 'aaa'})
    _db.insert(table_name='test',
               record_id='988',
               record={'teste': 124, 'teste2': 'bbb'})
    resultado = _db.query_by_key_value(table_name='test',
                                       key='teste',
                                       value=124,
                                       keys_to_return=['teste2'])

    assert resultado == [{'teste2': 'bbb'}]
