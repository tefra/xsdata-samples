from __future__ import annotations

from travelport.models.booking_hotel_segment_port_type_service_input import (
    BookingHotelSegmentPortTypeServiceInput,
)
from travelport.models.booking_hotel_segment_port_type_service_output import (
    BookingHotelSegmentPortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class BookingHotelSegmentPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/SharedBookingService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/SharedBookingService"
    input = BookingHotelSegmentPortTypeServiceInput
    output = BookingHotelSegmentPortTypeServiceOutput
