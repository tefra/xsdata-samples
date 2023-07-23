from __future__ import annotations
from travelport.models.universal_record_modify_service_port_type_service_input import UniversalRecordModifyServicePortTypeServiceInput
from travelport.models.universal_record_modify_service_port_type_service_output import UniversalRecordModifyServicePortTypeServiceOutput

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class UniversalRecordModifyServicePortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/UniversalRecordService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/UniversalRecordService"
    input = UniversalRecordModifyServicePortTypeServiceInput
    output = UniversalRecordModifyServicePortTypeServiceOutput
