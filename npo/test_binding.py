from pathlib import Path
from unittest import TestCase

from lxml import etree
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import JsonSerializer
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from npo.models import PageSearchResult

parser = XmlParser(context=XmlContext())
config = SerializerConfig(pretty_print=True)
serializer = XmlSerializer(context=parser.context, config=config)
jsonSerializer = JsonSerializer(indent=True)
here = Path(__file__).parent.absolute()
schema_path = here.joinpath("schemas/rs.poms.omroep.nl/v1/schema/urn:vpro:api:2013")


class BindingTests(TestCase):
    def test_binding(self):
        xml_fixture = here.joinpath("sample.xml")
        output = here.joinpath("sample.output.xml")
        ns_map = {
            "api": "urn:vpro:api:2013",
            "pages": "urn:vpro:pages:2013",
        }

        obj = parser.from_path(xml_fixture, PageSearchResult)
        with output.open("w") as f:
            serializer.write(f, obj, ns_map=ns_map)

        schema_doc = etree.parse(schema_path.as_uri())
        schema = etree.XMLSchema(schema_doc)
        output.with_suffix(".json").write_text(jsonSerializer.render(obj) + "\n")

        schema.assertValid(etree.parse(str(output)))

        self.assertEqual(obj.items.item[0].result.title, "Antibiotics")
