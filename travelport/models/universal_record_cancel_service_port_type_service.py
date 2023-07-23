from __future__ import annotations
from travelport.models.universal_record_cancel_service_port_type_service_input import UniversalRecordCancelServicePortTypeServiceInput
from travelport.models.universal_record_cancel_service_port_type_service_output import UniversalRecordCancelServicePortTypeServiceOutput

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class UniversalRecordCancelServicePortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/UniversalRecordService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/UniversalRecordService"
    input = UniversalRecordCancelServicePortTypeServiceInput
    output = UniversalRecordCancelServicePortTypeServiceOutput
