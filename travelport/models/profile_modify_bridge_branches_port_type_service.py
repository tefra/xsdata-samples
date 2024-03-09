from __future__ import annotations

from travelport.models.profile_modify_bridge_branches_port_type_service_input import (
    ProfileModifyBridgeBranchesPortTypeServiceInput,
)
from travelport.models.profile_modify_bridge_branches_port_type_service_output import (
    ProfileModifyBridgeBranchesPortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class ProfileModifyBridgeBranchesPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/UProfileService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/UProfileService"
    input = ProfileModifyBridgeBranchesPortTypeServiceInput
    output = ProfileModifyBridgeBranchesPortTypeServiceOutput
