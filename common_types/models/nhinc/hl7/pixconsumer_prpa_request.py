from __future__ import annotations

from dataclasses import dataclass, field

from ...hl7_v3.ne2008.multi_cache.prpa_in201301_uv02 import PrpaIn201301Uv02
from ...hl7_v3.ne2008.multi_cache.prpa_in201302_uv02 import PrpaIn201302Uv02
from ..common.nhinc_common import (
    AssertionType,
    NhinTargetCommunitiesType,
)

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass(kw_only=True)
class PixconsumerPrpaIn201301UvrequestType:
    class Meta:
        name = "PIXConsumer_PRPA_IN201301UVRequestType"

    prpa_in201301_uv02: PrpaIn201301Uv02 = field(
        metadata={
            "name": "PRPA_IN201301UV02",
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
class PixconsumerPrpaIn201301UvsecuredRequestType:
    class Meta:
        name = "PIXConsumer_PRPA_IN201301UVSecuredRequestType"

    prpa_in201301_uv02: PrpaIn201301Uv02 = field(
        metadata={
            "name": "PRPA_IN201301UV02",
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
class PixconsumerPrpaIn201302UvrequestType:
    class Meta:
        name = "PIXConsumer_PRPA_IN201302UVRequestType"

    prpa_in201302_uv02: PrpaIn201302Uv02 = field(
        metadata={
            "name": "PRPA_IN201302UV02",
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
class PixconsumerPrpaIn201302UvsecuredRequestType:
    class Meta:
        name = "PIXConsumer_PRPA_IN201302UVSecuredRequestType"

    prpa_in201302_uv02: PrpaIn201302Uv02 = field(
        metadata={
            "name": "PRPA_IN201302UV02",
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
class PixconsumerPrpaIn201301Uvrequest(PixconsumerPrpaIn201301UvrequestType):
    class Meta:
        name = "PIXConsumer_PRPA_IN201301UVRequest"
        namespace = "urn:hl7-org:v3"


@dataclass(kw_only=True)
class PixconsumerPrpaIn201301UvsecuredRequest(
    PixconsumerPrpaIn201301UvsecuredRequestType
):
    class Meta:
        name = "PIXConsumer_PRPA_IN201301UVSecuredRequest"
        namespace = "urn:hl7-org:v3"


@dataclass(kw_only=True)
class PixconsumerPrpaIn201302Uvrequest(PixconsumerPrpaIn201302UvrequestType):
    class Meta:
        name = "PIXConsumer_PRPA_IN201302UVRequest"
        namespace = "urn:hl7-org:v3"


@dataclass(kw_only=True)
class PixconsumerPrpaIn201302UvsecuredRequest(
    PixconsumerPrpaIn201302UvsecuredRequestType
):
    class Meta:
        name = "PIXConsumer_PRPA_IN201302UVSecuredRequest"
        namespace = "urn:hl7-org:v3"
