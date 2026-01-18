from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_exchange_bundle import AirExchangeBundle

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class AirExchangeBundleList:
    """
    The shared object list of AirsegmentData.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_exchange_bundle: list[AirExchangeBundle] = field(
        default_factory=list,
        metadata={
            "name": "AirExchangeBundle",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
