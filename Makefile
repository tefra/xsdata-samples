OUTPUT_FORMAT ?= dataclasses

build-amadeus: schema = amadeus/schemas
build-autosar: schema = autosar/schemas/AUTOSAR_00049_COMPACT.xsd
build-bpmn: schema = bpmn/schemas/BPMN20.xsd
build-common_types: schema = common_types/Common-Types/src/main/resources/schemas/nhinc/hl7
build-datexii: schema = datexii/schemas
build-ewp: schema = ewp/schemas/ewp-specs-api-discovery/stable-v5/manifest.xsd
build-generali: schema = generali/schemas -r
build-netex: schema = netex/NeTEx/xsd/NeTEx_publication.xsd
build-npo: schema = npo/schemas/rs.poms.omroep.nl/v1/schema/api_2013.xsd
build-reqif: schema = reqif/schemas/reqif.xsd
build-sabre: schema = sabre/schemas
build-spacex: schema = spacex/launches.json
build-travelport: schema = travelport/schemas/air_v48_0/Air.wsdl
build-ubl: schema = ubl/schemas/maindoc

builds = $\
	build-amadeus $\
	build-autosar $\
	build-bpmn $\
	build-common_types $\
	build-datexii $\
	build-ewp $\
	build-generali $\
	build-netex $\
	build-npo $\
	build-reqif $\
	build-sabre $\
	build-spacex $\
	build-travelport $\
	build-ubl

tests = $\
	test-amadeus $\
	test-autosar $\
	test-bpmn $\
	test-common_types $\
	test-datexii $\
	test-defxml $\
	test-ewp $\
	test-generali $\
	test-netex $\
	test-npo $\
	test-reqif $\
	test-sabre $\
	test-spacex $\
	test-travelport $\
	test-ubl

mypies = $\
	mypy-amadeus $\
	mypy-autosar $\
	mypy-bpmn $\
	mypy-common_types $\
	mypy-datexii $\
	mypy-defxml $\
	mypy-ewp $\
	mypy-generali $\
	mypy-netex $\
	mypy-npo $\
	mypy-reqif $\
	mypy-sabre $\
	mypy-spacex $\
	mypy-travelport $\
	mypy-ubl

init-configs = $\
	init-config-amadeus $\
	init-config-autosar $\
	init-config-bpmn $\
	init-config-common_types $\
	init-config-datexii $\
	init-config-defxml $\
	init-config-ewp $\
	init-config-generali $\
	init-config-netex $\
	init-config-npo $\
	init-config-reqif $\
	init-config-sabre $\
	init-config-spacex $\
	init-config-travelport $\
	init-config-ubl

all: $(builds) $(tests) $(mypies)

amadeus: build-amadeus test-amadeus mypy-amadeus
autosar: build-autosar test-autosar mypy-autosar
bpmn: build-bpmn test-bpmn mypy-bpmn
common_types: build-common_types test-common_types mypy-common_types
datexii: build-datexii test-datexii mypy-datexii
defxml: test-defxml mypy-defxml
ewp: build-ewp test-ewp mypy-ewp
generali: build-generali test-generali mypy-generali
netex: build-netex test-netex mypy-netex
npo: build-npo test-npo mypy-npo
reqif: build-reqif test-reqif mypy-reqif
sabre: build-sabre test-sabre mypy-sabre
spacex: build-spacex test-spacex mypy-spacex
travelport: build-travelport test-travelport mypy-travelport
ubl: build-ubl test-ubl mypy-ubl

build: $(builds)
test: $(tests)
mypy: $(mypies)
init-config: $(init-configs)

build-%:
	@echo "**** Generating models: $* ****"
	@rm -rf $*/models
	xsdata $(schema) --config $*/.xsdata.xml --output $(OUTPUT_FORMAT)

test-%:
	@echo "**** Running tests: $* ****"
	pytest --output-format $(OUTPUT_FORMAT) $*/

mypy-%:
	@echo "**** Running static analysis: $* ****"
	mypy $*/models

init-config-%:
	xsdata init-config $*/.xsdata.xml