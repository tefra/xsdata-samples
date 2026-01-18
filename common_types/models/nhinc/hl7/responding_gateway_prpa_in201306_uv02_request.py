from __future__ import annotations

from dataclasses import dataclass, field

from ...hl7_v3.ne2008.multi_cache.prpa_in201306_uv02 import PrpaIn201306Uv02
from ..common.nhinc_common import (
    AssertionType,
    NhinTargetCommunitiesType,
)

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass(kw_only=True)
class RespondingGatewayPrpaIn201306Uv02RequestType:
    class Meta:
        name = "RespondingGateway_PRPA_IN201306UV02RequestType"

    prpa_in201306_uv02: PrpaIn201306Uv02 = field(
        metadata={
            "name": "PRPA_IN201306UV02",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    assertion: AssertionType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    nhin_target_communities: None | NhinTargetCommunitiesType = field(
        default=None,
        metadata={
            "name": "NhinTargetCommunities",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )


@dataclass(kw_only=True)
class RespondingGatewayPrpaIn201306Uv02SecuredRequestType:
    class Meta:
        name = "RespondingGateway_PRPA_IN201306UV02SecuredRequestType"

    prpa_in201306_uv02: PrpaIn201306Uv02 = field(
        metadata={
            "name": "PRPA_IN201306UV02",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    nhin_target_communities: None | NhinTargetCommunitiesType = field(
        default=None,
        metadata={
            "name": "NhinTargetCommunities",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )


@dataclass(kw_only=True)
class RespondingGatewayPrpaIn201306Uv02Request(
    RespondingGatewayPrpaIn201306Uv02RequestType
):
    class Meta:
        name = "RespondingGateway_PRPA_IN201306UV02Request"
        namespace = "urn:hl7-org:v3"


@dataclass(kw_only=True)
class RespondingGatewayPrpaIn201306Uv02SecuredRequest(
    RespondingGatewayPrpaIn201306Uv02SecuredRequestType
):
    class Meta:
        name = "RespondingGateway_PRPA_IN201306UV02SecuredRequest"
        namespace = "urn:hl7-org:v3"
