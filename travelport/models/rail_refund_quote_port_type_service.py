from __future__ import annotations
from travelport.models.rail_refund_quote_port_type_service_input import RailRefundQuotePortTypeServiceInput
from travelport.models.rail_refund_quote_port_type_service_output import RailRefundQuotePortTypeServiceOutput

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class RailRefundQuotePortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/RailService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/RailService"
    input = RailRefundQuotePortTypeServiceInput
    output = RailRefundQuotePortTypeServiceOutput
