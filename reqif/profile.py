import sys
from pathlib import Path

from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from reqif.models import ReqIf

here = Path(__file__).parent

xml_fixture = here.joinpath("sample.xml")
parser = XmlParser()
config = SerializerConfig(pretty_print=True, encoding="ascii")
serializer = XmlSerializer(context=parser.context, config=config)

obj = parser.from_path(xml_fixture, ReqIf)
ns_map = {
    None: "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
    "xhtml": "http://www.w3.org/1999/xhtml",
}
serializer.write(sys.stdout, obj, ns_map=ns_map)
