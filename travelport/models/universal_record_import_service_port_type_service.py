from __future__ import annotations
from travelport.models.universal_record_import_service_port_type_service_input import (
    UniversalRecordImportServicePortTypeServiceInput,
)
from travelport.models.universal_record_import_service_port_type_service_output import (
    UniversalRecordImportServicePortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class UniversalRecordImportServicePortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/UniversalRecordService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/UniversalRecordService"
    input = UniversalRecordImportServicePortTypeServiceInput
    output = UniversalRecordImportServicePortTypeServiceOutput
