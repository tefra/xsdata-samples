from __future__ import annotations
from travelport.models.uimeta_data_delete_port_type_service_input import (
    UimetaDataDeletePortTypeServiceInput,
)
from travelport.models.uimeta_data_delete_port_type_service_output import (
    UimetaDataDeletePortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class UimetaDataDeletePortTypeService:
    style = "document"
    location = "http://localhost:9080/kestrel/UProfileSharedService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:9080/kestrel/UProfileSharedService"
    input = UimetaDataDeletePortTypeServiceInput
    output = UimetaDataDeletePortTypeServiceOutput
