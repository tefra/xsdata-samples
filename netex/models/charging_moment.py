from __future__ import annotations

from dataclasses import dataclass

from .charging_moment_value_structure import ChargingMomentValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ChargingMoment(ChargingMomentValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
