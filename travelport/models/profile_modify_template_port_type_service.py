from __future__ import annotations

from travelport.models.profile_modify_template_port_type_service_input import (
    ProfileModifyTemplatePortTypeServiceInput,
)
from travelport.models.profile_modify_template_port_type_service_output import (
    ProfileModifyTemplatePortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class ProfileModifyTemplatePortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/UProfileService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/UProfileService"
    input = ProfileModifyTemplatePortTypeServiceInput
    output = ProfileModifyTemplatePortTypeServiceOutput
