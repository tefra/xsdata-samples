import subprocess
import time
from contextlib import contextmanager
from pathlib import Path

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler
from xsdata.formats.dataclass.parsers.handlers import XmlEventHandler


@contextmanager
def timing(description: str) -> None:
    start = time.time()
    yield
    ellapsed_time = time.time() - start

    print(f"{description}: {ellapsed_time}")


with timing("importing module"):
    from netex.models import *

here = Path(__file__).parent
with timing("decompress sample"):
    subprocess.run(
        ["tar", "-xf", str(here.joinpath("NeTEx_HTM__2020-10-12.tar.xz")), "-C", "/tmp"]
    )


sample = "/tmp/NeTEx_HTM__2020-10-12.xml"
context = XmlContext()
config = ParserConfig(fail_on_unknown_properties=False)

parser = XmlParser(context=context, config=config, handler=LxmlEventHandler)
with timing("XmlContext warmup"):
    parser.parse(sample, PublicationDelivery)

parser = XmlParser(context=context, config=config, handler=LxmlEventHandler)
with timing("Parse[LxmlEventHandler]"):
    parser.parse(sample, PublicationDelivery)

parser = XmlParser(context=context, config=config, handler=XmlEventHandler)
with timing("Parse[EventHandler]"):
    parser.parse(sample, PublicationDelivery)
