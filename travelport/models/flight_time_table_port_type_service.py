from __future__ import annotations
from travelport.models.flight_time_table_port_type_service_input import (
    FlightTimeTablePortTypeServiceInput,
)
from travelport.models.flight_time_table_port_type_service_output import (
    FlightTimeTablePortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class FlightTimeTablePortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/AirService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/AirService"
    input = FlightTimeTablePortTypeServiceInput
    output = FlightTimeTablePortTypeServiceOutput
