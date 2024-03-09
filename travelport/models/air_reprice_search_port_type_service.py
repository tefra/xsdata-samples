from __future__ import annotations

from travelport.models.air_reprice_search_port_type_service_input import (
    AirRepriceSearchPortTypeServiceInput,
)
from travelport.models.air_reprice_search_port_type_service_output import (
    AirRepriceSearchPortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class AirRepriceSearchPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/AirService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/AirService"
    input = AirRepriceSearchPortTypeServiceInput
    output = AirRepriceSearchPortTypeServiceOutput
