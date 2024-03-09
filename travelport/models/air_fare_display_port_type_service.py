from __future__ import annotations

from travelport.models.air_fare_display_port_type_service_input import (
    AirFareDisplayPortTypeServiceInput,
)
from travelport.models.air_fare_display_port_type_service_output import (
    AirFareDisplayPortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class AirFareDisplayPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/AirService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/AirService"
    input = AirFareDisplayPortTypeServiceInput
    output = AirFareDisplayPortTypeServiceOutput
