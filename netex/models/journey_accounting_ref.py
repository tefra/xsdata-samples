from dataclasses import dataclass

from .journey_accounting_ref_structure import JourneyAccountingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyAccountingRef(JourneyAccountingRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
