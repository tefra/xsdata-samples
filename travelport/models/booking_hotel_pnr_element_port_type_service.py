from __future__ import annotations
from travelport.models.booking_hotel_pnr_element_port_type_service_input import (
    BookingHotelPnrElementPortTypeServiceInput,
)
from travelport.models.booking_hotel_pnr_element_port_type_service_output import (
    BookingHotelPnrElementPortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class BookingHotelPnrElementPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/SharedBookingService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/SharedBookingService"
    input = BookingHotelPnrElementPortTypeServiceInput
    output = BookingHotelPnrElementPortTypeServiceOutput
