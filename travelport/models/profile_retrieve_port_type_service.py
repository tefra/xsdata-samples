from __future__ import annotations

from travelport.models.profile_retrieve_port_type_service_input import (
    ProfileRetrievePortTypeServiceInput,
)
from travelport.models.profile_retrieve_port_type_service_output import (
    ProfileRetrievePortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class ProfileRetrievePortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/UProfileService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:9080/kestrel/UProfileSharedService"
    input = ProfileRetrievePortTypeServiceInput
    output = ProfileRetrievePortTypeServiceOutput
