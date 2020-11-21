from pathlib import Path
from unittest import TestCase

from lxml import etree
from xsdata.formats.dataclass.parsers import JsonParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from sabre.models import OtaAirLowFareSearchRq

parser = JsonParser()
config = SerializerConfig(pretty_print=True)
serializer = XmlSerializer(config=config)
cwd = Path(__file__).parent.absolute()
xsd_location = str(cwd.joinpath("schemas/BargainFinderMaxRQ_v1-9-7.xsd"))


class SerializerTests(TestCase):
    def test_bargain_finder_max(self):
        fixture = "bargain_finder_max_rq"
        json_fixture = cwd.joinpath(f"{fixture}.json")
        xml_fixture = cwd.joinpath(f"{fixture}.xml")

        obj = parser.from_path(json_fixture, OtaAirLowFareSearchRq)
        xml = serializer.render(
            obj, ns_map={None: "http://www.opentravel.org/OTA/2003/05"}
        )

        xml_fixture.write_text(xml)

        schema = etree.XMLSchema(etree.parse(xsd_location))
        is_valid = schema.validate(etree.parse(str(xml_fixture)))
        self.assertTrue(is_valid, schema.error_log)
