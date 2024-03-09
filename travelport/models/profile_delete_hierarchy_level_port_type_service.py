from __future__ import annotations

from travelport.models.profile_delete_hierarchy_level_port_type_service_input import (
    ProfileDeleteHierarchyLevelPortTypeServiceInput,
)
from travelport.models.profile_delete_hierarchy_level_port_type_service_output import (
    ProfileDeleteHierarchyLevelPortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class ProfileDeleteHierarchyLevelPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/UProfileService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/UProfileService"
    input = ProfileDeleteHierarchyLevelPortTypeServiceInput
    output = ProfileDeleteHierarchyLevelPortTypeServiceOutput
