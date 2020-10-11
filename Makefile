all: build test mypy

build: build-amadeus build-sabre build-travelport build-common build-reqif

test: test-amadeus test-sabre test-travelport test-bnm test-reqif

mypy: mypy-common mypy-reqif

build-amadeus:
	rm -rf amadeus/models
	xsdata amadeus/schemas --config amadeus/.xsdata.xml

test-amadeus:
	pytest amadeus

build-sabre:
	rm -rf sabre/models
	xsdata sabre/schemas --package sabre.models

test-sabre:
	pytest sabre

build-travelport:
	rm -rf travelport/models
	xsdata travelport/schemas/air_v48_0/Air.wsdl --config travelport/.xsdata.xml

test-travelport:
	pytest travelport

test-bnm:
	pytest bnm

build-common:
	rm -rf common_types/models
	xsdata common_types/Common-Types/src/main/resources/schemas/nhinc/hl7 --config common_types/.xsdata.xml

mypy-common:
	mypy common_types

build-reqif:
	rm -rf reqif/models
	xsdata reqif/schemas/reqif.xsd --package reqif.models --ns-struct

test-reqif:
	pytest reqif

mypy-reqif:
	mypy reqif/models
