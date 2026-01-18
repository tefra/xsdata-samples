from __future__ import annotations

from dataclasses import dataclass

from .journey_accounting_version_structure import (
    JourneyAccountingVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyAccounting(JourneyAccountingVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
