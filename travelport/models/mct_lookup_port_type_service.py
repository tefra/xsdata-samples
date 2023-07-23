from __future__ import annotations
from travelport.models.mct_lookup_port_type_service_input import MctLookupPortTypeServiceInput
from travelport.models.mct_lookup_port_type_service_output import MctLookupPortTypeServiceOutput

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class MctLookupPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/UtilService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/UtilService"
    input = MctLookupPortTypeServiceInput
    output = MctLookupPortTypeServiceOutput
