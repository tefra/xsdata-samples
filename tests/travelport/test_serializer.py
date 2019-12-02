import json
from pathlib import Path
from unittest import TestCase
from uuid import UUID

from lxml import etree
from xsdata.formats.dict.parser import DictParser
from xsdata.formats.xml.serializer import XmlSerializer

from samples.travelport.output.air_v48_0.air_req_rsp import LowFareSearchReq

parser = DictParser()
serializer = XmlSerializer()

class SerializerTests(TestCase):
    def test_low_fare_search(self):
        fixture = "low_fare_search"
        xsd = (
            "../../xsd/travelport/air_v48_0/AirReqRsp.xsd"
        )

        json_data = Path(f"{fixture}.json").read_text()
        obj = parser.from_json(json_data, LowFareSearchReq)

        xml = serializer.render(obj, pretty_print=True)

        output = Path(f"{fixture}.xml")
        output.write_text(xml.decode())

        schema = etree.XMLSchema(etree.parse(xsd))
        is_valid = schema.validate(etree.parse(str(output)))
        self.assertTrue(is_valid, schema.error_log)
