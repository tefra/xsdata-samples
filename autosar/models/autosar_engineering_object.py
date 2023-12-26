from dataclasses import dataclass, field
from typing import List, Optional
from .nmtoken_string import NmtokenString
from .revision_label_string import RevisionLabelString

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class AutosarEngineeringObject:
    """This denotes an engineering object being part of the process.

    It is a specialization of the abstract class EngineeringObject for
    usage within AUTOSAR.

    :ivar short_label: This is the short name of the engineering object.
        Note that it is modeled as NameToken and not as Identifier since
        in ASAM-CC it is also a NameToken.
    :ivar category: This denotes the role of the engineering object in
        the development cycle. Categories are such as * SWSRC for source
        code * SWOBJ for object code * SWHDR for a C-header file Further
        roles need to be defined via Methodology.
    :ivar revision_labels:
    :ivar domain: This denotes the domain in which the engineering
        object is stored. This allows to indicate various segments in
        the repository keeping the engineering objects. The domain may
        segregate companies, as well as automotive domains. Details need
        to be defined by the Methodology. Attribute is optional to
        support a default domain.
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
        name = "AUTOSAR-ENGINEERING-OBJECT"

    short_label: Optional[NmtokenString] = field(
        default=None,
        metadata={
            "name": "SHORT-LABEL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    category: Optional[NmtokenString] = field(
        default=None,
        metadata={
            "name": "CATEGORY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    revision_labels: Optional[
        "AutosarEngineeringObject.RevisionLabels"
    ] = field(
        default=None,
        metadata={
            "name": "REVISION-LABELS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    domain: Optional[NmtokenString] = field(
        default=None,
        metadata={
            "name": "DOMAIN",
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
    class RevisionLabels:
        """
        :ivar revision_label: This is a revision label denoting a
            particular version of the engineering object.
        """

        revision_label: List[RevisionLabelString] = field(
            default_factory=list,
            metadata={
                "name": "REVISION-LABEL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
