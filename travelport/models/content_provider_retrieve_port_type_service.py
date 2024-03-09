from __future__ import annotations

from travelport.models.content_provider_retrieve_port_type_service_input import (
    ContentProviderRetrievePortTypeServiceInput,
)
from travelport.models.content_provider_retrieve_port_type_service_output import (
    ContentProviderRetrievePortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class ContentProviderRetrievePortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/UtilService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/UtilService"
    input = ContentProviderRetrievePortTypeServiceInput
    output = ContentProviderRetrievePortTypeServiceOutput
