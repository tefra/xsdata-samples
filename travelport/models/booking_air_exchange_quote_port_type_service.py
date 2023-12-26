from __future__ import annotations
from travelport.models.booking_air_exchange_quote_port_type_service_input import (
    BookingAirExchangeQuotePortTypeServiceInput,
)
from travelport.models.booking_air_exchange_quote_port_type_service_output import (
    BookingAirExchangeQuotePortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class BookingAirExchangeQuotePortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/SharedBookingService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/SharedBookingService"
    input = BookingAirExchangeQuotePortTypeServiceInput
    output = BookingAirExchangeQuotePortTypeServiceOutput
