from __future__ import annotations
from travelport.models.profile_delete_port_type_service_input import ProfileDeletePortTypeServiceInput
from travelport.models.profile_delete_port_type_service_output import ProfileDeletePortTypeServiceOutput

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class ProfileDeletePortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/UProfileService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:9080/kestrel/UProfileSharedService"
    input = ProfileDeletePortTypeServiceInput
    output = ProfileDeletePortTypeServiceOutput
