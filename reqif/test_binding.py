from pathlib import Path
from unittest import TestCase

from lxml import etree
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import JsonSerializer
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from reqif.models import ReqIf

parser = XmlParser(context=XmlContext())
config = SerializerConfig(pretty_print=True, encoding="ascii")
serializer = XmlSerializer(context=parser.context, config=config)
jsonSerializer = JsonSerializer(indent=True)
here = Path(__file__).parent.absolute()


class BindingTests(TestCase):
    def test_parser_validate_serializer_output(self):
        xml_fixture = here.joinpath("sample.xml")
        output = here.joinpath("sample.output.xml")

        obj = parser.from_path(xml_fixture, ReqIf)
        ns_map = {
            None: "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "xhtml": "http://www.w3.org/1999/xhtml",
        }
        with output.open("w") as f:
            serializer.write(f, obj, ns_map=ns_map)

        schema_doc = etree.parse(here.joinpath("schemas/reqif.xsd").as_uri())
        schema = etree.XMLSchema(schema_doc)
        output.with_suffix(".json").write_text(jsonSerializer.render(obj) + "\n")

        schema.assertValid(etree.parse(str(output)))
