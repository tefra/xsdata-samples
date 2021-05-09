import os
from pathlib import Path
from typing import Type

from click.testing import CliRunner
from lxml import etree
from xsdata.cli import cli
from xsdata.formats.dataclass.parsers import JsonParser
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import JsonSerializer
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.utils.testing import load_class

here = Path(__file__).parent

root = here.parent
output = here.joinpath("output")
output.mkdir(parents=True, exist_ok=True)

os.chdir(root)


def test_definitive_xml_schema_chapter_01():
    schema = here.joinpath("schemas/chapter01.xsd")
    package = "defxml.models"
    runner = CliRunner()
    result = runner.invoke(cli, [str(schema), "--package", package])

    if result.exception:
        raise result.exception

    clazz = load_class(result.output, "Product")
    validate_bindings(schema, clazz)


def test_definitive_xml_schema_chapter_03():
    schema = here.joinpath("schemas/chapter03.xsd")
    package = "defxml.models"
    runner = CliRunner()
    result = runner.invoke(cli, [str(schema), "--package", package])

    if result.exception:
        raise result.exception

    clazz = load_class(result.output, "Envelope")
    validate_bindings(schema, clazz)


def test_definitive_xml_schema_chapter_04():
    schema = here.joinpath("schemas/chapter04.xsd")
    package = "defxml.models"
    runner = CliRunner()
    result = runner.invoke(cli, [str(schema), "--package", package])

    if result.exception:
        raise result.exception

    clazz = load_class(result.output, "Order")
    validate_bindings(schema, clazz)


def test_definitive_xml_schema_chapter_05():
    schema = here.joinpath("schemas/chapter05.xsd")
    package = "defxml.models"
    runner = CliRunner()
    result = runner.invoke(cli, [str(schema), "--package", package])

    if result.exception:
        raise result.exception

    clazz = load_class(result.output, "Order")
    validate_bindings(schema, clazz)


def test_definitive_xml_schema_chapter_08():
    schema = here.joinpath("schemas/chapter08.xsd")
    package = "defxml.models"
    runner = CliRunner()
    result = runner.invoke(cli, [str(schema), "--package", package])

    if result.exception:
        raise result.exception

    clazz = load_class(result.output, "Sizes")
    validate_bindings(schema, clazz)


def test_definitive_xml_schema_chapter_10():
    schema = here.joinpath("schemas/chapter10.xsd")
    package = "defxml.models"
    runner = CliRunner()
    result = runner.invoke(cli, [str(schema), "--package", package])

    if result.exception:
        raise result.exception

    clazz = load_class(result.output, "Sizes")
    validate_bindings(schema, clazz)


def test_definitive_xml_schema_chapter_12():
    schema = here.joinpath("schemas/chapter12.xsd")
    package = "defxml.models"
    runner = CliRunner()
    result = runner.invoke(
        cli, [str(schema), "--package", package, "--compound-fields"]
    )

    if result.exception:
        raise result.exception

    clazz = load_class(result.output, "Items")
    validate_bindings(schema, clazz)


def test_definitive_xml_schema_chapter_13():
    schema = here.joinpath("schemas/chapter13.xsd")
    package = "defxml.models"
    runner = CliRunner()
    result = runner.invoke(cli, [str(schema), "--package", package])

    if result.exception:
        raise result.exception

    clazz = load_class(result.output, "Items")
    validate_bindings(schema, clazz)


def test_definitive_xml_schema_chapter_15():
    schema = here.joinpath("schemas/chapter15.xsd")
    package = "defxml.models"
    runner = CliRunner()
    result = runner.invoke(cli, [str(schema), "--package", package])

    if result.exception:
        raise result.exception

    clazz = load_class(result.output, "Shirt")
    validate_bindings(schema, clazz)


def test_definitive_xml_schema_chapter_16():
    schema = here.joinpath("schemas/chapter16.xsd")
    package = "defxml.models"
    runner = CliRunner()
    result = runner.invoke(cli, [str(schema), "--package", package])

    if result.exception:
        raise result.exception

    clazz = load_class(result.output, "Items")
    validate_bindings(schema, clazz)


def test_definitive_xml_schema_chapter_17():
    schema = here.joinpath("schemas/chapter17.xsd")
    package = "defxml.models"
    runner = CliRunner()
    result = runner.invoke(
        cli, [str(schema), "--package", package, "--compound-fields"]
    )

    if result.exception:
        raise result.exception

    clazz = load_class(result.output, "Order")
    validate_bindings(schema, clazz)


def validate_bindings(schema: Path, clazz: Type):
    __tracebackhide__ = True

    chapter = schema.stem.replace("chapter", "")

    sample = here.joinpath(f"samples/chapter{chapter}.xml")
    output_xml = here.joinpath(f"output/chapter{chapter}.xsdata.xml")
    output_json = here.joinpath(f"output/chapter{chapter}.xsdata.json")

    obj = XmlParser().from_path(sample, clazz)
    config = SerializerConfig(pretty_print=True)

    actual_json = JsonSerializer(indent=4).render(obj)
    actual_xml = XmlSerializer(config=config).render(obj)

    if output_json.exists():
        assert output_json.read_text() == actual_json
        assert obj == JsonParser().from_string(actual_json, clazz)
    else:
        output_json.write_text(actual_json, encoding="utf-8")

    if output_xml.exists():
        assert output_xml.read_text() == actual_xml
    else:
        output_xml.write_text(actual_xml, encoding="utf-8")

    validator = etree.XMLSchema(etree.parse(str(schema)))
    validator.assertValid(etree.fromstring(actual_xml.encode()))
