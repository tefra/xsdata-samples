from __future__ import annotations
from travelport.models.booking_air_pnr_element_port_type_service_input import BookingAirPnrElementPortTypeServiceInput
from travelport.models.booking_air_pnr_element_port_type_service_output import BookingAirPnrElementPortTypeServiceOutput

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class BookingAirPnrElementPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/SharedBookingService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/SharedBookingService"
    input = BookingAirPnrElementPortTypeServiceInput
    output = BookingAirPnrElementPortTypeServiceOutput
