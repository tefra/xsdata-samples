from dataclasses import dataclass, field
from typing import List, Optional
from .diagnostic_common_props_conditional import DiagnosticCommonPropsConditional

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class DiagnosticCommonProps:
    """
    This meta-class aggregates a number of common properties that are shared
    among a diagnostic extract.

    :ivar diagnostic_common_props_variants: This element was
        generated/modified due to an atpVariation stereotype.
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
        name = "DIAGNOSTIC-COMMON-PROPS"

    diagnostic_common_props_variants: Optional["DiagnosticCommonProps.DiagnosticCommonPropsVariants"] = field(
        default=None,
        metadata={
            "name": "DIAGNOSTIC-COMMON-PROPS-VARIANTS",
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
    class DiagnosticCommonPropsVariants:
        diagnostic_common_props_conditional: List[DiagnosticCommonPropsConditional] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-COMMON-PROPS-CONDITIONAL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
