from __future__ import annotations
from travelport.models.single_profile_migration_port_type_service_input import (
    SingleProfileMigrationPortTypeServiceInput,
)
from travelport.models.single_profile_migration_port_type_service_output import (
    SingleProfileMigrationPortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class SingleProfileMigrationPortTypeService:
    style = "document"
    location = "http://localhost:9080/kestrel/UProfileService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:9080/kestrel/UProfileSharedService"
    input = SingleProfileMigrationPortTypeServiceInput
    output = SingleProfileMigrationPortTypeServiceOutput
