from dataclasses import dataclass, field
from typing import Optional
from netex.models.check_constraint_version_structure import CheckConstraintVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CheckConstraint(CheckConstraintVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    responsibility_set_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "responsibilitySetRef",
            "type": "Attribute",
        }
    )
