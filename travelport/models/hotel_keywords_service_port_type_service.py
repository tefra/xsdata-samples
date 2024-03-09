from __future__ import annotations

from travelport.models.hotel_keywords_service_port_type_service_input import (
    HotelKeywordsServicePortTypeServiceInput,
)
from travelport.models.hotel_keywords_service_port_type_service_output import (
    HotelKeywordsServicePortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class HotelKeywordsServicePortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/HotelService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/HotelService"
    input = HotelKeywordsServicePortTypeServiceInput
    output = HotelKeywordsServicePortTypeServiceOutput
