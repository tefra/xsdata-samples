from pathlib import Path
from unittest import TestCase

from lxml import etree
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer

from reqif.models import ReqIf

parser = XmlParser(context=XmlContext())
serializer = XmlSerializer(context=parser.context, pretty_print=True)
here = Path(__file__).parent.absolute()


class BindingTests(TestCase):
    def test_parser_validate_serializer_output(self):
        xml_fixture = here.joinpath("sample.xml")

        obj = parser.from_path(xml_fixture, ReqIf)
        tree = serializer.render_tree(obj)

        schema_doc = etree.parse(here.joinpath("schemas/reqif.xsd").as_uri())
        schema = etree.XMLSchema(schema_doc)

        schema.assertValid(tree)

        here.joinpath("sample.output.xml").write_bytes(
            etree.tostring(
                tree, xml_declaration=True, encoding="ascii", pretty_print=True,
            )
        )
