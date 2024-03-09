from __future__ import annotations

from travelport.models.profile_create_hierarchy_level_port_type_service_input import (
    ProfileCreateHierarchyLevelPortTypeServiceInput,
)
from travelport.models.profile_create_hierarchy_level_port_type_service_output import (
    ProfileCreateHierarchyLevelPortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class ProfileCreateHierarchyLevelPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/UProfileService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/UProfileService"
    input = ProfileCreateHierarchyLevelPortTypeServiceInput
    output = ProfileCreateHierarchyLevelPortTypeServiceOutput
