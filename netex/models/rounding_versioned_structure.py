from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from .entity_in_version_structure import DataManagedObjectStructure
from .multilingual_string import MultilingualString
from .rounding_method_enumeration import RoundingMethodEnumeration
from .rounding_steps_rel_structure import RoundingStepsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RoundingVersionedStructure(DataManagedObjectStructure):
    class Meta:
        name = "Rounding_VersionedStructure"

    name: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    rounding_method: None | RoundingMethodEnumeration = field(
        default=None,
        metadata={
            "name": "RoundingMethod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    rounding_modulus: None | Decimal = field(
        default=None,
        metadata={
            "name": "RoundingModulus",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    rounding_steps: None | RoundingStepsRelStructure = field(
        default=None,
        metadata={
            "name": "roundingSteps",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
