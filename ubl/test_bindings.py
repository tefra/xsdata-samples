import functools
from pathlib import Path

import pytest
from lxml import etree
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer

from ubl.models.maindoc import *  # noqa

cases = []
ids = []
here = Path(__file__).parent
schemas = here.joinpath("schemas/maindoc").resolve().glob("*")
for schema in list(schemas):
    _, name, _ = schema.name.split("-")
    for sample in here.joinpath("samples").glob(f"UBL-{name}-*"):
        cases.append((str(schema), str(sample)))
        ids.append(sample.name)

parser = XmlParser()
serializer = XmlSerializer()
serializer.config.pretty_print = True


@functools.lru_cache(maxsize=5)
def get_validator(xsd: str):
    return etree.XMLSchema(etree.parse(xsd))


@pytest.mark.parametrize("schema,sample", cases, ids=ids)
def test_serialize(schema, sample):
    obj = parser.parse(sample)
    output = serializer.render(obj, ns_map=parser.ns_map)
    parser.ns_map.clear()

    validator = get_validator(schema)
    validator.assertValid(etree.fromstring(output.encode()))