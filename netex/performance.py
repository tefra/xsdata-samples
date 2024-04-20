import subprocess
import time
from contextlib import contextmanager
from pathlib import Path
from typing import Any
from sys import getsizeof

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler
from xsdata.formats.dataclass.parsers.handlers import XmlEventHandler


@contextmanager
def timing(description: str) -> Any:
    start = time.time()
    yield
    ellapsed_time = time.time() - start

    print(f"{description}: {ellapsed_time}")


def get_size(obj, seen=None):
    """Recursively finds size of objects."""
    size = getsizeof(obj)
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0
    seen.add(obj_id)
    if isinstance(obj, dict):
        size += sum(get_size(v, seen) for v in obj.values())
        size += sum(get_size(k, seen) for k in obj.keys())
    elif hasattr(obj, "__dict__"):
        size += get_size(obj.__dict__, seen)
    elif hasattr(obj, "__iter__") and not isinstance(obj, (str, bytes, bytearray)):
        size += sum(get_size(i, seen) for i in obj)
    return size


with timing("importing module"):
    from netex.models import *  # noqa

sample = str(Path(__file__).parent.joinpath("NeTEx_HTM__2020-10-12.tar.xz"))
with timing("decompress sample"):
    subprocess.run(["tar", "-xf", sample, "-C", "/tmp"])

sample = "/tmp/NeTEx_HTM__2020-10-12.xml"
context = XmlContext()
config = ParserConfig(fail_on_unknown_properties=False)


from netex.models import PublicationDelivery  # noqa

with timing("XmlContext warmup"):
    context.build_recursive(PublicationDelivery)
    print(f"Context cache size: {get_size(context.cache)}")

parser = XmlParser(context=context, config=config, handler=LxmlEventHandler)
with timing("Parse[LxmlEventHandler]"):
    parser.parse(sample, PublicationDelivery)

parser = XmlParser(context=context, config=config, handler=XmlEventHandler)
with timing("Parse[EventHandler]"):
    parser.parse(sample, PublicationDelivery)
