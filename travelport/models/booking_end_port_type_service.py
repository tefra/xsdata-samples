from __future__ import annotations
from travelport.models.booking_end_port_type_service_input import (
    BookingEndPortTypeServiceInput,
)
from travelport.models.booking_end_port_type_service_output import (
    BookingEndPortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class BookingEndPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/SharedBookingService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/SharedBookingService"
    input = BookingEndPortTypeServiceInput
    output = BookingEndPortTypeServiceOutput
