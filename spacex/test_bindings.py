from pathlib import Path
from typing import List

from spacex.models import Launches

here = Path(__file__).parent


def test_parser(json_parser, json_serializer):
    sample = here.joinpath("launches.json")
    launches = json_parser.from_path(sample, List[Launches])

    assert 145 == len(launches)

    output = here.joinpath("launch.output.json")

    actual = json_serializer.render(launches[0])

    if output.exists():
        assert output.read_text() == actual
    else:
        output.write_text(actual)
