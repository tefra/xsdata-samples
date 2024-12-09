from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.description import Description
from ipxact.models.display_name import DisplayName
from ipxact.models.drive_constraint import DriveConstraint
from ipxact.models.load_constraint import LoadConstraint
from ipxact.models.short_description import ShortDescription
from ipxact.models.timing_constraint import TimingConstraint
from ipxact.models.unsigned_int_expression import UnsignedIntExpression

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class ConstraintSet:
    """Defines constraints that apply to a component port.

    If multiple constraintSet elements are used, each must have a unique
    value for the constraintSetId attribute.

    :ivar name: Unique name
    :ivar display_name:
    :ivar short_description:
    :ivar description:
    :ivar vector: The optional element vector specify the bits of a
        vector for which the constraints apply. The vaules of left and
        right must be within the range of the port. If the vector is not
        specified then the constraints apply to all the bits of the
        port.
    :ivar drive_constraint:
    :ivar load_constraint:
    :ivar timing_constraint:
    :ivar constraint_set_id: Indicates a name for this set of
        constraints. Constraints are tied to a view using this name in
        the constraintSetRef element.
    :ivar id:
    """

    class Meta:
        name = "constraintSet"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    display_name: Optional[DisplayName] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
        },
    )
    short_description: Optional[ShortDescription] = field(
        default=None,
        metadata={
            "name": "shortDescription",
            "type": "Element",
        },
    )
    description: Optional[Description] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    vector: Optional["ConstraintSet.Vector"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    drive_constraint: Optional[DriveConstraint] = field(
        default=None,
        metadata={
            "name": "driveConstraint",
            "type": "Element",
        },
    )
    load_constraint: Optional[LoadConstraint] = field(
        default=None,
        metadata={
            "name": "loadConstraint",
            "type": "Element",
        },
    )
    timing_constraint: list[TimingConstraint] = field(
        default_factory=list,
        metadata={
            "name": "timingConstraint",
            "type": "Element",
        },
    )
    constraint_set_id: str = field(
        default="default",
        metadata={
            "name": "constraintSetId",
            "type": "Attribute",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )

    @dataclass
    class Vector:
        """
        :ivar left: The optional elements left and right can be used to
            select a bit-slice of a vector.
        :ivar right: The optional elements left and right can be used to
            select a bit-slice of a vector.
        """

        left: Optional[UnsignedIntExpression] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        right: Optional[UnsignedIntExpression] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
