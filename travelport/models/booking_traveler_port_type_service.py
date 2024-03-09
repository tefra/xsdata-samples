from __future__ import annotations

from travelport.models.booking_traveler_port_type_service_input import (
    BookingTravelerPortTypeServiceInput,
)
from travelport.models.booking_traveler_port_type_service_output import (
    BookingTravelerPortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class BookingTravelerPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/SharedBookingService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/SharedBookingService"
    input = BookingTravelerPortTypeServiceInput
    output = BookingTravelerPortTypeServiceOutput
