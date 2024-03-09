from __future__ import annotations

from travelport.models.air_exchange_ticketing_port_type_service_input import (
    AirExchangeTicketingPortTypeServiceInput,
)
from travelport.models.air_exchange_ticketing_port_type_service_output import (
    AirExchangeTicketingPortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class AirExchangeTicketingPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/AirService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/AirService"
    input = AirExchangeTicketingPortTypeServiceInput
    output = AirExchangeTicketingPortTypeServiceOutput
