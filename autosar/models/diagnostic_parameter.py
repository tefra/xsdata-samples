from dataclasses import dataclass, field
from typing import List, Optional
from .admin_data import VariationPoint
from .diagnostic_data_element import DiagnosticDataElement
from .diagnostic_parameter_support_info import DiagnosticParameterSupportInfo
from .positive_integer import PositiveInteger

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class DiagnosticParameter:
    """
    This meta-class represents the ability to describe information relevant for the
    execution of a specific diagnostic service, i.e. it can be taken to
    parameterize the service.

    :ivar bit_offset: This represents the bitOffset of the
        DiagnosticParameter
    :ivar data_elements: This represents the related dataElement of the
        DiagnosticParameter The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was 1.
    :ivar support_info: This attribute represents the ability to define
        which bit of the support info byte is representing this part of
        the PID.
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
        name = "DIAGNOSTIC-PARAMETER"

    bit_offset: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "BIT-OFFSET",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    data_elements: Optional["DiagnosticParameter.DataElements"] = field(
        default=None,
        metadata={
            "name": "DATA-ELEMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    support_info: Optional[DiagnosticParameterSupportInfo] = field(
        default=None,
        metadata={
            "name": "SUPPORT-INFO",
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
    class DataElements:
        diagnostic_data_element: List[DiagnosticDataElement] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-DATA-ELEMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
