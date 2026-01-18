from __future__ import annotations

from dataclasses import dataclass

from .group_of_tariff_zones_ref_structure import GroupOfTariffZonesRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupOfTariffZonesRef(GroupOfTariffZonesRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
