from __future__ import annotations

from travelport.models.reference_data_retrieve_port_type_service_input import (
    ReferenceDataRetrievePortTypeServiceInput,
)
from travelport.models.reference_data_retrieve_port_type_service_output import (
    ReferenceDataRetrievePortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class ReferenceDataRetrievePortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/UtilService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/UtilService"
    input = ReferenceDataRetrievePortTypeServiceInput
    output = ReferenceDataRetrievePortTypeServiceOutput
