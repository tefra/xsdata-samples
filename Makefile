all: build test mypy

build: build-amadeus build-sabre build-travelport build-common build-reqif build-npo

test: test-amadeus test-sabre test-travelport test-bnm test-reqif test-npo

mypy: mypy-common mypy-reqif mypy-npo

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

mypy-travelport:
	mypy travelport/models

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

build-npo:
	rm -rf npo/models
	xsdata npo/schemas/rs.poms.omroep.nl/v1/schema/urn:vpro:api:2013 --package npo.models

test-npo:
	pytest npo/models

mypy-npo:
	mypy npm/models
