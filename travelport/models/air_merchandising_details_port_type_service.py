from __future__ import annotations
from travelport.models.air_merchandising_details_port_type_service_input import AirMerchandisingDetailsPortTypeServiceInput
from travelport.models.air_merchandising_details_port_type_service_output import AirMerchandisingDetailsPortTypeServiceOutput

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class AirMerchandisingDetailsPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/AirService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/AirService"
    input = AirMerchandisingDetailsPortTypeServiceInput
    output = AirMerchandisingDetailsPortTypeServiceOutput
