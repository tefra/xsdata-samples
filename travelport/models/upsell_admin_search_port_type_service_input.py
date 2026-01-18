from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.upsell_search_req import UpsellSearchReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class UpsellAdminSearchPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: UpsellAdminSearchPortTypeServiceInput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        upsell_search_req: UpsellSearchReq = field(
            metadata={
                "name": "UpsellSearchReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/util_v52_0",
            }
        )
