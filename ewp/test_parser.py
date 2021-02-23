import json
from pathlib import Path
from unittest import TestCase

from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import DictFactory
from xsdata.formats.dataclass.serializers import JsonSerializer

from ewp.models import Catalogue

parser = XmlParser()
serializer = JsonSerializer(indent=2, dict_factory=DictFactory.FILTER_NONE)
cwd = Path(__file__).parent.absolute()


class ParserTests(TestCase):
    def test_catalogue_example(self):
        fixture = "catalogue-example"
        xml_fixture = cwd.joinpath(f"{fixture}.xml")
        json_fixture = cwd.joinpath(f"{fixture}.json")

        obj = parser.from_path(xml_fixture, Catalogue)
        result = serializer.render(obj)

        if json_fixture.exists():
            expected = json_fixture.read_text()
            self.assertEqual(json.loads(expected), json.loads(result))
        else:
            json_fixture.write_text(result + "\n")
