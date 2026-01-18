from __future__ import annotations

from dataclasses import dataclass, field

from .class_of_use_ref_structure import ClassOfUseRefStructure
from .exchangable_to_enumeration import ExchangableToEnumeration
from .fare_class_enumeration import FareClassEnumeration
from .reselling_version_structure import ResellingVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ExchangingVersionStructure(ResellingVersionStructure):
    class Meta:
        name = "Exchanging_VersionStructure"

    number_of_exchanges_allowed: int | None = field(
        default=None,
        metadata={
            "name": "NumberOfExchangesAllowed",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    to_fare_class: FareClassEnumeration | None = field(
        default=None,
        metadata={
            "name": "ToFareClass",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    to_class_of_use_ref: ClassOfUseRefStructure | None = field(
        default=None,
        metadata={
            "name": "ToClassOfUseRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    exchangable_to: ExchangableToEnumeration | None = field(
        default=None,
        metadata={
            "name": "ExchangableTo",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
