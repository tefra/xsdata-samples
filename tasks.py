import asyncio
import sys
from typing import Iterator

from invoke import task, Context, Collection

# ANSI color codes for suite prefixes (similar to docker-compose)
COLORS = [
    "\033[36m",  # cyan
    "\033[33m",  # yellow
    "\033[32m",  # green
    "\033[35m",  # magenta
    "\033[34m",  # blue
    "\033[91m",  # bright red
    "\033[92m",  # bright green
    "\033[93m",  # bright yellow
    "\033[94m",  # bright blue
    "\033[95m",  # bright magenta
    "\033[96m",  # bright cyan
]
RESET = "\033[0m"

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


def get_suite(c: Context, suite: str | None = None) -> Iterator[str]:
    if suite:
        yield suite
    elif "suite" in c:
        yield c.suite
    else:
        yield from SUITES.keys()


def get_prefix(suite: str) -> str:
    """Get a colored prefix for a suite."""
    max_suite_len = max(len(s) for s in SUITES.keys())
    suite_index = list(SUITES.keys()).index(suite)
    color = COLORS[suite_index % len(COLORS)]
    return f"{color}[{suite:<{max_suite_len}}]{RESET}"


async def run_command_async(cmd: str, suite: str) -> bool:
    """Run a command asynchronously with prefixed output."""
    prefix = get_prefix(suite)

    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.STDOUT,
    )

    if proc.stdout:
        async for line in proc.stdout:
            text = line.decode().rstrip()
            print(f"{prefix} {text}", flush=True)

    await proc.wait()
    return proc.returncode == 0


async def run_suite_build(suite: str, build_cmd_args: str) -> bool:
    """Run build commands for a single suite."""
    prefix = get_prefix(suite)

    print(f"{prefix} Starting build...", flush=True)

    # Clean models directory
    success = await run_command_async(f"rm -rf {suite}/models", suite)
    if not success:
        print(f"{prefix} Failed to clean models directory", flush=True)
        return False

    # Run xsdata generate
    success = await run_command_async(
        f"xsdata generate {SUITES[suite]} --config {suite}/.xsdata.xml {build_cmd_args}",
        suite,
    )
    if not success:
        print(f"{prefix} Build failed!", flush=True)
        return False

    print(f"{prefix} Build completed successfully", flush=True)
    return True


async def run_suite_test(suite: str, output_format: str, dump_context: bool) -> bool:
    """Run tests for a single suite."""
    prefix = get_prefix(suite)

    print(f"{prefix} Running tests...", flush=True)

    build_cmd_args = f"--output-format {output_format}"
    if dump_context:
        build_cmd_args += "  --dump-context"

    success = await run_command_async(f"pytest {build_cmd_args} {suite}/", suite)
    if not success:
        print(f"{prefix} Tests failed!", flush=True)
        return False

    print(f"{prefix} Tests passed", flush=True)
    return True


async def run_suite_mypy(suite: str) -> bool:
    """Run mypy for a single suite."""
    if suite in ("generali", "sdmx_ml"):
        return True

    prefix = get_prefix(suite)

    print(f"{prefix} Running mypy...", flush=True)

    success = await run_command_async(f"mypy {suite}/models", suite)
    if not success:
        print(f"{prefix} mypy failed!", flush=True)
        return False

    print(f"{prefix} mypy passed", flush=True)
    return True


async def run_suite_all(
    suite: str, build_cmd_args: str, output_format: str, dump_context: bool
) -> bool:
    """Run all tasks for a single suite (build, test, mypy)."""
    if not await run_suite_build(suite, build_cmd_args):
        return False
    if not await run_suite_test(suite, output_format, dump_context):
        return False
    if not await run_suite_mypy(suite):
        return False
    return True


def print_summary(results: dict[str, bool], task_name: str) -> bool:
    """Print a summary of results and return overall success."""
    print("\n" + "=" * 60)
    print(f" {task_name.upper()} SUMMARY")
    print("=" * 60)

    passed = [s for s, ok in results.items() if ok]
    failed = [s for s, ok in results.items() if not ok]

    if passed:
        print(f"\n  Passed ({len(passed)}):")
        for s in passed:
            print(f"    - {s}")

    if failed:
        print(f"\n  Failed ({len(failed)}):")
        for s in failed:
            print(f"    - {s}")

    print("\n" + "=" * 60)
    print(f" Total: {len(passed)} passed, {len(failed)} failed")
    print("=" * 60 + "\n")

    return len(failed) == 0


@task
def build(
    c: Context,
    suite: str | None = None,
    output_format: str = "dataclasses",
    unnest_classes: bool = False,
    cache: bool = False,
    debug: bool = False,
):
    """Build all suites in parallel."""
    build_cmd_args = f"--output {output_format}"
    if unnest_classes:
        build_cmd_args += " --unnest-classes"
    if cache:
        build_cmd_args += " --cache"
    if debug:
        build_cmd_args += " --debug"

    suites = list(get_suite(c, suite))

    async def run_all():
        tasks = [run_suite_build(s, build_cmd_args) for s in suites]
        results = await asyncio.gather(*tasks)
        return dict(zip(suites, results))

    results = asyncio.run(run_all())
    success = print_summary(results, "build")
    if not success:
        sys.exit(1)


@task
def test(
    c: Context,
    suite: str | None = None,
    output_format: str = "dataclasses",
    dump_context: bool = False,
):
    """Run tests for all suites in parallel."""
    suites = list(get_suite(c, suite))

    async def run_all():
        tasks = [run_suite_test(s, output_format, dump_context) for s in suites]
        results = await asyncio.gather(*tasks)
        return dict(zip(suites, results))

    results = asyncio.run(run_all())
    success = print_summary(results, "test")
    if not success:
        sys.exit(1)


@task
def mypy(c: Context, suite: str | None = None):
    """Run mypy for all suites in parallel."""
    suites = list(get_suite(c, suite))

    async def run_all():
        tasks = [run_suite_mypy(s) for s in suites]
        results = await asyncio.gather(*tasks)
        return dict(zip(suites, results))

    results = asyncio.run(run_all())
    success = print_summary(results, "mypy")
    if not success:
        sys.exit(1)


@task(name="all")
def all_tasks(
    c: Context,
    suite: str | None = None,
    output_format: str = "dataclasses",
    unnest_classes: bool = False,
    cache: bool = False,
    debug: bool = False,
    dump_context: bool = False,
):
    """Run build, test, and mypy for all suites in parallel."""
    build_cmd_args = f"--output {output_format}"
    if unnest_classes:
        build_cmd_args += " --unnest-classes"
    if cache:
        build_cmd_args += " --cache"
    if debug:
        build_cmd_args += " --debug"

    suites = list(get_suite(c, suite))

    async def run_all():
        tasks = [
            run_suite_all(s, build_cmd_args, output_format, dump_context)
            for s in suites
        ]
        results = await asyncio.gather(*tasks)
        return dict(zip(suites, results))

    results = asyncio.run(run_all())
    success = print_summary(results, "all (build + test + mypy)")
    if not success:
        sys.exit(1)


@task
def config(c: Context, suite: str | None = None):
    """Initialize xsdata config for suites."""
    from functools import partial

    run = partial(c.run, pty=True, echo=True)
    for s in get_suite(c, suite):
        run(f"xsdata init-config {s}/.xsdata.xml")


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
    collection.add_task(all_tasks, default=True)
    collection.configure({"suite": key})
    ns.add_collection(collection)
