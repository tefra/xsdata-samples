from pathlib import Path
from unittest import TestCase

from lxml import etree
from xsdata.formats.dataclass.parsers import JsonParser
from xsdata.formats.dataclass.serializers import XmlSerializer

from travelport.models import LowFareSearchReq

parser = JsonParser()
serializer = XmlSerializer(pretty_print=True)
cwd = Path(__file__).parent.absolute()
xsd_location = str(cwd.joinpath("schemas/air_v48_0/AirReqRsp.xsd"))


class SerializerTests(TestCase):
    def test_low_fare_search(self):
        fixture = "low_fare_search"
        json_fixture = cwd.joinpath(f"{fixture}.json")
        xml_fixture = cwd.joinpath(f"{fixture}.xml")

        obj = parser.from_path(json_fixture, LowFareSearchReq)
        xml = serializer.render(
            obj=obj,
            ns_map={
                None: "http://www.travelport.com/schema/air_v48_0",
                "ns1": "http://www.travelport.com/schema/common_v48_0",
            },
        )

        xml_fixture.write_text(xml)

        schema = etree.XMLSchema(etree.parse(xsd_location))
        is_valid = schema.validate(etree.parse(str(xml_fixture)))
        self.assertTrue(is_valid, schema.error_log)
