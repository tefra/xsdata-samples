from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.seat_map_req import SeatMapReq
from travelport.models.session_context import SessionContext

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class SeatMapPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    header: SeatMapPortTypeServiceInput.Header = field(
        metadata={
            "name": "Header",
            "type": "Element",
        }
    )
    body: SeatMapPortTypeServiceInput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Header:
        session_context: SessionContext = field(
            metadata={
                "name": "SessionContext",
                "type": "Element",
                "namespace": "http://www.travelport.com/soa/common/security/SessionContext_v1",
            }
        )

    @dataclass(kw_only=True)
    class Body:
        seat_map_req: SeatMapReq = field(
            metadata={
                "name": "SeatMapReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v52_0",
            }
        )
