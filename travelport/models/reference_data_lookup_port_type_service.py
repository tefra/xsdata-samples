from __future__ import annotations
from travelport.models.reference_data_lookup_port_type_service_input import (
    ReferenceDataLookupPortTypeServiceInput,
)
from travelport.models.reference_data_lookup_port_type_service_output import (
    ReferenceDataLookupPortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class ReferenceDataLookupPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/ReferenceDataLookupService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/ReferenceDataLookupService"
    input = ReferenceDataLookupPortTypeServiceInput
    output = ReferenceDataLookupPortTypeServiceOutput
