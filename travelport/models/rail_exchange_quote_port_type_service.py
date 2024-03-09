from __future__ import annotations

from travelport.models.rail_exchange_quote_port_type_service_input import (
    RailExchangeQuotePortTypeServiceInput,
)
from travelport.models.rail_exchange_quote_port_type_service_output import (
    RailExchangeQuotePortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class RailExchangeQuotePortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/RailService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/RailService"
    input = RailExchangeQuotePortTypeServiceInput
    output = RailExchangeQuotePortTypeServiceOutput
