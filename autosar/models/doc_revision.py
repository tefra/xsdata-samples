from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.date import Date
from autosar.models.modification import Modification
from autosar.models.nmtoken_string import NmtokenString
from autosar.models.revision_label_string import RevisionLabelString
from autosar.models.string import String

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class DocRevision:
    """
    This meta-class represents the ability to maintain information which
    relates to revision management of documents or objects.

    :ivar revision_label: This attribute represents the version number
        of the object.
    :ivar revision_label_p_1: This attribute represents the version
        number of the first predecessor  of the object.
    :ivar revision_label_p_2: This attribute represents the version
        number of the second predecessor of the object.  This attribute
        is used if the object is the result of a merge process in which
        two branches are merged in to one new revision.
    :ivar state: The attribute state represents the current state of the
        current file according to the configuration management plan. It
        is a NameToken until possible states are  standardized.
    :ivar issued_by: This is the name of an individual or an
        organization who issued the current revision of the document or
        document fragment.
    :ivar date: This specifies the date and time, when the object in
        question was released
    :ivar modifications: This property represents one particular
        modification in comparison to its predecessor.
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
        name = "DOC-REVISION"

    revision_label: Optional[RevisionLabelString] = field(
        default=None,
        metadata={
            "name": "REVISION-LABEL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    revision_label_p_1: Optional[RevisionLabelString] = field(
        default=None,
        metadata={
            "name": "REVISION-LABEL-P-1",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    revision_label_p_2: Optional[RevisionLabelString] = field(
        default=None,
        metadata={
            "name": "REVISION-LABEL-P-2",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    state: Optional[NmtokenString] = field(
        default=None,
        metadata={
            "name": "STATE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    issued_by: Optional[String] = field(
        default=None,
        metadata={
            "name": "ISSUED-BY",
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
    modifications: Optional["DocRevision.Modifications"] = field(
        default=None,
        metadata={
            "name": "MODIFICATIONS",
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
    class Modifications:
        modification: List[Modification] = field(
            default_factory=list,
            metadata={
                "name": "MODIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
