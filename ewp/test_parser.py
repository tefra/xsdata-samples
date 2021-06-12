import json
from pathlib import Path

from xsdata.formats.dataclass.serializers import DictFactory

from ewp.models import Catalogue

cwd = Path(__file__).parent.absolute()


def test_bindings(xml_parser, json_serializer):
    fixture = "catalogue-example"
    xml_fixture = cwd.joinpath(f"{fixture}.xml")
    json_fixture = cwd.joinpath(f"{fixture}.json")

    obj = xml_parser.from_path(xml_fixture, Catalogue)

    json_serializer.dict_factory = DictFactory.FILTER_NONE
    result = json_serializer.render(obj)

    if json_fixture.exists():
        expected = json_fixture.read_text()
        assert json.loads(expected) == json.loads(result)
    else:
        json_fixture.write_text(result + "\n")
