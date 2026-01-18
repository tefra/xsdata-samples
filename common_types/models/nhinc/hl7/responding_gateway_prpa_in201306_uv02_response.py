from dataclasses import dataclass, field
from typing import Optional

from ...hl7_v3.ne2008.multi_cache.prpa_in201306_uv02 import PrpaIn201306Uv02
from ..common.nhinc_common import NhinTargetCommunityType

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class CommunityPrpaIn201306Uv02ResponseType:
    class Meta:
        name = "Community_PRPA_IN201306UV02ResponseType"

    prpa_in201306_uv02: PrpaIn201306Uv02 | None = field(
        default=None,
        metadata={
            "name": "PRPA_IN201306UV02",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    nhin_target_community: NhinTargetCommunityType | None = field(
        default=None,
        metadata={
            "name": "nhinTargetCommunity",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )


@dataclass
class RespondingGatewayPrpaIn201306Uv02ResponseType:
    class Meta:
        name = "RespondingGateway_PRPA_IN201306UV02ResponseType"

    community_response: list[CommunityPrpaIn201306Uv02ResponseType] = field(
        default_factory=list,
        metadata={
            "name": "communityResponse",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        },
    )


@dataclass
class RespondingGatewayPrpaIn201306Uv02Response(
    RespondingGatewayPrpaIn201306Uv02ResponseType
):
    class Meta:
        name = "RespondingGateway_PRPA_IN201306UV02Response"
        namespace = "urn:hl7-org:v3"
