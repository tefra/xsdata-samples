from __future__ import annotations
from travelport.models.profile_modify_tags_port_type_service_input import ProfileModifyTagsPortTypeServiceInput
from travelport.models.profile_modify_tags_port_type_service_output import ProfileModifyTagsPortTypeServiceOutput

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class ProfileModifyTagsPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/UProfileService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:9080/kestrel/UProfileSharedService"
    input = ProfileModifyTagsPortTypeServiceInput
    output = ProfileModifyTagsPortTypeServiceOutput
