from __future__ import annotations
from travelport.models.rail_refund_port_type_service_input import RailRefundPortTypeServiceInput
from travelport.models.rail_refund_port_type_service_output import RailRefundPortTypeServiceOutput

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class RailRefundPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/RailService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/RailService"
    input = RailRefundPortTypeServiceInput
    output = RailRefundPortTypeServiceOutput
