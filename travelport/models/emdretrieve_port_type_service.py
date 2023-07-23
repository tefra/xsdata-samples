from __future__ import annotations
from travelport.models.emdretrieve_port_type_service_input import EmdretrievePortTypeServiceInput
from travelport.models.emdretrieve_port_type_service_output import EmdretrievePortTypeServiceOutput

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class EmdretrievePortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/AirService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/AirService"
    input = EmdretrievePortTypeServiceInput
    output = EmdretrievePortTypeServiceOutput
