from __future__ import annotations
from travelport.models.air_cancel_port_type_service_input import AirCancelPortTypeServiceInput
from travelport.models.air_cancel_port_type_service_output import AirCancelPortTypeServiceOutput

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class AirCancelPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/AirService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/AirService"
    input = AirCancelPortTypeServiceInput
    output = AirCancelPortTypeServiceOutput
