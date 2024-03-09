from __future__ import annotations

from travelport.models.air_low_fare_search_port_type_service_input import (
    AirLowFareSearchPortTypeServiceInput,
)
from travelport.models.air_low_fare_search_port_type_service_output import (
    AirLowFareSearchPortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class AirLowFareSearchPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/AirService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/AirService"
    input = AirLowFareSearchPortTypeServiceInput
    output = AirLowFareSearchPortTypeServiceOutput
