import json
from pathlib import Path
from unittest import TestCase
from uuid import UUID

from lxml import etree
from xsdata.formats.dict.parser import DictParser
from xsdata.formats.xml.serializer import XmlSerializer

from samples.sabre.output.bargain_finder_max_rq_v1_9_7 import OtaAirLowFareSearchRq

parser = DictParser()
serializer = XmlSerializer()

class SerializerTests(TestCase):
    def test_bargain_finder_max(self):
        fixture = "bargain_finder_max"
        xsd = (
            "../../xsd/sabre/BargainFinderMaxRQ_v1-9-7.xsd"
        )

        json_data = Path(f"{fixture}.json").read_text()
        obj = parser.from_json(json_data, OtaAirLowFareSearchRq)

        xml = serializer.render(obj, pretty_print=True)

        output = Path(f"{fixture}.xml")
        output.write_text(xml.decode())

        schema = etree.XMLSchema(etree.parse(xsd))
        is_valid = schema.validate(etree.parse(str(output)))
        self.assertTrue(is_valid, schema.error_log)
