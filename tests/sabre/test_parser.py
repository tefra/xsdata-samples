import json
from dataclasses import asdict
from pathlib import Path
from unittest import TestCase

from xsdata.formats.xml.parser import XmlParser

from samples.sabre.output.bargain_finder_max_rs_v1_9_7 import (
    OtaAirLowFareSearchRs,
)

parser = XmlParser()
dir = Path(__file__).parent.absolute()


def value_dict(data):
    return {x: v for x, v in dict(data).items() if v is not None}


class ParserTests(TestCase):
    def test_bargain_finder_max(self):
        fixture = "bargain_finder_max_rs"

        xml_str = dir.joinpath(f"{fixture}.xml").read_text()
        obj = parser.parse(xml_str, OtaAirLowFareSearchRs)

        output = dir.joinpath(f"{fixture}.json")
        output.write_text(
            json.dumps(asdict(obj, dict_factory=value_dict), indent=2)
        )
