from dataclasses import dataclass, field
from typing import Optional

from .admin_data import VariationPoint
from .ar_parameter_in_implementation_data_instance_ref import (
    ArParameterInImplementationDataInstanceRef,
)
from .ar_variable_in_implementation_data_instance_ref import (
    ArVariableInImplementationDataInstanceRef,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ImplementationDataTypeSubElementRef:
    """
    This meta-class represents the specialization of SubElementMapping with respect
    to ImplementationDataTypes.

    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
    :ivar implementation_data_type_element: This represents the
        referenced implementationDataTypeElement.
    :ivar parameter_implementation_data_type_element: This represents
        the referenced ImplementationDataTypeElement.
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
        name = "IMPLEMENTATION-DATA-TYPE-SUB-ELEMENT-REF"

    variation_point: Optional[VariationPoint] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    implementation_data_type_element: Optional[
        ArVariableInImplementationDataInstanceRef
    ] = field(
        default=None,
        metadata={
            "name": "IMPLEMENTATION-DATA-TYPE-ELEMENT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    parameter_implementation_data_type_element: Optional[
        ArParameterInImplementationDataInstanceRef
    ] = field(
        default=None,
        metadata={
            "name": "PARAMETER-IMPLEMENTATION-DATA-TYPE-ELEMENT",
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
