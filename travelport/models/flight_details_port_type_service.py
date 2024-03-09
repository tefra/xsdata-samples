from __future__ import annotations

from travelport.models.flight_details_port_type_service_input import (
    FlightDetailsPortTypeServiceInput,
)
from travelport.models.flight_details_port_type_service_output import (
    FlightDetailsPortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class FlightDetailsPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/FlightService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/FlightService"
    input = FlightDetailsPortTypeServiceInput
    output = FlightDetailsPortTypeServiceOutput
