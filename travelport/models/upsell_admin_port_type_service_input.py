from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.upsell_admin_req import UpsellAdminReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class UpsellAdminPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | UpsellAdminPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        upsell_admin_req: None | UpsellAdminReq = field(
            default=None,
            metadata={
                "name": "UpsellAdminReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/util_v52_0",
            },
        )
