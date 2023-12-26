from __future__ import annotations
from travelport.models.booking_display_port_type_service_input import (
    BookingDisplayPortTypeServiceInput,
)
from travelport.models.booking_display_port_type_service_output import (
    BookingDisplayPortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class BookingDisplayPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/SharedBookingService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/SharedBookingService"
    input = BookingDisplayPortTypeServiceInput
    output = BookingDisplayPortTypeServiceOutput
