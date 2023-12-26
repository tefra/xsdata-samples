from __future__ import annotations
from travelport.models.air_refund_ticket_port_type_service_input import (
    AirRefundTicketPortTypeServiceInput,
)
from travelport.models.air_refund_ticket_port_type_service_output import (
    AirRefundTicketPortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class AirRefundTicketPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/AirService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/AirService"
    input = AirRefundTicketPortTypeServiceInput
    output = AirRefundTicketPortTypeServiceOutput
