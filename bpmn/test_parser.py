from pathlib import Path
from typing import Dict

from bpmn.models import Definitions

cwd = Path(__file__).parent.absolute()


def test_waypoint_example(xml_parser, xml_serializer):
    fixture = "example"
    xml_fixture = cwd.joinpath(f"{fixture}.xml")
    xsdata_fixture = cwd.joinpath(f"{fixture}.xsdata.xml")
    ns_map: Dict = {}
    obj = xml_parser.from_path(xml_fixture, Definitions, ns_map)
    result = xml_serializer.render(obj, ns_map=ns_map)

    if xsdata_fixture.exists():
        expected = xsdata_fixture.read_text()
        assert expected == result
    else:
        xsdata_fixture.write_text(result)
