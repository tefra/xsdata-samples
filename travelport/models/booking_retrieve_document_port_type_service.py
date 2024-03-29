from __future__ import annotations

from travelport.models.booking_retrieve_document_port_type_service_input import (
    BookingRetrieveDocumentPortTypeServiceInput,
)
from travelport.models.booking_retrieve_document_port_type_service_output import (
    BookingRetrieveDocumentPortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class BookingRetrieveDocumentPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/SharedBookingService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/SharedBookingService"
    input = BookingRetrieveDocumentPortTypeServiceInput
    output = BookingRetrieveDocumentPortTypeServiceOutput
