from __future__ import annotations

from travelport.models.booking_air_exchange_port_type_service_input import (
    BookingAirExchangePortTypeServiceInput,
)
from travelport.models.booking_air_exchange_port_type_service_output import (
    BookingAirExchangePortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class BookingAirExchangePortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/SharedBookingService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/SharedBookingService"
    input = BookingAirExchangePortTypeServiceInput
    output = BookingAirExchangePortTypeServiceOutput
