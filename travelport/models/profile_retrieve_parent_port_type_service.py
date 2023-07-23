from __future__ import annotations
from travelport.models.profile_retrieve_parent_port_type_service_input import ProfileRetrieveParentPortTypeServiceInput
from travelport.models.profile_retrieve_parent_port_type_service_output import ProfileRetrieveParentPortTypeServiceOutput

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class ProfileRetrieveParentPortTypeService:
    style = "document"
    location = "http://localhost:9080/kestrel/UProfileSharedService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:9080/kestrel/UProfileSharedService"
    input = ProfileRetrieveParentPortTypeServiceInput
    output = ProfileRetrieveParentPortTypeServiceOutput
