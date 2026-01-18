from __future__ import annotations

from dataclasses import dataclass, field

from .date import Date
from .identifier import Identifier
from .short_name_fragment import ShortNameFragment
from .single_language_long_name import SingleLanguageLongName
from .string import String
from .url import Url

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class Std:
    """
    This represents a reference to external standards.

    :ivar short_name: This specifies an identifying shortName for the
        object. It needs to be unique within its context and is intended
        for humans but even more for technical reference.
    :ivar short_name_fragments: This specifies how the
        Referrable.shortName is composed of several shortNameFragments.
    :ivar long_name_1: This specifies the long name of the object. The
        role is longName1 for compatibilty to ASAM FSX
    :ivar subtitle: This represents the subtitle of the standard.
    :ivar state: This represents  version and state of a standard. Kept
        as a string.
    :ivar date: This element specifies the release date of the external
        standard if applicable.
    :ivar url: This represents the URL of the standard.
    :ivar position: This represents the reference to the relevant
        positions of a standard. Kept as a string.
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
        name = "STD"

    short_name: None | Identifier = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: None | Std.ShortNameFragments = field(
        default=None,
        metadata={
            "name": "SHORT-NAME-FRAGMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    long_name_1: None | SingleLanguageLongName = field(
        default=None,
        metadata={
            "name": "LONG-NAME-1",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    subtitle: None | String = field(
        default=None,
        metadata={
            "name": "SUBTITLE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    state: None | String = field(
        default=None,
        metadata={
            "name": "STATE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    date: None | Date = field(
        default=None,
        metadata={
            "name": "DATE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    url: None | Url = field(
        default=None,
        metadata={
            "name": "URL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    position: None | String = field(
        default=None,
        metadata={
            "name": "POSITION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: None | str = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: None | str = field(
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
