from __future__ import annotations

from dataclasses import dataclass, field

from ...hl7_v3.ne2008.multi_cache.prpa_in201305_uv02 import PrpaIn201305Uv02
from ..common.nhinc_common import (
    AssertionType,
    NhinTargetSystemType,
)

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass(kw_only=True)
class ProxyPrpaIn201305UvproxyRequestType:
    class Meta:
        name = "Proxy_PRPA_IN201305UVProxyRequestType"

    prpa_in201305_uv02: PrpaIn201305Uv02 = field(
        metadata={
            "name": "PRPA_IN201305UV02",
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
    nhin_target_system: NhinTargetSystemType = field(
        metadata={
            "name": "nhinTargetSystem",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ProxyPrpaIn201305UvproxySecuredRequestType:
    class Meta:
        name = "Proxy_PRPA_IN201305UVProxySecuredRequestType"

    prpa_in201305_uv02: PrpaIn201305Uv02 = field(
        metadata={
            "name": "PRPA_IN201305UV02",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    nhin_target_system: NhinTargetSystemType = field(
        metadata={
            "name": "nhinTargetSystem",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ProxyPrpaIn201305UvproxyRequest(ProxyPrpaIn201305UvproxyRequestType):
    class Meta:
        name = "Proxy_PRPA_IN201305UVProxyRequest"
        namespace = "urn:hl7-org:v3"


@dataclass(kw_only=True)
class ProxyPrpaIn201305UvproxySecuredRequest(
    ProxyPrpaIn201305UvproxySecuredRequestType
):
    class Meta:
        name = "Proxy_PRPA_IN201305UVProxySecuredRequest"
        namespace = "urn:hl7-org:v3"
