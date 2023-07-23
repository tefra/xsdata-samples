from __future__ import annotations
from travelport.models.profile_retrieve_action_port_type_service_input import ProfileRetrieveActionPortTypeServiceInput
from travelport.models.profile_retrieve_action_port_type_service_output import ProfileRetrieveActionPortTypeServiceOutput

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class ProfileRetrieveActionPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/UProfileService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/UProfileService"
    input = ProfileRetrieveActionPortTypeServiceInput
    output = ProfileRetrieveActionPortTypeServiceOutput
