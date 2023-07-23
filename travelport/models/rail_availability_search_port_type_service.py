from __future__ import annotations
from travelport.models.rail_availability_search_port_type_service_input import RailAvailabilitySearchPortTypeServiceInput
from travelport.models.rail_availability_search_port_type_service_output import RailAvailabilitySearchPortTypeServiceOutput

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class RailAvailabilitySearchPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/RailService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/RailService"
    input = RailAvailabilitySearchPortTypeServiceInput
    output = RailAvailabilitySearchPortTypeServiceOutput
