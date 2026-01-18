from __future__ import annotations

from dataclasses import dataclass, field

from sabre.models.exchange_source_type import ExchangeSourceType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class ExchangePostype:
    class Meta:
        name = "ExchangePOSType"

    source: ExchangeSourceType = field(
        metadata={
            "name": "Source",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )
