from __future__ import annotations
from travelport.models.profile_search_action_port_type_service_input import ProfileSearchActionPortTypeServiceInput
from travelport.models.profile_search_action_port_type_service_output import ProfileSearchActionPortTypeServiceOutput

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class ProfileSearchActionPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/UProfileService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/UProfileService"
    input = ProfileSearchActionPortTypeServiceInput
    output = ProfileSearchActionPortTypeServiceOutput
