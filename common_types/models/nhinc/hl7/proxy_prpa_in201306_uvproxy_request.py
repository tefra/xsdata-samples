from dataclasses import dataclass, field
from typing import Optional

from ...hl7_v3.ne2008.multi_cache.prpa_in201306_uv02 import PrpaIn201306Uv02
from ..common.nhinc_common import (
    AssertionType,
    NhinTargetSystemType,
)

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class ProxyPrpaIn201306UvproxyRequestType:
    class Meta:
        name = "Proxy_PRPA_IN201306UVProxyRequestType"

    prpa_in201306_uv02: Optional[PrpaIn201306Uv02] = field(
        default=None,
        metadata={
            "name": "PRPA_IN201306UV02",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    assertion: Optional[AssertionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    nhin_target_system: Optional[NhinTargetSystemType] = field(
        default=None,
        metadata={
            "name": "nhinTargetSystem",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )


@dataclass
class ProxyPrpaIn201306UvproxySecuredRequestType:
    class Meta:
        name = "Proxy_PRPA_IN201306UVProxySecuredRequestType"

    prpa_in201306_uv02: Optional[PrpaIn201306Uv02] = field(
        default=None,
        metadata={
            "name": "PRPA_IN201306UV02",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    nhin_target_system: Optional[NhinTargetSystemType] = field(
        default=None,
        metadata={
            "name": "nhinTargetSystem",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )


@dataclass
class ProxyPrpaIn201306UvproxyRequest(ProxyPrpaIn201306UvproxyRequestType):
    class Meta:
        name = "Proxy_PRPA_IN201306UVProxyRequest"
        namespace = "urn:hl7-org:v3"


@dataclass
class ProxyPrpaIn201306UvproxySecuredRequest(
    ProxyPrpaIn201306UvproxySecuredRequestType
):
    class Meta:
        name = "Proxy_PRPA_IN201306UVProxySecuredRequest"
        namespace = "urn:hl7-org:v3"
