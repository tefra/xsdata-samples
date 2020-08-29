from pathlib import Path

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.handlers import IterparseHandler
from xsdata.formats.dataclass.parsers.handlers import TargetHandler

from sabre.models import OtaAirLowFareSearchRs

here = Path(__file__).parent.absolute()
fixture = here.joinpath("bargain_finder_max_rs.xml")

context = XmlContext()


def parse(handler):
    parser = XmlParser(context=context, handler=handler)
    parser.from_path(fixture, OtaAirLowFareSearchRs)


def test_target_performance(benchmark):
    benchmark(parse, TargetHandler)


def test_iterparse_performance(benchmark):
    benchmark(parse, IterparseHandler)
