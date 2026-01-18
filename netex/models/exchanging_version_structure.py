from __future__ import annotations

from dataclasses import dataclass, field

from .class_of_use_ref_structure import ClassOfUseRefStructure
from .exchangable_to_enumeration import ExchangableToEnumeration
from .fare_class_enumeration import FareClassEnumeration
from .reselling_version_structure import ResellingVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ExchangingVersionStructure(ResellingVersionStructure):
    class Meta:
        name = "Exchanging_VersionStructure"

    number_of_exchanges_allowed: None | int = field(
        default=None,
        metadata={
            "name": "NumberOfExchangesAllowed",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    to_fare_class: None | FareClassEnumeration = field(
        default=None,
        metadata={
            "name": "ToFareClass",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    to_class_of_use_ref: None | ClassOfUseRefStructure = field(
        default=None,
        metadata={
            "name": "ToClassOfUseRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    exchangable_to: None | ExchangableToEnumeration = field(
        default=None,
        metadata={
            "name": "ExchangableTo",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
