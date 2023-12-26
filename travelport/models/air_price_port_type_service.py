from __future__ import annotations
from travelport.models.air_price_port_type_service_input import (
    AirPricePortTypeServiceInput,
)
from travelport.models.air_price_port_type_service_output import (
    AirPricePortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class AirPricePortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/AirService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/AirService"
    input = AirPricePortTypeServiceInput
    output = AirPricePortTypeServiceOutput
