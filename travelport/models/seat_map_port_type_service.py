from __future__ import annotations

from travelport.models.seat_map_port_type_service_input import (
    SeatMapPortTypeServiceInput,
)
from travelport.models.seat_map_port_type_service_output import (
    SeatMapPortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class SeatMapPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/AirService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/AirService"
    input = SeatMapPortTypeServiceInput
    output = SeatMapPortTypeServiceOutput
