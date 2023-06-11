from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class Tt:
    """This meta-class represents the ability to express specific technical terms.

    The kind of term is denoted in the attribute "type".

    :ivar value:
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
    :ivar tex_render: This attribute holds information how the content
        (represented by attribute "term") of the particular technical
        term is rendered using LaTeX. This allows to inject specific
        LaTeX commands such as \\sep{}.  An example is to render
        "MyClass" as "My\\sep{}Class". Default is the value of the
        attribute "term".
    :ivar type_value: This attribute specifies the type of the technical
        term. Values are such as "VARIABLE" "CALPRM". It is no longer an
        enum in order to support process specific extensions.
    """
    class Meta:
        name = "TT"

    value: str = field(
        default="",
        metadata={
            "required": True,
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
    tex_render: Optional[str] = field(
        default=None,
        metadata={
            "name": "TEX-RENDER",
            "type": "Attribute",
        }
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "TYPE",
            "type": "Attribute",
        }
    )
