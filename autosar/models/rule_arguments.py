from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.annotation import VariationPoint
from autosar.models.numerical_or_text import NumericalOrText
from autosar.models.numerical_value import NumericalValue
from autosar.models.numerical_value_variation_point import NumericalValueVariationPoint
from autosar.models.verbatim_string import VerbatimString

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class RuleArguments:
    """
    This represents the arguments for a rule-based value specification.

    :ivar v: This represents a numerical value for the
        RuleBasedValueSpecification.
    :ivar vf: This represents a numerical value for the
        RuleBasedValueSpecification which may subject to variability.
        The latest binding time of the VariationPoint shall be
        preCompileTime.
    :ivar vt: This represents a textual value for the
        RuleBasedValueSpecification.
    :ivar vtf: This aggregation represents the ability to provide a
        value that is either numerical or text which existence is
        subject to variability.  The upper multiplicity of this role has
        been increased to * due to resolving an atpVariation stereotype.
        The previous value was 1.
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
        name = "RULE-ARGUMENTS"

    v: List[NumericalValue] = field(
        default_factory=list,
        metadata={
            "name": "V",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    vf: List[NumericalValueVariationPoint] = field(
        default_factory=list,
        metadata={
            "name": "VF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    vt: List[VerbatimString] = field(
        default_factory=list,
        metadata={
            "name": "VT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    vtf: List[NumericalOrText] = field(
        default_factory=list,
        metadata={
            "name": "VTF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    variation_point: List[VariationPoint] = field(
        default_factory=list,
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
