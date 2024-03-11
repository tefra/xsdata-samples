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
    for smp in here.joinpath("samples").glob(f"UBL-{name}-*.xml"):
        if not smp.stem.endswith("xsdata"):
            cases.append((str(sch), str(smp)))
            ids.append(smp.name)


@functools.lru_cache(maxsize=5)
def get_validator(xsd: str):
    return etree.XMLSchema(etree.parse(xsd))


@pytest.mark.parametrize("schema,sample", cases, ids=ids)
def test_serialize(schema, sample, xml_parser, xml_serializer, code_serializer):
    ns_map = {}
    obj = xml_parser.parse(sample, ns_map=ns_map)
    result = xml_serializer.render(obj, ns_map=ns_map)
    code = code_serializer.render(obj)
    output = Path(sample)

    output.with_suffix(".py").write_text(code)
    expected = output.with_suffix(".xsdata.xml")
    if expected.exists():
        assert expected.read_text() == result
    else:
        expected.write_text(result)

    validator = get_validator(schema)
    validator.assertValid(etree.fromstring(result.encode()))
