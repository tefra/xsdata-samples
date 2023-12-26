from __future__ import annotations
from travelport.models.rail_seat_map_port_type_service_input import (
    RailSeatMapPortTypeServiceInput,
)
from travelport.models.rail_seat_map_port_type_service_output import (
    RailSeatMapPortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class RailSeatMapPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/RailService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/RailService"
    input = RailSeatMapPortTypeServiceInput
    output = RailSeatMapPortTypeServiceOutput
