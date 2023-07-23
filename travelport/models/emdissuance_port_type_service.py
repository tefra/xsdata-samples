from __future__ import annotations
from travelport.models.emdissuance_port_type_service_input import EmdissuancePortTypeServiceInput
from travelport.models.emdissuance_port_type_service_output import EmdissuancePortTypeServiceOutput

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class EmdissuancePortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/AirService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/AirService"
    input = EmdissuancePortTypeServiceInput
    output = EmdissuancePortTypeServiceOutput
