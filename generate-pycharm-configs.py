from pathlib import Path

schemas = [
    "amadeus/schemas",
    "autosar/schemas/AUTOSAR_00049_COMPACT.xsd",
    "bpmn/schemas/BPMN20.xsd",
    "common_types/Common-Types/src/main/resources/schemas/nhinc/hl7",
    "crossref/schema/schemas/crossref5.3.1.xsd",
    "datexii/schemas",
    "ewp/schemas/ewp-specs-api-discovery/stable-v5/manifest.xsd",
    "generali/schemas -r",
    "netex/NeTEx/xsd/NeTEx_publication.xsd",
    "npo/schemas/rs.poms.omroep.nl/v1/schema/api_2013.xsd",
    "reqif/schemas/reqif.xsd",
    "sabre/schemas",
    "spacex/launches.json",
    "travelport/schemas/air_v48_0/Air.wsdl",
    "ubl/schemas/maindoc",
    "xcbl/schemas",
]


template = """<component name="ProjectRunConfigurationManager">
  <configuration default="false" name="{name}"
    type="PythonConfigurationType" factoryName="Python">
    <module name="xsdata" />
    <option name="INTERPRETER_OPTIONS" value="" />
    <option name="PARENT_ENVS" value="true" />
    <envs>
      <env name="PYTHONUNBUFFERED" value="1" />
    </envs>
    <option name="SDK_HOME" value="$USER_HOME$/.pyenv/versions/xsdata/bin/python" />
    <option name="WORKING_DIRECTORY" value="$PROJECT_DIR$/../xsdata-samples" />
    <option name="IS_MODULE_SDK" value="false" />
    <option name="ADD_CONTENT_ROOTS" value="true" />
    <option name="ADD_SOURCE_ROOTS" value="true" />
    <EXTENSION ID="PythonCoverageRunConfigurationExtension" runner="coverage.py" />
    <EXTENSION ID="net.ashald.envfile">
      <option name="IS_ENABLED" value="false" />
      <option name="IS_SUBST" value="false" />
      <option name="IS_PATH_MACRO_SUPPORTED" value="false" />
      <option name="IS_IGNORE_MISSING_FILES" value="false" />
      <option name="IS_ENABLE_EXPERIMENTAL_INTEGRATIONS" value="false" />
      <ENTRIES>
        <ENTRY IS_ENABLED="true" PARSER="runconfig" IS_EXECUTABLE="false" />
      </ENTRIES>
    </EXTENSION>
    <option name="SCRIPT_NAME" value="xsdata.cli" />
    <option name="PARAMETERS" value="generate {path} --config {name}/.xsdata.xml" />
    <option name="SHOW_COMMAND_LINE" value="false" />
    <option name="EMULATE_TERMINAL" value="false" />
    <option name="MODULE_MODE" value="true" />
    <option name="REDIRECT_INPUT" value="false" />
    <option name="INPUT_FILE" value="" />
    <method v="2" />
  </configuration>
</component>"""


dir = Path.cwd().joinpath(".run/")
dir.mkdir(exist_ok=True)
for schema in schemas:
    name, _ = schema.split("/", 1)
    result = template.format(name=name, path=schema)

    dir.joinpath(f"{name}.run.xml").write_text(result)
