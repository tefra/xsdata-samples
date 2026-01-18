from __future__ import annotations

from dataclasses import dataclass, field

from ...hl7_v3.ne2008.multi_cache.prpa_in201305_uv02 import PrpaIn201305Uv02
from ...hl7_v3.ne2008.multi_cache.prpa_in201306_uv02 import PrpaIn201306Uv02
from ..common.nhinc_common import (
    AssertionType,
    NhinTargetCommunitiesType,
)

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class AsyncAdapterPatientDiscoveryErrorRequestType:
    prpa_in201305_uv02: None | PrpaIn201305Uv02 = field(
        default=None,
        metadata={
            "name": "PRPA_IN201305UV02",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    prpa_in201306_uv02: None | PrpaIn201306Uv02 = field(
        default=None,
        metadata={
            "name": "PRPA_IN201306UV02",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    assertion: None | AssertionType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    nhin_target_communities: None | NhinTargetCommunitiesType = field(
        default=None,
        metadata={
            "name": "NhinTargetCommunities",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    error_msg: None | str = field(
        default=None,
        metadata={
            "name": "errorMsg",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )


@dataclass
class AsyncAdapterPatientDiscoveryErrorSecuredRequestType:
    prpa_in201305_uv02: None | PrpaIn201305Uv02 = field(
        default=None,
        metadata={
            "name": "PRPA_IN201305UV02",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    prpa_in201306_uv02: None | PrpaIn201306Uv02 = field(
        default=None,
        metadata={
            "name": "PRPA_IN201306UV02",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    nhin_target_communities: None | NhinTargetCommunitiesType = field(
        default=None,
        metadata={
            "name": "NhinTargetCommunities",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    error_msg: None | str = field(
        default=None,
        metadata={
            "name": "errorMsg",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )


@dataclass
class AsyncAdapterPatientDiscoveryErrorRequest(
    AsyncAdapterPatientDiscoveryErrorRequestType
):
    class Meta:
        namespace = "urn:hl7-org:v3"


@dataclass
class AsyncAdapterPatientDiscoveryErrorSecuredRequest(
    AsyncAdapterPatientDiscoveryErrorSecuredRequestType
):
    class Meta:
        namespace = "urn:hl7-org:v3"
