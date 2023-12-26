from dataclasses import dataclass, field
from typing import Optional
from .identifier import Identifier
from .limit import Limit
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .scale_constr_validity_enum_simple import ScaleConstrValidityEnumSimple

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ScaleConstr:
    """
    This meta-class represents the ability to specify constraints as a list of
    intervals (called scales).

    :ivar short_label: This element specifies a short name for the
        scaleConstr. This can for example be used to create more
        specific messages of a constraint checker. The constraints
        cannot be associated in the meta-model, therefore shortLabel is
        somehow a substitute for shortName.
    :ivar desc: &lt;desc&gt; represents a general but brief description
        of the object in question.
    :ivar lower_limit: This specifies the lower limit of the scale.
    :ivar upper_limit: This specifies the upper limit of a the scale.
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
    :ivar validity: Specifies if the values defined by the scales are
        considered to be valid. If the attribute is missing then the
        default value is "VALID".
    """

    class Meta:
        name = "SCALE-CONSTR"

    short_label: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-LABEL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    desc: Optional[MultiLanguageOverviewParagraph] = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    lower_limit: Optional[Limit] = field(
        default=None,
        metadata={
            "name": "LOWER-LIMIT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    upper_limit: Optional[Limit] = field(
        default=None,
        metadata={
            "name": "UPPER-LIMIT",
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
    validity: Optional[ScaleConstrValidityEnumSimple] = field(
        default=None,
        metadata={
            "name": "VALIDITY",
            "type": "Attribute",
        },
    )
