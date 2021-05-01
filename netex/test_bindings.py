from pathlib import Path

import pytest
from lxml import etree
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer

from netex.models import PublicationDelivery

ids = []
here = Path(__file__).parent
samples = list(map(str, here.joinpath("NeTEx/examples/functions").rglob("*.xml")))
schema = here.joinpath("NeTEx/xsd/NeTEx_publication.xsd")

validator = etree.XMLSchema(etree.parse(str(schema)))

parser = XmlParser()
serializer = XmlSerializer()
serializer.config.pretty_print = True


@pytest.mark.parametrize("sample", samples)
def test_serialize(sample):

    obj = parser.parse(sample, PublicationDelivery)
    output = serializer.render(obj, ns_map=parser.ns_map)
    parser.ns_map.clear()

    validator.assertValid(etree.fromstring(output.encode()))
