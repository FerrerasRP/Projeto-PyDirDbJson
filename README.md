# Projeto-PyDirDbJson

[![Run Python tests](https://github.com/FerrerasRP/Projeto-PyDirDbJson/actions/workflows/test.yml/badge.svg)](https://github.com/FerrerasRP/Projeto-PyDirDbJson/actions/workflows/test.yml)
[![Publish Python to PyPI](https://github.com/FerrerasRP/Projeto-PyDirDbJson/actions/workflows/publish_to_pypi.yml/badge.svg)](https://github.com/FerrerasRP/Projeto-PyDirDbJson/actions/workflows/publish_to_pypi.yml)
![GitHub repo size](https://img.shields.io/github/repo-size/FerrerasRP/Projeto-PyDirDbJson)
![GitHub contributors](https://img.shields.io/github/contributors/FerrerasRP/Projeto-PyDirDbJson)
![GitHub stars](https://img.shields.io/github/stars/FerrerasRp/Projeto-PyDirDbJson)
![GitHub forks](https://img.shields.io/github/forks/FerrerasRP/Projeto-PyDirDbJson)

Project name is a Database in JSON on directory.

## Prerequisites

No prerequisites

## Installing PyDirDbJson

To install PyDirDbJson, follow these steps:

Windows, Linux and macOS:
```
pip install pydirdbjson
```

## Using PyDirDbJson

To use pydirdbjson, follow these steps:

```python
from pydirdbjson import Pydirdbjson
```

```python
db = Pydirdbjson(db_path='my_database')

db.create_table(table_name='users')
db.insert(table_name='users',
          record_id='1',
          record={'name': 'John', 'age': 30, 'city': 'São Paulo'})
db.insert(table_name='users',
          record_id='2',
          record={'name': 'Mary', 'age': 25, 'city': 'Rio de Janeiro'})

db.create_table(table_name='customers')
db.insert(table_name='customers',
          record_id='1',
          record={'name': 'ABC'})
db.insert(table_name='customers',
          record_id='2',
          record={'name': 'XWZ'})

db.create_table(table_name='permissions')
db.insert(table_name='permissions',
          record_id='1',
          record={'user': '1', 'customer': '1'})
db.insert(table_name='permissions',
          record_id='2',
          record={'user': '1', 'customer': '2'})
db.insert(table_name='permissions',
          record_id='3',
          record={'user': '2', 'customer': '2'})
```

```python
print(db.query(table_name='users', record_id='1'))

>>> {'name': 'John', 'age': 30, 'city': 'São Paulo'}

print(db.query_by_key_value(table_name='permissions',
                            key='customer',
                            value='1',
                            keys_to_return=['user']))

>>> [{'user': '1'}]
```

```python
db.delete(table_name='users', record_id='1')
```

## Database structure

```bash
|-- my_database
|   |-- users
|   |   |-- 1.json
|   |   |-- 2.json
|   |-- customers
|   |   |-- 1.json
|   |   |-- 2.json
|   |-- permissions
|   |   |-- 1.json
|   |   |-- 2.json
|   |   |-- 3.json
```

## File structure


File: my_database/users/2.json

```json
{"name": "Mary", "age": 25, "city": "Rio de Janeiro"}
```

## Contributing to PyDirDbJson

To contribute to PyDirDbJson, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.

Alternatively see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## Contributors

Thanks to the following people who have contributed to this project:

* [@FerrerasRP](https://github.com/FerrerasRP) 📖

You might want to consider using something like the [All Contributors](https://github.com/all-contributors/all-contributors) specification and its [emoji key](https://allcontributors.org/docs/en/emoji-key).

## Contact

If you want to contact me you can reach me at ricardo(dot)ferreras(at)gmail(dot)com.

## License

This project uses the following license: [MIT](LICENSE).
