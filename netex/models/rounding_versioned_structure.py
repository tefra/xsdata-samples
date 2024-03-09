from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from .entity_in_version_structure import DataManagedObjectStructure
from .multilingual_string import MultilingualString
from .rounding_method_enumeration import RoundingMethodEnumeration
from .rounding_steps_rel_structure import RoundingStepsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RoundingVersionedStructure(DataManagedObjectStructure):
    class Meta:
        name = "Rounding_VersionedStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    rounding_method: Optional[RoundingMethodEnumeration] = field(
        default=None,
        metadata={
            "name": "RoundingMethod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    rounding_modulus: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RoundingModulus",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    rounding_steps: Optional[RoundingStepsRelStructure] = field(
        default=None,
        metadata={
            "name": "roundingSteps",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
