from __future__ import annotations
from travelport.models.air_pre_pay_port_type_service_input import AirPrePayPortTypeServiceInput
from travelport.models.air_pre_pay_port_type_service_output import AirPrePayPortTypeServiceOutput

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class AirPrePayPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/AirService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/AirService"
    input = AirPrePayPortTypeServiceInput
    output = AirPrePayPortTypeServiceOutput
