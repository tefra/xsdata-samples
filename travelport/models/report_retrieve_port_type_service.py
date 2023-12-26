from __future__ import annotations
from travelport.models.report_retrieve_port_type_service_input import (
    ReportRetrievePortTypeServiceInput,
)
from travelport.models.report_retrieve_port_type_service_output import (
    ReportRetrievePortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class ReportRetrievePortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/UtilService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/UtilService"
    input = ReportRetrievePortTypeServiceInput
    output = ReportRetrievePortTypeServiceOutput
