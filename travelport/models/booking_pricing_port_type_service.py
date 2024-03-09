from __future__ import annotations

from travelport.models.booking_pricing_port_type_service_input import (
    BookingPricingPortTypeServiceInput,
)
from travelport.models.booking_pricing_port_type_service_output import (
    BookingPricingPortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class BookingPricingPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/SharedBookingService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/SharedBookingService"
    input = BookingPricingPortTypeServiceInput
    output = BookingPricingPortTypeServiceOutput
