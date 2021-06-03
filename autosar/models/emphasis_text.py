from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.e_enum_font_simple import EEnumFontSimple
from autosar.models.e_enum_simple import EEnumSimple
from autosar.models.supscript import Supscript
from autosar.models.tt import Tt

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class EmphasisText:
    """This is an emphasized text.

    As a compromise it contains some rendering oriented attributes such
    as color and font.

    :ivar content:
    :ivar sub: this is subscript text
    :ivar sup: This is superscript text
    :ivar tt: This is a technical term.
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
    :ivar color: This allows to recommend a color of the emphasis. It is
        specified bases on 6 digits RGB hex-code.
    :ivar font: This specifies the font style in which the emphasized
        text shall be rendered.
    :ivar type: Indicates how the text may be emphasized. Note that this
        is only a proposal which can be overridden or ignored by
        particular formatting engines. Default is BOLD.
    """
    class Meta:
        name = "EMPHASIS-TEXT"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    sub: List[Supscript] = field(
        default_factory=list,
        metadata={
            "name": "SUB",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    sup: List[Supscript] = field(
        default_factory=list,
        metadata={
            "name": "SUP",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    tt: List[Tt] = field(
        default_factory=list,
        metadata={
            "name": "TT",
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
    color: Optional[str] = field(
        default=None,
        metadata={
            "name": "COLOR",
            "type": "Attribute",
        }
    )
    font: Optional[EEnumFontSimple] = field(
        default=None,
        metadata={
            "name": "FONT",
            "type": "Attribute",
        }
    )
    type: Optional[EEnumSimple] = field(
        default=None,
        metadata={
            "name": "TYPE",
            "type": "Attribute",
        }
    )
