#!/usr/bin/env python
import argparse
import subprocess
import sys

config = {
    "amadeus": "amadeus/schemas",
    "autosar": "autosar/schemas/AUTOSAR_00049_COMPACT.xsd",
    "bpmn": "bpmn/schemas/BPMN20.xsd",
    "common_types": "common_types/Common-Types/src/main/resources/schemas/nhinc/hl7",
    "crossref": "crossref/schema/schemas/crossref5.3.1.xsd",
    "datexii": "datexii/schemas",
    "ewp": "ewp/schemas/ewp-specs-api-discovery/stable-v5/manifest.xsd",
    "generali": "generali/schemas -r",
    "netex": "netex/NeTEx/xsd/NeTEx_publication.xsd",
    "npo": "npo/schemas/rs.poms.omroep.nl/v1/schema/api_2013.xsd",
    "reqif": "reqif/schemas/reqif.xsd",
    "sabre": "sabre/schemas",
    "spacex": "spacex/launches.json",
    "travelport": "travelport/schemas/air_v48_0/Air.wsdl",
    "ubl": "ubl/schemas/maindoc",
    "xcbl": "xcbl/schemas",
}

commands = ["all", "build", "test", "mypy", "init-config"]
suites = ["all"] + list(config.keys())

parser = argparse.ArgumentParser()
parser.add_argument("command", nargs="?", default="all", choices=commands)
parser.add_argument("suite", nargs="?", default="all", choices=suites)
parser.add_argument("--output-format", default="dataclasses")


def build(suite: str, output_format: str):
    print(f"**** Generating models: {suite} ****")
    subprocess.run(f"rm -rf {suite}/models", shell=True)
    schema = config[suite]
    subprocess.run(
        f"xsdata {schema} --config {suite}/.xsdata.xml --output {output_format}",
        shell=True,
    )


def test(suite: str, output_format: str):
    print(f"**** Running tests: {suite} ****")
    subprocess.run(f"pytest --output-format {output_format} {suite}/", shell=True)


def mypy(suite: str, *args):
    print(f"**** Running static analysis: {suite} ****")
    subprocess.run(f"mypy {suite}/models", shell=True)


def init_config(suite: str, *args):
    subprocess.run(f"xsdata init-config {suite}/.xsdata.xml", shell=True)


def all(suite: str, output_format: str):
    build(suite, output_format)
    test(suite, output_format)
    mypy(suite)


args = parser.parse_args()
cmd = getattr(sys.modules[__name__], args.command.replace("-", "_"))

if args.suite == "all":
    for suite in config:
        cmd(suite, args.output_format)
else:
    cmd(args.suite, args.output_format)
