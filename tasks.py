from functools import partial
from typing import Optional, Iterator

from invoke import task, Context, Collection

SUITES = {
    "amadeus": "amadeus/schemas",
    "autosar": "autosar/schemas/AUTOSAR_00049_COMPACT.xsd",
    "bpmn": "bpmn/schemas/BPMN20.xsd",
    "common_types": "common_types/Common-Types/src/main/resources/schemas/nhinc/hl7",
    "crossref": "crossref/schema/schemas/crossref5.3.1.xsd",
    "datexii": "datexii/schemas",
    "ewp": "ewp/schemas/ewp-specs-api-discovery/stable-v5/manifest.xsd",
    "generali": "generali/schemas -r",
    "ipxact": "ipxact/schemas/index.xsd",
    "netex": "netex/NeTEx/xsd/NeTEx_publication.xsd",
    "npo": "npo/schemas/rs.poms.omroep.nl/v1/schema/api_2013.xsd",
    "reqif": "reqif/schemas/reqif.xsd",
    "sabre": "sabre/schemas",
    "sdmx_ml": "sdmx_ml/repo/schemas/ -r",
    "spacex": "spacex/launches.json",
    "tpdb": "tpdb/repo/xml/xtc.xsd",
    "travelport": "travelport/schemas -r",
    "ubl": "ubl/schemas/maindoc",
    "voko": "voko/dtd",
    "xcbl": "xcbl/schemas",
}


def get_suite(c: Context, suite: Optional[str] = None) -> Iterator[str]:
    if suite:
        yield suite
    elif "suite" in c:
        yield c.suite
    else:
        yield from SUITES.keys()


@task
def build(
    c: Context,
    suite: Optional[str] = None,
    output_format: str = "dataclasses",
    unnest_classes: bool = False,
    cache: bool = False,
    debug: bool = False,
):
    run = partial(c.run, pty=True, echo=True)
    build_cmd_args = f"--output {output_format}"
    if unnest_classes:
        build_cmd_args += " --unnest-classes"
    if cache:
        build_cmd_args += " --cache"
    if debug:
        build_cmd_args += " --debug"

    for s in get_suite(c, suite):
        run(f"rm -rf {s}/models")
        run(f"xsdata generate {SUITES[s]} --config {s}/.xsdata.xml {build_cmd_args}")


@task
def test(c: Context, suite: Optional[str] = None, output_format="dataclasses"):
    run = partial(c.run, pty=True, echo=True)
    for s in get_suite(c, suite):
        run(f"pytest --output-format {output_format} {s}/")


@task
def mypy(c: Context, suite: Optional[str] = None):
    run = partial(c.run, pty=True, echo=True)
    for s in get_suite(c, suite):
        run(f"mypy {s}/models")


@task
def config(c: Context, suite: Optional[str] = None):
    run = partial(c.run, pty=True, echo=True)
    for s in get_suite(c, suite):
        run(f"xsdata init-config {s}/.xsdata.xml")


@task(name="all")
def all_tasks(
    c: Context,
    suite: Optional[str] = None,
    output_format: str = "dataclasses",
    unnest_classes: bool = False,
    cache: bool = False,
    debug: bool = False,
):
    run = partial(c.run, pty=True, echo=True)

    build_cmd_args = f"--output {output_format}"
    if unnest_classes:
        build_cmd_args += " --unnest-classes"
    if cache:
        build_cmd_args += " --cache"
    if debug:
        build_cmd_args += " --debug"

    for s in get_suite(c, suite):
        run(f"rm -rf {s}/models")
        run(f"xsdata generate {SUITES[s]} --config {s}/.xsdata.xml {build_cmd_args}")
        run(f"pytest --output-format {output_format} {s}/")

        if s not in ("generali", "sdmx_ml"):
            run(f"mypy {s}/models")


ns = Collection()
ns.add_task(all_tasks)
ns.add_task(build)
ns.add_task(mypy)
ns.add_task(test)
ns.add_task(config)

for key in SUITES.keys():
    collection = Collection(key)
    collection.add_task(build)
    collection.add_task(test)
    collection.add_task(mypy)
    collection.add_task(all_tasks)
    collection.configure({"suite": key})
    ns.add_collection(collection)
