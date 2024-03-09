from __future__ import annotations

from travelport.models.ack_schedule_change_service_port_type_service_input import (
    AckScheduleChangeServicePortTypeServiceInput,
)
from travelport.models.ack_schedule_change_service_port_type_service_output import (
    AckScheduleChangeServicePortTypeServiceOutput,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


class AckScheduleChangeServicePortTypeService:
    style = "document"
    location = "http://localhost:8080/kestrel/ScheduleChangeService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://localhost:8080/kestrel/ScheduleChangeService"
    input = AckScheduleChangeServicePortTypeServiceInput
    output = AckScheduleChangeServicePortTypeServiceOutput
