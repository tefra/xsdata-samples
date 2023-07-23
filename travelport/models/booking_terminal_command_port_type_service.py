from __future__ import annotations
from travelport.models.booking_terminal_command_port_type_service_input import BookingTerminalCommandPortTypeServiceInput
from travelport.models.booking_terminal_command_port_type_service_output import BookingTerminalCommandPortTypeServiceOutput

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class BookingTerminalCommandPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/SharedBookingService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/SharedBookingService"
    input = BookingTerminalCommandPortTypeServiceInput
    output = BookingTerminalCommandPortTypeServiceOutput
