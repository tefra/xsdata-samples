from dataclasses import dataclass, field

from .admin_data import VariationPoint
from .c_identifier import CIdentifier
from .compu_const import CompuConst
from .compu_rational_coeffs import CompuRationalCoeffs
from .identifier import Identifier
from .limit import Limit
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .positive_integer import PositiveInteger

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class CompuScale:
    """
    This meta-class represents the ability to specify one segment of a
    segmented computation method.

    :ivar short_label: This element specifies a short name for the
        particular scale. The name can for example be used to derive a
        programming language identifier.
    :ivar symbol: The symbol, if provided, is used by code generators to
        get a C identifier for the CompuScale. The name will be used as
        is for the code generation, therefore it needs to be unique
        within the generation context.
    :ivar desc: &lt;desc&gt; represents a general but brief description
        of the object in question.
    :ivar mask: In difference to all the other computational methods
        every COMPU-SCALE will be applied including the bit MASK.
        Therefore it is allowed for this type of COMPU-METHOD, that
        COMPU-SCALES overlap. To calculate the string reverse to a
        value, the string has to be split and the according value for
        each substring has to be summed up. The sum is finally
        transmitted. The processing has to be done in order of the
        COMPU-SCALE elements.
    :ivar lower_limit: This specifies the lower limit of the scale.
    :ivar upper_limit: This specifies the upper limit of a of the scale.
    :ivar compu_inverse_value: This is the inverse value of the
        constraint. This supports the case that the scale is not
        reversible per se.
    :ivar compu_const: This represents the fact that the scale is a
        constant. The use case is mainly a non interpolated scale. It is
        a simplification of the fact that a constant scale can also be
        expressed as rational function of order 0.
    :ivar compu_rational_coeffs: This specifies the coefficients of the
        rational formula.
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
        name = "COMPU-SCALE"

    short_label: Identifier | None = field(
        default=None,
        metadata={
            "name": "SHORT-LABEL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    symbol: CIdentifier | None = field(
        default=None,
        metadata={
            "name": "SYMBOL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    desc: MultiLanguageOverviewParagraph | None = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    mask: PositiveInteger | None = field(
        default=None,
        metadata={
            "name": "MASK",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    lower_limit: Limit | None = field(
        default=None,
        metadata={
            "name": "LOWER-LIMIT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    upper_limit: Limit | None = field(
        default=None,
        metadata={
            "name": "UPPER-LIMIT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    compu_inverse_value: CompuConst | None = field(
        default=None,
        metadata={
            "name": "COMPU-INVERSE-VALUE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    compu_const: CompuConst | None = field(
        default=None,
        metadata={
            "name": "COMPU-CONST",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    compu_rational_coeffs: CompuRationalCoeffs | None = field(
        default=None,
        metadata={
            "name": "COMPU-RATIONAL-COEFFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: VariationPoint | None = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: str | None = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: str | None = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )
