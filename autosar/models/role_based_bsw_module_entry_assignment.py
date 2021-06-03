from dataclasses import dataclass, field
from typing import Optional
from autosar.models.annotation import VariationPoint
from autosar.models.bsw_module_entry_subtypes_enum import BswModuleEntrySubtypesEnum
from autosar.models.identifier import Identifier
from autosar.models.ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class RoleBasedBswModuleEntryAssignment:
    """This class specifies an assignment of a role to a particular
    BswModuleEntry (usually a configurable callback).

    With this assignment, the role of the callback is mapped to a
    specific ServiceNeeds element, so that a tool is able to create
    appropriate configuration values for the module that implements the
    AUTOSAR Service.

    :ivar assigned_entry_ref: The assigned entry. It should be an
        implementedEntry or expectedEntry of the module or cluster that
        requires the ServiceNeeds.
    :ivar role: This is the role of the assigned BswModuleEntry in the
        given context. The attribute is required (for example) because
        different kind of callbacks may be associated with the same
        ServiceNeeds (e.g. end-notification vs. error-notification).
        The value shall be the role name of a configurable function call
        (usually a callback) as standardized in the Software
        Specification of the related AUTOSAR Service.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
    :ivar s: Checksum calculated by the user's tool environment for an
        ArObject. May be used in an own tool environment to determine if
        an ArObject has changed. The checksum has no semantic meaning
        for an AUTOSAR model and there is no requirement for AUTOSAR
        tools to manage the checksum.
    :ivar t: Timestamp calculated by the user's tool environment for an
        ArObject. May be used in an own tool environment to determine
        the last change of an ArObject. The timestamp has no semantic
        meaning for an AUTOSAR model and there is no requirement for
        AUTOSAR tools to manage the timestamp.
    """
    class Meta:
        name = "ROLE-BASED-BSW-MODULE-ENTRY-ASSIGNMENT"

    assigned_entry_ref: Optional["RoleBasedBswModuleEntryAssignment.AssignedEntryRef"] = field(
        default=None,
        metadata={
            "name": "ASSIGNED-ENTRY-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    role: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "ROLE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    variation_point: Optional[VariationPoint] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        }
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        }
    )

    @dataclass
    class AssignedEntryRef(Ref):
        dest: Optional[BswModuleEntrySubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
