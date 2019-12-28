from pathlib import Path
from unittest import TestCase

from lxml import etree
from xsdata.formats.dataclass.parsers import DictParser
from xsdata.formats.dataclass.serializers import XmlSerializer

from samples.sabre.output.bargain_finder_max_rq_v1_9_7 import (
    OtaAirLowFareSearchRq,
)

parser = DictParser()
serializer = XmlSerializer()
dir = Path(__file__).parent.absolute()
xsd_location = str(
    dir.joinpath("../../xsd/sabre/BargainFinderMaxRQ_v1-9-7.xsd")
)


class SerializerTests(TestCase):
    def test_bargain_finder_max(self):
        fixture = "bargain_finder_max_rq"

        json_data = dir.joinpath(f"{fixture}.json").read_text()
        xml = serializer.render(
            obj=parser.from_json(json_data, OtaAirLowFareSearchRq),
            pretty_print=True,
        )

        output = dir.joinpath(f"{fixture}.xml")
        output.write_text(xml.decode())

        schema = etree.XMLSchema(etree.parse(xsd_location))
        is_valid = schema.validate(etree.parse(str(output)))
        self.assertTrue(is_valid, schema.error_log)
