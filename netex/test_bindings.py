from pathlib import Path

import pytest
from lxml import etree
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer

from netex.models import PublicationDelivery

here = Path(__file__).parent
output = here.joinpath("output")
functions = here.joinpath("NeTEx/examples/functions")
samples = [str(sample.relative_to(functions)) for sample in functions.rglob("*.xml")]
schema = here.joinpath("NeTEx/xsd/NeTEx_publication.xsd")

validator = etree.XMLSchema(etree.parse(str(schema)))

parser = XmlParser()
serializer = XmlSerializer()
serializer.config.pretty_print = True


@pytest.mark.parametrize("sample", samples)
def test_serialize(sample):

    obj = parser.from_path(functions.joinpath(sample), PublicationDelivery)
    result = serializer.render(obj, ns_map=parser.ns_map)
    parser.ns_map.clear()

    expected = output.joinpath(sample)
    if expected.exists():
        assert expected.read_text().strip() == result.strip()
    else:
        expected.parent.mkdir(parents=True, exist_ok=True)
        expected.write_text(result + "\n")

    validator.assertValid(etree.fromstring(result.encode()))
