from pathlib import Path
from unittest import TestCase

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer

from autosar.models import Autosar

context = XmlContext()
parser = XmlParser(context=context)
serializer = XmlSerializer(context=context)
serializer.config.pretty_print = True
cwd = Path(__file__).parent.absolute()


class ParserTests(TestCase):
    def test_ecu_example(self):
        fixture = "MyECU.ecuc"
        xml_fixture = cwd.joinpath(f"{fixture}.arxml")
        xsdata_fixture = cwd.joinpath(f"{fixture}.xsdata.xml")

        obj = parser.from_path(xml_fixture, Autosar)
        result = serializer.render(obj)

        if xsdata_fixture.exists():
            expected = xsdata_fixture.read_text()
            self.assertEqual(expected, result)
        else:
            xsdata_fixture.write_text(result)
