from pathlib import Path
from unittest import TestCase

from lxml import etree
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import JsonSerializer
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from datexii.models import D2LogicalModel

config = SerializerConfig(pretty_print=True)
context = XmlContext()
xml_parser = XmlParser(context=context)
xml_serializer = XmlSerializer(context=context, config=config)
json_serializer = JsonSerializer(context=context)
here = Path(__file__).parent.absolute()
xsd_location = str(here.joinpath("schemas/DATEXIISchema_2_2_3.xsd"))


class SerializerTests(TestCase):
    def test_binding(self):
        ns_map = {None: "http://datex2.eu/schema/2/2_0"}
        sample = here.joinpath("sample.xml")

        payload = xml_parser.from_path(sample, D2LogicalModel)
        result = xml_serializer.render(payload, ns_map=ns_map)

        output = here.joinpath("sample.xsdata.xml")
        if output.exists():
            self.assertEqual(output.read_text(), result)
        else:
            output.write_text(result)

        schema = etree.XMLSchema(etree.parse(xsd_location))
        is_valid = schema.validate(etree.parse(str(output)))
        self.assertTrue(is_valid, schema.error_log)
