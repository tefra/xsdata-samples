from pathlib import Path

import pytest
from lxml import etree

from voko.models import Vortaro

here = Path(__file__).parent
schemas = here.joinpath("dtd")
output_dir = here.joinpath("output")
samples_dir = here.joinpath("samples")
samples = list(map(str, samples_dir.rglob("*.xml")))

dtd = etree.DTD(schemas.joinpath("vokoxml.dtd"))


@pytest.mark.parametrize("sample", samples)
def test_bindings(sample, xml_parser, xml_serializer):
    xml_parser.config.load_dtd = True
    ns_map = {}
    obj = xml_parser.parse(sample, Vortaro, ns_map)
    result = xml_serializer.render(obj, ns_map=ns_map)

    sample_path = Path(sample).relative_to(samples_dir)
    expected = output_dir.joinpath(sample_path)
    if expected.exists():
        assert expected.read_text().strip() == result.strip()
    else:
        expected.parent.mkdir(parents=True, exist_ok=True)
        expected.write_text(result + "\n")

    root = etree.XML(result.encode())

    dtd.assertValid(root)
