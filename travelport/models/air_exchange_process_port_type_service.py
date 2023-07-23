from __future__ import annotations
from travelport.models.air_exchange_process_port_type_service_input import AirExchangeProcessPortTypeServiceInput
from travelport.models.air_exchange_process_port_type_service_output import AirExchangeProcessPortTypeServiceOutput

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class AirExchangeProcessPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/AirService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/AirService"
    input = AirExchangeProcessPortTypeServiceInput
    output = AirExchangeProcessPortTypeServiceOutput
