import sys
from pathlib import Path

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer

from reqif.models import ReqIf

here = Path(__file__).parent

xml_fixture = here.joinpath("sample.xml")
context = XmlContext()
parser = XmlParser(context=context)
serializer = XmlSerializer(context=context, pretty_print=True, encoding="ascii")

obj = parser.from_path(xml_fixture, ReqIf)
ns_map = {
    None: "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
    "xhtml": "http://www.w3.org/1999/xhtml",
}
serializer.write(sys.stdout, obj, ns_map=ns_map)
