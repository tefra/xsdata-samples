from __future__ import annotations
from travelport.models.air_void_document_port_type_service_input import (
    AirVoidDocumentPortTypeServiceInput,
)
from travelport.models.air_void_document_port_type_service_output import (
    AirVoidDocumentPortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class AirVoidDocumentPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/AirService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/AirService"
    input = AirVoidDocumentPortTypeServiceInput
    output = AirVoidDocumentPortTypeServiceOutput
