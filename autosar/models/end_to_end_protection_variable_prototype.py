from dataclasses import dataclass, field
from typing import List, Optional
from .annotation import VariationPoint
from .identifier import Identifier
from .variable_data_prototype_in_system_instance_ref import (
    VariableDataPrototypeInSystemInstanceRef,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class EndToEndProtectionVariablePrototype:
    """It is possible to protect the data exchanged between software components.

    For this purpose, for each communication to be protected,  the user defines a separate EndToEndProtection (specifying a set of protection settings) and refers to a variableDataPrototype in the role of sender and to one or many variableDataPrototypes in the role of receiver. For details, see EndToEnd Library.
    Caveat: The E2E wrapper approach involves technologies that are not subjected to the AUTOSAR standard and is superseded by the superior E2E transformer approach (which is fully standardized by AUTOSAR). Hence, new projects (without legacy constraints due to carry-over parts) shall use the fully standardized E2E transformer approach.

    :ivar receiver_irefs: This represents the receiver. Note that 1:n
        communication is supported for this use case.
    :ivar sender_iref: This represents the sender. Can be optional if an
        ecu extract is provided and the sender is part of the extract.
    :ivar short_label: This serves as part of the split key in case of
        more than one EndToEndProtectionVariablePrototype is aggregated
        in the bound model.
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
        name = "END-TO-END-PROTECTION-VARIABLE-PROTOTYPE"

    receiver_irefs: Optional[
        "EndToEndProtectionVariablePrototype.ReceiverIrefs"
    ] = field(
        default=None,
        metadata={
            "name": "RECEIVER-IREFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sender_iref: Optional[VariableDataPrototypeInSystemInstanceRef] = field(
        default=None,
        metadata={
            "name": "SENDER-IREF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    short_label: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-LABEL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: Optional[VariationPoint] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )

    @dataclass
    class ReceiverIrefs:
        receiver_iref: List[VariableDataPrototypeInSystemInstanceRef] = field(
            default_factory=list,
            metadata={
                "name": "RECEIVER-IREF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
