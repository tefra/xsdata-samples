from __future__ import annotations

from travelport.models.profile_create_tags_port_type_service_input import (
    ProfileCreateTagsPortTypeServiceInput,
)
from travelport.models.profile_create_tags_port_type_service_output import (
    ProfileCreateTagsPortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class ProfileCreateTagsPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/UProfileService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:9080/kestrel/UProfileSharedService"
    input = ProfileCreateTagsPortTypeServiceInput
    output = ProfileCreateTagsPortTypeServiceOutput
