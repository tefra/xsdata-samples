from __future__ import annotations
from travelport.models.air_availability_search_port_type_service_input import AirAvailabilitySearchPortTypeServiceInput
from travelport.models.air_availability_search_port_type_service_output import AirAvailabilitySearchPortTypeServiceOutput

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class AirAvailabilitySearchPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/AirService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/AirService"
    input = AirAvailabilitySearchPortTypeServiceInput
    output = AirAvailabilitySearchPortTypeServiceOutput
