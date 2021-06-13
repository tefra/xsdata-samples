OUTPUT_FORMAT ?= dataclasses

build-amadeus: schema = amadeus/schemas
build-sabre: schema = sabre/schemas
build-travelport: schema = travelport/schemas/air_v48_0/Air.wsdl
build-common_types: schema = common_types/Common-Types/src/main/resources/schemas/nhinc/hl7
build-reqif: schema = reqif/schemas/reqif.xsd
build-npo: schema = npo/schemas/rs.poms.omroep.nl/v1/schema/api_2013.xsd
build-datexii: schema = datexii/schemas
build-ewp: schema = ewp/schemas/ewp-specs-api-discovery/stable-v5/manifest.xsd
build-ubl: schema = ubl/schemas/maindoc
build-netex: schema = netex/NeTEx/xsd/NeTEx_publication.xsd
build-spacex: schema = spacex/launches.json
build-autosar: schema = autosar/schemas/AUTOSAR_00049_COMPACT.xsd

builds = $\
	build-amadeus $\
	build-sabre $\
	build-travelport $\
	build-common_types $\
	build-reqif $\
	build-npo $\
	build-datexii $\
	build-ewp $\
	build-ubl $\
	build-spacex $\
	build-autosar $\
	build-netex

tests = $\
	test-amadeus $\
	test-sabre $\
	test-travelport $\
	test-common_types $\
	test-reqif $\
	test-npo $\
	test-datexii $\
	test-ewp $\
	test-ubl $\
	test-defxml $\
	test-spacex $\
	test-autosar $\
	test-netex

mypies = $\
	mypy-amadeus $\
	mypy-sabre $\
	mypy-travelport $\
	mypy-common_types $\
	mypy-reqif $\
	mypy-npo $\
	mypy-datexii $\
	mypy-ewp $\
	mypy-ubl $\
	mypy-defxml $\
	mypy-spacex $\
	mypy-autosar $\
	mypy-netex

all: $(builds) $(tests) $(mypies)

amadeus: build-amadeus test-amadeus mypy-amadeus
sabre: build-sabre test-sabre mypy-sabre
travelport: build-travelport test-travelport mypy-travelport
common_types: build-common_types test-common_types mypy-common_types
reqif: build-reqif test-reqif mypy-reqif
npo: build-npo test-npo mypy-npo
datexii: build-datexii test-datexii mypy-datexii
ewp: build-ewp test-ewp mypy-ewp
ubl: build-ubl test-ubl mypy-ubl
netex: build-netex test-netex mypy-netex
defxml: test-defxml mypy-defxml
spacex: build-spacex test-spacex mypy-spacex
autosar: build-autosar test-autosar mypy-autosar

build: $(builds)
test: $(tests)
mypy: $(mypies)

build-%:
	echo "**** Generating models: $* ****"
	rm -rf $*/models
	xsdata $(schema) --config $*/.xsdata.xml --output $(OUTPUT_FORMAT)

test-%:
	echo "**** Running tests: $* ****"
	pytest --output-format $(OUTPUT_FORMAT) $*/

mypy-%:
	echo "**** Running static analysis: $* ****"
	mypy $*/models
