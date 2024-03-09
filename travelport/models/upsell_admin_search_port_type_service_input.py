from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.upsell_search_req import UpsellSearchReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class UpsellAdminSearchPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | UpsellAdminSearchPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        upsell_search_req: None | UpsellSearchReq = field(
            default=None,
            metadata={
                "name": "UpsellSearchReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/util_v52_0",
            },
        )
