from __future__ import annotations

from dataclasses import dataclass

from .money_service_version_structure import MoneyServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class MoneyService(MoneyServiceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
