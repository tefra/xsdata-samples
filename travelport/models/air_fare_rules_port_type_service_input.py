from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_fare_rules_req import AirFareRulesReq
from travelport.models.session_context import SessionContext

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class AirFareRulesPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    header: None | AirFareRulesPortTypeServiceInput.Header = field(
        default=None,
        metadata={
            "name": "Header",
            "type": "Element",
        },
    )
    body: None | AirFareRulesPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Header:
        session_context: None | SessionContext = field(
            default=None,
            metadata={
                "name": "SessionContext",
                "type": "Element",
                "namespace": "http://www.travelport.com/soa/common/security/SessionContext_v1",
            },
        )

    @dataclass
    class Body:
        air_fare_rules_req: None | AirFareRulesReq = field(
            default=None,
            metadata={
                "name": "AirFareRulesReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v52_0",
            },
        )
