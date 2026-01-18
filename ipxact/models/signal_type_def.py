from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.signal_type_def_signal_type import SignalTypeDefSignalType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class SignalTypeDef:
    """
    Definition of a single signal type defintion that can relate to
    multiple views.

    :ivar signal_type: defines the signal type for the port. Continuous-
        conservative is a signal which is continuous in time and
        quantity, where the quantity represents voltage and current to
        capture the conservative behavior of an electrical network (i.
        e. Kirchhoff’s Laws apply), and which has no direction.
        Continuous-non-conservative is a directed signal which is
        continuous in time and quantity, where the quantity represents
        either a voltage or a current (often called signal flow). In
        this case it only captures the non-conservative behavior of a
        set of interconnected components. Discrete is a directed sampled
        signal which is time-discrete and value-continuous (the value
        may also be quantified), where the value represents either a
        voltage or a current (other representations are possible also).
        It captures the non-conservative behavior of a set of
        interconnected components. Digital is a time-discrete and value-
        discrete signal. The interpretation of the signal values is
        described by the wireTypeDefs.
    :ivar view_ref: A reference to a view in the file for which this
        type applies.
    :ivar id:
    """

    class Meta:
        name = "signalTypeDef"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    signal_type: SignalTypeDefSignalType | None = field(
        default=None,
        metadata={
            "name": "signalType",
            "type": "Element",
            "required": True,
        },
    )
    view_ref: list[SignalTypeDef.ViewRef] = field(
        default_factory=list,
        metadata={
            "name": "viewRef",
            "type": "Element",
        },
    )
    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )

    @dataclass
    class ViewRef:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        id: str | None = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.w3.org/XML/1998/namespace",
            },
        )
