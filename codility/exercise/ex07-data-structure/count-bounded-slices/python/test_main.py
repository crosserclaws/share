from ast import literal_eval
from collections.abc import Generator
from pathlib import Path
from typing import Any

from pytest import Metafunc

from main import solution


def test_solution(data_input: tuple[int, list[int]], data_output: int):
    K, A = data_input
    result = solution(K, A)
    assert result == data_output


def pytest_generate_tests(metafunc: Metafunc):
    fixtures = ('data_input', 'data_output')
    if all(f in metafunc.fixturenames for f in fixtures):
        arg_names = ','.join(fixtures)
        paths = (f.replace('_', '/') for f in fixtures)
        data_group = map(load_data, paths)
        arg_values = zip(*data_group)
        metafunc.parametrize(arg_names, arg_values)


def load_data(fixture: str) -> Generator[Any, None, None]:
    for file in Path(fixture).iterdir():
        content = file.read_text().strip()
        data = literal_eval(content)
        yield data
