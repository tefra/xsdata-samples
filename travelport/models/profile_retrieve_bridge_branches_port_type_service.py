from __future__ import annotations

from travelport.models.profile_retrieve_bridge_branches_port_type_service_input import (
    ProfileRetrieveBridgeBranchesPortTypeServiceInput,
)
from travelport.models.profile_retrieve_bridge_branches_port_type_service_output import (
    ProfileRetrieveBridgeBranchesPortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class ProfileRetrieveBridgeBranchesPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/UProfileService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/UProfileService"
    input = ProfileRetrieveBridgeBranchesPortTypeServiceInput
    output = ProfileRetrieveBridgeBranchesPortTypeServiceOutput
