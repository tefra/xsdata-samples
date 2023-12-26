from __future__ import annotations
from travelport.models.profile_modify_field_port_type_service_input import (
    ProfileModifyFieldPortTypeServiceInput,
)
from travelport.models.profile_modify_field_port_type_service_output import (
    ProfileModifyFieldPortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class ProfileModifyFieldPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/UProfileService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:9080/kestrel/UProfileSharedService"
    input = ProfileModifyFieldPortTypeServiceInput
    output = ProfileModifyFieldPortTypeServiceOutput
