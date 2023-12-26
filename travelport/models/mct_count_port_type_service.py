from __future__ import annotations
from travelport.models.mct_count_port_type_service_input import (
    MctCountPortTypeServiceInput,
)
from travelport.models.mct_count_port_type_service_output import (
    MctCountPortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class MctCountPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/UtilService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/UtilService"
    input = MctCountPortTypeServiceInput
    output = MctCountPortTypeServiceOutput
