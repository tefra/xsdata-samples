from __future__ import annotations

from travelport.models.reference_data_update_port_type_service_input import (
    ReferenceDataUpdatePortTypeServiceInput,
)
from travelport.models.reference_data_update_port_type_service_output import (
    ReferenceDataUpdatePortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class ReferenceDataUpdatePortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/UtilService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/UtilService"
    input = ReferenceDataUpdatePortTypeServiceInput
    output = ReferenceDataUpdatePortTypeServiceOutput
