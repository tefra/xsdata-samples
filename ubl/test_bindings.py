import functools
from pathlib import Path

import pytest
from lxml import etree

from ubl.models.maindoc import *  # noqa

cases = []
ids = []
here = Path(__file__).parent
schemas = here.joinpath("schemas/maindoc").resolve().glob("*")
for sch in list(schemas):
    _, name, _ = sch.name.split("-")
    for smp in here.joinpath("samples").glob(f"UBL-{name}-*"):
        if not smp.stem.endswith("xsdata"):
            cases.append((str(sch), str(smp)))
            ids.append(smp.name)


@functools.lru_cache(maxsize=5)
def get_validator(xsd: str):
    return etree.XMLSchema(etree.parse(xsd))


@pytest.mark.parametrize("schema,sample", cases, ids=ids)
def test_serialize(schema, sample, xml_parser, xml_serializer):
    obj = xml_parser.parse(sample)
    result = xml_serializer.render(obj, ns_map=xml_parser.ns_map)
    xml_parser.ns_map.clear()

    expected = Path(sample).with_suffix(".xsdata.xml")
    if expected.exists():
        assert expected.read_text() == result
    else:
        expected.write_text(result + "\n")

    validator = get_validator(schema)
    validator.assertValid(etree.fromstring(result.encode()))
