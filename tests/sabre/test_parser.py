import json
from pathlib import Path
from unittest import TestCase

from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import DictSerializer

from samples.sabre.output.bargain_finder_max_rs_v1_9_7 import (
    OtaAirLowFareSearchRs,
)

parser = XmlParser()
serializer = DictSerializer()
dir = Path(__file__).parent.absolute()


def value_dict(data):
    return {x: v for x, v in dict(data).items() if v is not None}


class ParserTests(TestCase):
    def test_bargain_finder_max(self):
        fixture = "bargain_finder_max_rs"

        xml_str = dir.joinpath(f"{fixture}.xml")
        obj = parser.from_path(xml_str, OtaAirLowFareSearchRs)

        output = dir.joinpath(f"{fixture}.json")
        expected = json.loads(output.read_text())

        result = serializer.render(obj, dict_factory=serializer.filter_none)
        self.assertEqual(expected, result)

        output.write_text(json.dumps(result, indent=2))
