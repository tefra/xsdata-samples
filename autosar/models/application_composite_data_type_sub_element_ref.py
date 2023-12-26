from dataclasses import dataclass, field
from typing import Optional
from .annotation import VariationPoint
from .application_composite_element_in_port_interface_instance_ref import (
    ApplicationCompositeElementInPortInterfaceInstanceRef,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ApplicationCompositeDataTypeSubElementRef:
    """
    This meta-class represents the specialization of SubElementMapping with respect
    to ApplicationCompositeDataTypes.

    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
    :ivar application_composite_element_iref: This represents the
        referenced ApplicationCompositeDataPrototype.
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
        name = "APPLICATION-COMPOSITE-DATA-TYPE-SUB-ELEMENT-REF"

    variation_point: Optional[VariationPoint] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    application_composite_element_iref: Optional[
        ApplicationCompositeElementInPortInterfaceInstanceRef
    ] = field(
        default=None,
        metadata={
            "name": "APPLICATION-COMPOSITE-ELEMENT-IREF",
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
