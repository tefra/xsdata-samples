from __future__ import annotations
from travelport.models.booking_seat_assignment_port_type_service_input import (
    BookingSeatAssignmentPortTypeServiceInput,
)
from travelport.models.booking_seat_assignment_port_type_service_output import (
    BookingSeatAssignmentPortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class BookingSeatAssignmentPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/SharedBookingService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/SharedBookingService"
    input = BookingSeatAssignmentPortTypeServiceInput
    output = BookingSeatAssignmentPortTypeServiceOutput
