from __future__ import annotations
from travelport.models.air_retrieve_document_port_type_service_input import (
    AirRetrieveDocumentPortTypeServiceInput,
)
from travelport.models.air_retrieve_document_port_type_service_output import (
    AirRetrieveDocumentPortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class AirRetrieveDocumentPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/AirService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/AirService"
    input = AirRetrieveDocumentPortTypeServiceInput
    output = AirRetrieveDocumentPortTypeServiceOutput
