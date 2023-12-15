# Architecture Patterns with Python


## Requirements

```sh
# Python 3.11
pip install requirements.txt
pip install -e src/
```


## Running the tests

Docker

```sh
# All
make test
# Or any
make unit
make integration
make e2e
```

Local

```sh
# Start envs for integration/e2e
make up

# All
pytest
pytest tests/

# Or any
pytest tests/unit
pytest tests/integration
pytest tests/e2e
```


## Reference

- Architecture Patterns with Python ([Site](https://www.cosmicpython.com/))([Book](https://www.cosmicpython.com/book/preface.html))([Github](https://github.com/cosmicpython/code))
- [Python Packaging User Guide](https://packaging.python.org/en/latest/)
- Pytest
  - [Good Integration Practices](https://docs.pytest.org/en/latest/explanation/goodpractices.html)
