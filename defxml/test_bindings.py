import os
from pathlib import Path
from typing import Type

from click.testing import CliRunner
from lxml import etree
from xsdata.cli import cli
from xsdata.formats.dataclass.context import XmlContext
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


def test_definitive_xml_schema_chapter_01(output_format):
    schema = here.joinpath("schemas/chapter01.xsd")
    cli_output = generate(str(schema), output_format)

    clazz = load_class(cli_output, "Product")
    validate_bindings(schema, clazz, output_format)


def test_definitive_xml_schema_chapter_03(output_format):
    schema = here.joinpath("schemas/chapter03.xsd")
    cli_output = generate(str(schema), output_format)

    clazz = load_class(cli_output, "Envelope")
    validate_bindings(schema, clazz, output_format)


def test_definitive_xml_schema_chapter_04(output_format):
    schema = here.joinpath("schemas/chapter04.xsd")
    cli_output = generate(str(schema), output_format)

    clazz = load_class(cli_output, "Order")
    validate_bindings(schema, clazz, output_format)


def test_definitive_xml_schema_chapter_05(output_format):
    schema = here.joinpath("schemas/chapter05.xsd")
    cli_output = generate(str(schema), output_format)

    clazz = load_class(cli_output, "Order")
    validate_bindings(schema, clazz, output_format)


def test_definitive_xml_schema_chapter_08(output_format):
    schema = here.joinpath("schemas/chapter08.xsd")
    cli_output = generate(str(schema), output_format)

    clazz = load_class(cli_output, "Sizes")
    validate_bindings(schema, clazz, output_format)


def test_definitive_xml_schema_chapter_10(output_format):
    schema = here.joinpath("schemas/chapter10.xsd")
    cli_output = generate(str(schema), output_format)

    clazz = load_class(cli_output, "Sizes")
    validate_bindings(schema, clazz, output_format)


def test_definitive_xml_schema_chapter_12(output_format):
    schema = here.joinpath("schemas/chapter12.xsd")
    cli_output = generate(str(schema), output_format, compound_fields=True)

    clazz = load_class(cli_output, "Items")
    validate_bindings(schema, clazz, output_format)


def test_definitive_xml_schema_chapter_13(output_format):
    schema = here.joinpath("schemas/chapter13.xsd")
    cli_output = generate(str(schema), output_format)

    clazz = load_class(cli_output, "Items")
    validate_bindings(schema, clazz, output_format)


def test_definitive_xml_schema_chapter_15(output_format):
    schema = here.joinpath("schemas/chapter15.xsd")
    cli_output = generate(str(schema), output_format)

    clazz = load_class(cli_output, "Shirt")
    validate_bindings(schema, clazz, output_format)


def test_definitive_xml_schema_chapter_16(output_format):
    schema = here.joinpath("schemas/chapter16.xsd")
    cli_output = generate(str(schema), output_format)

    clazz = load_class(cli_output, "Items")
    validate_bindings(schema, clazz, output_format)


def test_definitive_xml_schema_chapter_17(output_format):
    schema = here.joinpath("schemas/chapter17.xsd")
    cli_output = generate(str(schema), output_format, compound_fields=True)

    clazz = load_class(cli_output, "Order")
    validate_bindings(schema, clazz, output_format)


def generate(source: str, output_format: str, compound_fields: bool = False) -> str:
    runner = CliRunner()
    args = [source, "--package=defxml.models", f"--output={output_format}"]

    if compound_fields:
        args.append("--compound-fields")

    result = runner.invoke(cli, args)

    if result.exception:
        raise result.exception

    return result.output


def validate_bindings(schema: Path, clazz: Type, output_format: str):
    __tracebackhide__ = True

    chapter = schema.stem.replace("chapter", "")

    sample = here.joinpath(f"samples/chapter{chapter}.xml")
    output_xml = here.joinpath(f"output/chapter{chapter}.xsdata.xml")
    output_json = here.joinpath(f"output/chapter{chapter}.xsdata.json")

    context = XmlContext(class_type=output_format)
    obj = XmlParser(context=context).from_path(sample, clazz)
    config = SerializerConfig(pretty_print=True)

    actual_json = JsonSerializer(context=context, indent=4).render(obj)
    actual_xml = XmlSerializer(context=context, config=config).render(obj)

    if output_json.exists():
        assert output_json.read_text() == actual_json
        assert obj == JsonParser(context=context).from_string(actual_json, clazz)
    else:
        output_json.write_text(actual_json, encoding="utf-8")

    if output_xml.exists():
        assert output_xml.read_text() == actual_xml
    else:
        output_xml.write_text(actual_xml, encoding="utf-8")

    validator = etree.XMLSchema(etree.parse(str(schema)))
    validator.assertValid(etree.fromstring(actual_xml.encode()))
