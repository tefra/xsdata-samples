from __future__ import annotations

from travelport.models.upsell_admin_search_port_type_service_input import (
    UpsellAdminSearchPortTypeServiceInput,
)
from travelport.models.upsell_admin_search_port_type_service_output import (
    UpsellAdminSearchPortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class UpsellAdminSearchPortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/UpsellAdminSearchService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/UpsellAdminSearchService"
    input = UpsellAdminSearchPortTypeServiceInput
    output = UpsellAdminSearchPortTypeServiceOutput
