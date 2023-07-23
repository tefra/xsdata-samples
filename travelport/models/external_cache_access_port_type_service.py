from __future__ import annotations
from travelport.models.external_cache_access_port_type_service_input import ExternalCacheAccessPortTypeServiceInput
from travelport.models.external_cache_access_port_type_service_output import ExternalCacheAccessPortTypeServiceOutput

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class ExternalCacheAccessPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/ExternalCacheAccessService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/ExternalCacheAccessService"
    input = ExternalCacheAccessPortTypeServiceInput
    output = ExternalCacheAccessPortTypeServiceOutput
