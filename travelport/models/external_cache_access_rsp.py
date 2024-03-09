from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_rsp_3 import BaseRsp3

__NAMESPACE__ = "http://www.travelport.com/schema/system_v32_0"


@dataclass
class ExternalCacheAccessRsp(BaseRsp3):
    """
    The response to the CurrencyConversionReq.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/system_v32_0"

    cache_entry: list[ExternalCacheAccessRsp.CacheEntry] = field(
        default_factory=list,
        metadata={
            "name": "CacheEntry",
            "type": "Element",
            "max_occurs": 999,
        },
    )

    @dataclass
    class CacheEntry:
        """
        Parameters
        ----------
        value
        key
            Cache entry key
        """

        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        key: None | str = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            },
        )
