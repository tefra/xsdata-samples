from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.abstraction_def_port_constraints_type import (
    AbstractionDefPortConstraintsType,
)
from ipxact.models.direction import Direction
from ipxact.models.presence import Presence
from ipxact.models.qualifier_type import QualifierType
from ipxact.models.requires_driver import RequiresDriver
from ipxact.models.unsigned_bit_vector_expression import (
    UnsignedBitVectorExpression,
)
from ipxact.models.unsigned_positive_int_expression import (
    UnsignedPositiveIntExpression,
)

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class Wire:
    """
    A port that carries logic or an array of logic values.

    :ivar qualifier: The type of information this port carries A wire
        port can carry both address and data, but may not mix this with
        a clock or reset
    :ivar on_system: Defines constraints for this port when present in a
        system bus interface with a matching group name.
    :ivar on_initiator: Defines constraints for this port when present
        in a initiator bus interface.
    :ivar on_target: Defines constraints for this port when present in a
        target bus interface.
    :ivar default_value: Indicates the default value for this wire port.
    :ivar requires_driver:
    """

    class Meta:
        name = "wire"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    qualifier: Optional[QualifierType] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    on_system: list["Wire.OnSystem"] = field(
        default_factory=list,
        metadata={
            "name": "onSystem",
            "type": "Element",
        },
    )
    on_initiator: Optional["Wire.OnInitiator"] = field(
        default=None,
        metadata={
            "name": "onInitiator",
            "type": "Element",
        },
    )
    on_target: Optional["Wire.OnTarget"] = field(
        default=None,
        metadata={
            "name": "onTarget",
            "type": "Element",
        },
    )
    default_value: Optional[UnsignedBitVectorExpression] = field(
        default=None,
        metadata={
            "name": "defaultValue",
            "type": "Element",
        },
    )
    requires_driver: Optional[RequiresDriver] = field(
        default=None,
        metadata={
            "name": "requiresDriver",
            "type": "Element",
        },
    )

    @dataclass
    class OnSystem:
        """
        :ivar group: Used to group system ports into different groups
            within a common bus.
        :ivar presence:
        :ivar width: Number of bits required to represent this port.
            Absence of this element indicates unconstrained number of
            bits, i.e. the component will define the number of bits in
            this port. The logical numbering of the port starts at 0 to
            width-1.
        :ivar direction: If this element is present, the direction of
            this port is restricted to the specified value. The
            direction is relative to the non-mirrored interface.
        :ivar mode_constraints: Specifies default constraints for the
            enclosing wire type port. If the mirroredModeConstraints
            element is not defined, then these constraints applied to
            this port when it appears in a 'mode' bus interface or a
            mirrored-'mode' bus interface. Otherwise they only apply
            when the port appears in a 'mode' bus interface.
        :ivar mirrored_mode_constraints: Specifies default constraints
            for the enclosing wire type port when it appears in a
            mirrored-'mode' bus interface.
        :ivar id:
        """

        group: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        presence: Optional[Presence] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        width: Optional["Wire.OnSystem.Width"] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        direction: Optional[Direction] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        mode_constraints: Optional[AbstractionDefPortConstraintsType] = field(
            default=None,
            metadata={
                "name": "modeConstraints",
                "type": "Element",
            },
        )
        mirrored_mode_constraints: Optional[
            AbstractionDefPortConstraintsType
        ] = field(
            default=None,
            metadata={
                "name": "mirroredModeConstraints",
                "type": "Element",
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
        class Width(UnsignedPositiveIntExpression):
            """
            :ivar all_bits: false: mapping is optional, any number of
                bits can be mapped. true: mapping is required  the full
                width is supposed to be mapped.
            """

            all_bits: bool = field(
                default=False,
                metadata={
                    "name": "allBits",
                    "type": "Attribute",
                },
            )

    @dataclass
    class OnInitiator:
        """
        :ivar presence:
        :ivar width: Number of bits required to represent this port.
            Absence of this element indicates unconstrained number of
            bits, i.e. the component will define the number of bits in
            this port. The logical numbering of the port starts at 0 to
            width-1.
        :ivar direction: If this element is present, the direction of
            this port is restricted to the specified value. The
            direction is relative to the non-mirrored interface.
        :ivar mode_constraints: Specifies default constraints for the
            enclosing wire type port. If the mirroredModeConstraints
            element is not defined, then these constraints applied to
            this port when it appears in a 'mode' bus interface or a
            mirrored-'mode' bus interface. Otherwise they only apply
            when the port appears in a 'mode' bus interface.
        :ivar mirrored_mode_constraints: Specifies default constraints
            for the enclosing wire type port when it appears in a
            mirrored-'mode' bus interface.
        """

        presence: Optional[Presence] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        width: Optional["Wire.OnInitiator.Width"] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        direction: Optional[Direction] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        mode_constraints: Optional[AbstractionDefPortConstraintsType] = field(
            default=None,
            metadata={
                "name": "modeConstraints",
                "type": "Element",
            },
        )
        mirrored_mode_constraints: Optional[
            AbstractionDefPortConstraintsType
        ] = field(
            default=None,
            metadata={
                "name": "mirroredModeConstraints",
                "type": "Element",
            },
        )

        @dataclass
        class Width(UnsignedPositiveIntExpression):
            """
            :ivar all_bits: false: mapping is optional, any number of
                bits can be mapped. true: mapping is required  the full
                width is supposed to be mapped.
            """

            all_bits: bool = field(
                default=False,
                metadata={
                    "name": "allBits",
                    "type": "Attribute",
                },
            )

    @dataclass
    class OnTarget:
        """
        :ivar presence:
        :ivar width: Number of bits required to represent this port.
            Absence of this element indicates unconstrained number of
            bits, i.e. the component will define the number of bits in
            this port. The logical numbering of the port starts at 0 to
            width-1.
        :ivar direction: If this element is present, the direction of
            this port is restricted to the specified value. The
            direction is relative to the non-mirrored interface.
        :ivar mode_constraints: Specifies default constraints for the
            enclosing wire type port. If the mirroredModeConstraints
            element is not defined, then these constraints applied to
            this port when it appears in a 'mode' bus interface or a
            mirrored-'mode' bus interface. Otherwise they only apply
            when the port appears in a 'mode' bus interface.
        :ivar mirrored_mode_constraints: Specifies default constraints
            for the enclosing wire type port when it appears in a
            mirrored-'mode' bus interface.
        """

        presence: Optional[Presence] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        width: Optional["Wire.OnTarget.Width"] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        direction: Optional[Direction] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        mode_constraints: Optional[AbstractionDefPortConstraintsType] = field(
            default=None,
            metadata={
                "name": "modeConstraints",
                "type": "Element",
            },
        )
        mirrored_mode_constraints: Optional[
            AbstractionDefPortConstraintsType
        ] = field(
            default=None,
            metadata={
                "name": "mirroredModeConstraints",
                "type": "Element",
            },
        )

        @dataclass
        class Width(UnsignedPositiveIntExpression):
            """
            :ivar all_bits: false: mapping is optional, any number of
                bits can be mapped. true: mapping is required  the full
                width is supposed to be mapped.
            """

            all_bits: bool = field(
                default=False,
                metadata={
                    "name": "allBits",
                    "type": "Attribute",
                },
            )
