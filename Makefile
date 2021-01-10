build-amadeus: schema = amadeus/schemas
build-sabre: schema = sabre/schemas
build-travelport: schema = travelport/schemas/air_v48_0/Air.wsdl
build-common_types: schema = common_types/Common-Types/src/main/resources/schemas/nhinc/hl7
build-reqif: schema = reqif/schemas/reqif.xsd
build-npo: schema = npo/schemas/rs.poms.omroep.nl/v1/schema/urn:vpro:api:2013
build-datexii: schema = datexii/schemas

builds = $\
	build-amadeus $\
	build-sabre $\
	build-travelport $\
	build-common_types $\
	build-reqif $\
	build-npo $\
	build-datexii

tests = $\
	test-amadeus $\
	test-sabre $\
	test-travelport $\
	test-reqif $\
	test-npo $\
	test-datexii $\
	test-bnm

mypies = $\
	mypy-amadeus $\
	mypy-sabre $\
	mypy-travelport $\
	mypy-common_types $\
	mypy-reqif $\
	mypy-npo $\
	mypy-datexii

all: $(builds) $(tests) $(mypies)

amadeus: build-amadeus test-amadeus mypy-amadeus
sabre: build-sabre test-sabre mypy-sabre
travelport: build-travelport test-travelport mypy-travelport
common_types: build-common_types test-common_types mypy-common_types
reqif: build-reqif test-reqif mypy-reqif
npo: build-npo test-npo mypy-npo
datexii: build-datexii test-datexii mypy-datexii

build: $(builds)
test: $(tests)
mypy: $(mypies)

build-%:
	@echo "**** Generating models: $* ****"
	@rm -rf $*/models
	@xsdata $(schema) --config $*/.xsdata.xml

test-%:
	@echo "**** Running tests: $* ****"
	pytest $*/

mypy-%:
	@echo "**** Running static analysis: $* ****"
	mypy $*/models
