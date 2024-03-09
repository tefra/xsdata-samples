from __future__ import annotations

from travelport.models.hotel_details_service_port_type_service_input import (
    HotelDetailsServicePortTypeServiceInput,
)
from travelport.models.hotel_details_service_port_type_service_output import (
    HotelDetailsServicePortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class HotelDetailsServicePortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/HotelService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/HotelService"
    input = HotelDetailsServicePortTypeServiceInput
    output = HotelDetailsServicePortTypeServiceOutput
