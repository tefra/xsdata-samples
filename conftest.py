import json
from pathlib import Path

import pytest
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import JsonParser
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import JsonSerializer
from xsdata.formats.dataclass.serializers import PycodeSerializer
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.formats.dataclass.serializers import TreeSerializer
from xsdata.utils.debug import convert


_session_context_data = {}


def pytest_addoption(parser):
    parser.addoption(
        "--output-format",
        action="store",
        default="dataclasses",
        choices=["dataclasses", "attrs", "pydantic"],
        help="Class type format",
    )

    parser.addoption(
        "--dump-context",
        action="store_true",
        default=False,
        help="Dump debug data.",
    )


def pytest_sessionfinish(session, exitstatus):
    """Write accumulated context data once at end of session."""
    if not session.config.getoption("--dump-context"):
        return

    if not _session_context_data:
        return

    dump = Path(__file__).parent / "ctx.json"
    with dump.open("w") as f:
        json.dump(_session_context_data, f, indent=4)


@pytest.fixture
def output_format(request):
    return request.config.getoption("--output-format")


@pytest.fixture
def xml_context(output_format, request):
    ctx = XmlContext(class_type=output_format)
    yield ctx

    if not request.config.getoption("--dump-context"):
        return

    _session_context_data.update(convert(ctx.cache))


@pytest.fixture
def serializer_config():
    return SerializerConfig(indent="  ", ignore_default_attributes=True)


@pytest.fixture
def xml_parser(xml_context):
    return XmlParser(context=xml_context)


@pytest.fixture
def xml_serializer(xml_context, serializer_config):
    return XmlSerializer(context=xml_context, config=serializer_config)


@pytest.fixture
def code_serializer(xml_context, serializer_config):
    return PycodeSerializer(context=xml_context)


@pytest.fixture
def json_parser(xml_context):
    return JsonParser(context=xml_context)


@pytest.fixture
def json_serializer(xml_context, serializer_config):
    return JsonSerializer(context=xml_context, config=serializer_config)


@pytest.fixture
def tree_serializer(xml_context, serializer_config):
    return TreeSerializer(context=xml_context, config=serializer_config)
