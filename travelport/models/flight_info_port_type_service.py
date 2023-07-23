from __future__ import annotations
from travelport.models.flight_info_port_type_service_input import FlightInfoPortTypeServiceInput
from travelport.models.flight_info_port_type_service_output import FlightInfoPortTypeServiceOutput

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class FlightInfoPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/FlightService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/FlightService"
    input = FlightInfoPortTypeServiceInput
    output = FlightInfoPortTypeServiceOutput
