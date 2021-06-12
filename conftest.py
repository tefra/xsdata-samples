import pytest
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import JsonParser
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import JsonSerializer
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig


def pytest_addoption(parser):
    parser.addoption(
        "--output-format",
        action="store",
        default="dataclasses",
        choices=["dataclasses", "attrs"],
        help="Class type format",
    )


@pytest.fixture
def output_format(request):
    return request.config.getoption("--output-format")


@pytest.fixture
def xml_context(output_format):
    return XmlContext(class_type=output_format)


@pytest.fixture
def xml_parser(xml_context):
    return XmlParser(context=xml_context)


@pytest.fixture
def xml_serializer(xml_context):
    return XmlSerializer(
        context=xml_context, config=SerializerConfig(pretty_print=True)
    )


@pytest.fixture
def json_parser(xml_context):
    return JsonParser(context=xml_context)


@pytest.fixture
def json_serializer(xml_context):
    return JsonSerializer(context=xml_context, indent=4)
