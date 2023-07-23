from __future__ import annotations
from travelport.models.air_upsell_search_port_type_service_input import AirUpsellSearchPortTypeServiceInput
from travelport.models.air_upsell_search_port_type_service_output import AirUpsellSearchPortTypeServiceOutput

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class AirUpsellSearchPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/AirService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/AirService"
    input = AirUpsellSearchPortTypeServiceInput
    output = AirUpsellSearchPortTypeServiceOutput
