from __future__ import annotations
from travelport.models.uimeta_data_retrieve_port_type_service_input import UimetaDataRetrievePortTypeServiceInput
from travelport.models.uimeta_data_retrieve_port_type_service_output import UimetaDataRetrievePortTypeServiceOutput

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class UimetaDataRetrievePortTypeService:
    style = "document"
    location = "http://localhost:9080/kestrel/UProfileSharedService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:9080/kestrel/UProfileSharedService"
    input = UimetaDataRetrievePortTypeServiceInput
    output = UimetaDataRetrievePortTypeServiceOutput
