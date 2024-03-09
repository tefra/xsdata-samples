from dataclasses import dataclass, field
from typing import List, Optional

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
)
from .application_data_type_subtypes_enum import (
    ApplicationDataTypeSubtypesEnum,
)
from .category_string import CategoryString
from .diag_requirement_id_string import DiagRequirementIdString
from .diagnostic_audience_enum import DiagnosticAudienceEnum
from .diagnostic_event_needs_subtypes_enum import (
    DiagnosticEventNeedsSubtypesEnum,
)
from .diagnostic_monitor_update_kind_enum import (
    DiagnosticMonitorUpdateKindEnum,
)
from .identifier import Identifier
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .positive_integer import PositiveInteger
from .ref import Ref
from .short_name_fragment import ShortNameFragment

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ObdMonitorServiceNeeds:
    """Specifies the abstract needs of a component or module on the configuration
    of OBD Services in relation to a particular on-board monitoring test supported
    by this component or module.

    (OBD Service 06).

    :ivar short_name: This specifies an identifying shortName for the
        object. It needs to be unique within its context and is intended
        for humans but even more for technical reference.
    :ivar short_name_fragments: This specifies how the
        Referrable.shortName is composed of several shortNameFragments.
    :ivar long_name: This specifies the long name of the object. Long
        name is targeted to human readers and acts like a headline.
    :ivar desc: This represents a general but brief (one paragraph)
        description what the object in question is about. It is only one
        paragraph! Desc is intended to be collected into overview
        tables. This property helps a human reader to identify the
        object in question. More elaborate documentation, (in particular
        how the object is built or used) should go to "introduction".
    :ivar category: The category is a keyword that specializes the
        semantics of the Identifiable. It affects the expected existence
        of attributes and the applicability of constraints.
    :ivar admin_data: This represents the administrative data for the
        identifiable object.
    :ivar introduction: This represents more information about how the
        object in question is built or is used. Therefore it is a
        DocumentationBlock.
    :ivar annotations: Possibility to provide additional notes while
        defining a model element (e.g. the ECU Configuration Parameter
        Values). These are not intended as documentation but are mere
        design notes.
    :ivar audiences:
    :ivar diag_requirement: This denotes the requirement identifier to
        which the object can be linked to. Note that with the
        implementation of a generic tracing concept in AUTOSAR this
        attribute might become obsolete.
    :ivar security_access_level: This attribute denotes the level of
        security which is touched by the diagnostic object. The higher
        the level the more relevance for the security exists. This level
        shall be mapped to the security level in the ECU.
    :ivar application_data_type_ref: reference to an ApplicationDataType
        that describes the scaling of the data reported by the software-
        component to the Dem.
    :ivar event_needs_ref: This reference identifies the corresponding
        diagnostic event.
    :ivar on_board_monitor_id: On-board monitor ID according to ISO
        15031-5.
    :ivar test_id: Test Identifier (TID) according to ISO 15031-5.
    :ivar unit_and_scaling_id: Unit and scaling ID according to ISO
        15031-5.
    :ivar update_kind: This attribute indicates the settings for the
        acceptance of updates.
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
    :ivar uuid: The purpose of this attribute is to provide a globally
        unique identifier for an instance of a meta-class. The values of
        this attribute should be globally unique strings prefixed by the
        type of identifier.  For example, to include a DCE UUID as
        defined by The Open Group, the UUID would be preceded by "DCE:".
        The values of this attribute may be used to support merging of
        different AUTOSAR models. The form of the UUID (Universally
        Unique Identifier) is taken from a standard defined by the Open
        Group (was Open Software Foundation). This standard is widely
        used, including by Microsoft for COM (GUIDs) and by many
        companies for DCE, which is based on CORBA. The method for
        generating these 128-bit IDs is published in the standard and
        the effectiveness and uniqueness of the IDs is not in practice
        disputed. If the id namespace is omitted, DCE is assumed. An
        example is "DCE:2fac1234-31f8-11b4-a222-08002b34c003". The uuid
        attribute has no semantic meaning for an AUTOSAR model and there
        is no requirement for AUTOSAR tools to manage the timestamp.
    """

    class Meta:
        name = "OBD-MONITOR-SERVICE-NEEDS"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: Optional[
        "ObdMonitorServiceNeeds.ShortNameFragments"
    ] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME-FRAGMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    long_name: Optional[MultilanguageLongName] = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
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
    category: Optional[CategoryString] = field(
        default=None,
        metadata={
            "name": "CATEGORY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    admin_data: Optional[AdminData] = field(
        default=None,
        metadata={
            "name": "ADMIN-DATA",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    introduction: Optional[DocumentationBlock] = field(
        default=None,
        metadata={
            "name": "INTRODUCTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    annotations: Optional["ObdMonitorServiceNeeds.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    audiences: Optional["ObdMonitorServiceNeeds.Audiences"] = field(
        default=None,
        metadata={
            "name": "AUDIENCES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    diag_requirement: Optional[DiagRequirementIdString] = field(
        default=None,
        metadata={
            "name": "DIAG-REQUIREMENT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    security_access_level: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "SECURITY-ACCESS-LEVEL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    application_data_type_ref: Optional[
        "ObdMonitorServiceNeeds.ApplicationDataTypeRef"
    ] = field(
        default=None,
        metadata={
            "name": "APPLICATION-DATA-TYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    event_needs_ref: Optional["ObdMonitorServiceNeeds.EventNeedsRef"] = field(
        default=None,
        metadata={
            "name": "EVENT-NEEDS-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    on_board_monitor_id: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "ON-BOARD-MONITOR-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    test_id: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "TEST-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    unit_and_scaling_id: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "UNIT-AND-SCALING-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    update_kind: Optional[DiagnosticMonitorUpdateKindEnum] = field(
        default=None,
        metadata={
            "name": "UPDATE-KIND",
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
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Attribute",
        },
    )

    @dataclass
    class ShortNameFragments:
        short_name_fragment: List[ShortNameFragment] = field(
            default_factory=list,
            metadata={
                "name": "SHORT-NAME-FRAGMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class Annotations:
        annotation: List[Annotation] = field(
            default_factory=list,
            metadata={
                "name": "ANNOTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class Audiences:
        """
        :ivar audience: This specifies the intended audience for the
            diagnostic object. Note that this is not only for the
            documentation but also subsequent audience specific
            implementation.
        """

        audience: List[DiagnosticAudienceEnum] = field(
            default_factory=list,
            metadata={
                "name": "AUDIENCE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class ApplicationDataTypeRef(Ref):
        dest: Optional[ApplicationDataTypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class EventNeedsRef(Ref):
        dest: Optional[DiagnosticEventNeedsSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
