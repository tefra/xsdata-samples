from dataclasses import dataclass, field
from typing import Optional

from .identifier import Identifier
from .short_name_fragment import ShortNameFragment
from .single_language_long_name import SingleLanguageLongName
from .string import String
from .url import Url

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class Xfile:
    """
    This represents to reference an external file within a documentation.

    :ivar short_name: This specifies an identifying shortName for the
        object. It needs to be unique within its context and is intended
        for humans but even more for technical reference.
    :ivar short_name_fragments: This specifies how the
        Referrable.shortName is composed of several shortNameFragments.
    :ivar long_name_1: This specifies the long name of the object. The
        role is longName1 for compatibilty to ASAM FSX
    :ivar url: This represents the URL of the external file.
    :ivar tool: This element describes the tool which was used to
        generate the corresponding Xfile . Kept as a string since no
        specific syntax can be provided to denote a tool.
    :ivar tool_version: This element describes the tool version which
        was used to generate the corresponding xfile. Kept as a string,
        since no specific syntax can be specified.
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
        name = "XFILE"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: Optional["Xfile.ShortNameFragments"] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME-FRAGMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    long_name_1: Optional[SingleLanguageLongName] = field(
        default=None,
        metadata={
            "name": "LONG-NAME-1",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    url: Optional[Url] = field(
        default=None,
        metadata={
            "name": "URL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tool: Optional[String] = field(
        default=None,
        metadata={
            "name": "TOOL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tool_version: Optional[String] = field(
        default=None,
        metadata={
            "name": "TOOL-VERSION",
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
    class ShortNameFragments:
        short_name_fragment: list[ShortNameFragment] = field(
            default_factory=list,
            metadata={
                "name": "SHORT-NAME-FRAGMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
