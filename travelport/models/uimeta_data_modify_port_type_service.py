from __future__ import annotations
from travelport.models.uimeta_data_modify_port_type_service_input import (
    UimetaDataModifyPortTypeServiceInput,
)
from travelport.models.uimeta_data_modify_port_type_service_output import (
    UimetaDataModifyPortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class UimetaDataModifyPortTypeService:
    style = "document"
    location = "http://localhost:9080/kestrel/UProfileSharedService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:9080/kestrel/UProfileSharedService"
    input = UimetaDataModifyPortTypeServiceInput
    output = UimetaDataModifyPortTypeServiceOutput
