from __future__ import annotations
from travelport.models.air_merchandising_fulfillment_port_type_service_input import (
    AirMerchandisingFulfillmentPortTypeServiceInput,
)
from travelport.models.air_merchandising_fulfillment_port_type_service_output import (
    AirMerchandisingFulfillmentPortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class AirMerchandisingFulfillmentPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/AirService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/AirService"
    input = AirMerchandisingFulfillmentPortTypeServiceInput
    output = AirMerchandisingFulfillmentPortTypeServiceOutput
