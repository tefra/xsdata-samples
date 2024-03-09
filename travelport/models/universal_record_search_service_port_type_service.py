from __future__ import annotations

from travelport.models.universal_record_search_service_port_type_service_input import (
    UniversalRecordSearchServicePortTypeServiceInput,
)
from travelport.models.universal_record_search_service_port_type_service_output import (
    UniversalRecordSearchServicePortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class UniversalRecordSearchServicePortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/UniversalRecordService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/UniversalRecordService"
    input = UniversalRecordSearchServicePortTypeServiceInput
    output = UniversalRecordSearchServicePortTypeServiceOutput
