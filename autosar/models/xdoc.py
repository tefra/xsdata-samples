from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.date import Date
from autosar.models.identifier import Identifier
from autosar.models.short_name_fragment import ShortNameFragment
from autosar.models.single_language_long_name import SingleLanguageLongName
from autosar.models.string import String
from autosar.models.url import Url

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class Xdoc:
    """
    This meta-class represents the ability to refer to an external document
    which can be rendered as printed matter.

    :ivar short_name: This specifies an identifying shortName for the
        object. It needs to be unique within its context and is intended
        for humans but even more for technical reference.
    :ivar short_name_fragments: This specifies how the
        Referrable.shortName is composed of several shortNameFragments.
    :ivar long_name_1: This specifies the long name of the object. The
        role is longName1 for compatibilty to ASAM FSX
    :ivar number: This represents document number of an external
        document that is referenced. Kept as a string.
    :ivar state: This represents version and state of the external
        document. Kept as a string.
    :ivar date: This element specifies the release date of the external
        document if applicable.
    :ivar publisher: This represents the publisher of an external
        document that is being referenced. Kept as a string.
    :ivar url: This specifies the URL of the external document.
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
        name = "XDOC"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        }
    )
    short_name_fragments: Optional["Xdoc.ShortNameFragments"] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME-FRAGMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    long_name_1: Optional[SingleLanguageLongName] = field(
        default=None,
        metadata={
            "name": "LONG-NAME-1",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    number: Optional[String] = field(
        default=None,
        metadata={
            "name": "NUMBER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    state: Optional[String] = field(
        default=None,
        metadata={
            "name": "STATE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    date: Optional[Date] = field(
        default=None,
        metadata={
            "name": "DATE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    publisher: Optional[String] = field(
        default=None,
        metadata={
            "name": "PUBLISHER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    url: Optional[Url] = field(
        default=None,
        metadata={
            "name": "URL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    position: Optional[String] = field(
        default=None,
        metadata={
            "name": "POSITION",
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
    class ShortNameFragments:
        short_name_fragment: List[ShortNameFragment] = field(
            default_factory=list,
            metadata={
                "name": "SHORT-NAME-FRAGMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
