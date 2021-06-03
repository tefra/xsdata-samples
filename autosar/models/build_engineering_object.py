from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.nmtoken_string import NmtokenString
from autosar.models.regular_expression import RegularExpression
from autosar.models.revision_label_string import RevisionLabelString
from autosar.models.uri_string import UriString

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class BuildEngineeringObject:
    """
    This meta-class represents the ability to denote an artifact which is
    processed within a particular build action.

    :ivar short_label: This is the short name of the engineering object.
        Note that it is modeled as NameToken and not as Identifier since
        in ASAM-CC it is also a NameToken.
    :ivar category: This denotes the role of the engineering object in
        the development cycle.  Categories are such as  * SWSRC for
        source code * SWOBJ for object code * SWHDR for a C-header file
        Further roles need to be defined via Methodology.
    :ivar revision_labels:
    :ivar domain: This denotes the domain in which the engineering
        object is stored. This allows to indicate various segments in
        the repository keeping the engineering objects. The domain may
        segregate companies, as well as automotive domains. Details need
        to be defined by the Methodology.  Attribute is optional to
        support a default domain.
    :ivar file_type: This attribute indicates the file type which shall
        used for the engineering object. Note that an engineering object
        may deliver multiple representations of the same artifact. This
        attribute can select one of the provided representations.
    :ivar intended_filename: This attribute represents the name of the
        file if it is created newly. Note that engineering object
        resolves category + ShortLabel indicate mainly to refer to an
        existing file. If the file is created newly, the filename can
        either be determined by built in policy or predefined here.
        Note that extensions shall part of file name even if it could be
        derived from fileType.
    :ivar parent_category: This represents the category of the parent
        object.
    :ivar parent_short_label: This represents the shortLabel of the
        parent object. This allows to specify the output position in a
        hierarchically organized sysyetm
    :ivar short_label_pattern: This attribute allows to define a set of
        engineering objects as pattern based search applied to the
        shortLabel of the individual Enginering objects.
    :ivar file_type_pattern: This attribute allows to define a set of
        engineering objects as pattern based search applied to the
        filetype of the individual Engineering objects.
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
        name = "BUILD-ENGINEERING-OBJECT"

    short_label: Optional[NmtokenString] = field(
        default=None,
        metadata={
            "name": "SHORT-LABEL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    category: Optional[NmtokenString] = field(
        default=None,
        metadata={
            "name": "CATEGORY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    revision_labels: Optional["BuildEngineeringObject.RevisionLabels"] = field(
        default=None,
        metadata={
            "name": "REVISION-LABELS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    domain: Optional[NmtokenString] = field(
        default=None,
        metadata={
            "name": "DOMAIN",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    file_type: Optional[NmtokenString] = field(
        default=None,
        metadata={
            "name": "FILE-TYPE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    intended_filename: Optional[UriString] = field(
        default=None,
        metadata={
            "name": "INTENDED-FILENAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    parent_category: Optional[NmtokenString] = field(
        default=None,
        metadata={
            "name": "PARENT-CATEGORY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    parent_short_label: Optional[NmtokenString] = field(
        default=None,
        metadata={
            "name": "PARENT-SHORT-LABEL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    short_label_pattern: Optional[RegularExpression] = field(
        default=None,
        metadata={
            "name": "SHORT-LABEL-PATTERN",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    file_type_pattern: Optional[RegularExpression] = field(
        default=None,
        metadata={
            "name": "FILE-TYPE-PATTERN",
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
            }
        )
