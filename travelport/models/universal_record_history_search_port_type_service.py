from __future__ import annotations
from travelport.models.universal_record_history_search_port_type_service_input import (
    UniversalRecordHistorySearchPortTypeServiceInput,
)
from travelport.models.universal_record_history_search_port_type_service_output import (
    UniversalRecordHistorySearchPortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class UniversalRecordHistorySearchPortTypeService:
    style = "document"
    location = (
        "http://localhost:8080/kestrel/UniversalRecordHistorySearchService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = (
        "http://localhost:8080/kestrel/UniversalRecordHistorySearchService"
    )
    input = UniversalRecordHistorySearchPortTypeServiceInput
    output = UniversalRecordHistorySearchPortTypeServiceOutput
