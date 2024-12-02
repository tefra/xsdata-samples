from dataclasses import dataclass, field
from typing import Optional

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .boolean import Boolean
from .category_string import CategoryString
from .diagnostic_aging_subtypes_enum import DiagnosticAgingSubtypesEnum
from .diagnostic_data_identifier_set_ref_conditional import (
    DiagnosticDataIdentifierSetRefConditional,
)
from .diagnostic_data_identifier_set_subtypes_enum import (
    DiagnosticDataIdentifierSetSubtypesEnum,
)
from .diagnostic_extended_data_record_ref_conditional import (
    DiagnosticExtendedDataRecordRefConditional,
)
from .diagnostic_freeze_frame_ref_conditional import (
    DiagnosticFreezeFrameRefConditional,
)
from .diagnostic_memory_destination_subtypes_enum import (
    DiagnosticMemoryDestinationSubtypesEnum,
)
from .diagnostic_significance_enum import DiagnosticSignificanceEnum
from .environment_capture_to_reporting_enum import (
    EnvironmentCaptureToReportingEnum,
)
from .identifier import Identifier
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .positive_integer import PositiveInteger
from .positive_integer_value_variation_point import (
    PositiveIntegerValueVariationPoint,
)
from .ref import Ref
from .short_name_fragment import ShortNameFragment

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class DiagnosticTroubleCodeProps:
    """
    This element defines common Dtc properties that can be reused by different non
    OBD-relevant DTCs.

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
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
    :ivar aging_allowed: This represents the decision whether aging is
        allowed for this DiagnosticTroubleCodeProps.
    :ivar aging_ref: Reference to an aging algorithm in case that an
        aging/unlearning of the event is allowed.
    :ivar environment_capture_to_reporting: This attribute determines
        the point in time, when the data actually is captured.
    :ivar extended_data_records: Defines the links to an extended data
        class sampler. This property was modified due to atpVariation
        (DirectedAssociationPattern).
    :ivar fdc_threshold_storage_value: Threshold to allocate an event
        memory entry and to capture the Freeze Frame. Unit: none
        (attribute represents a counter value).
    :ivar freeze_frames: Define the links to a freeze frame class
        sampler. This property was modified due to atpVariation
        (DirectedAssociationPattern).
    :ivar freeze_frame_content_ref: This represents the freeze frame
        layout as a set of DIDs.
    :ivar freeze_frame_content_wwh_obd_ref: This reefrence identifies
        the layout of the WWH-OBD freeze frame.
    :ivar immediate_nv_data_storage: Switch to enable immediate storage
        triggering of an according event memory entry persistently to
        NVRAM. true: immediate non-volatile storage triggering enabled
        false: immediate non-volatile storage triggering disabled
    :ivar legislated_freeze_frame_content_wwh_obds: This reference
        identifies the layout of the WWH-OBD freeze frame. This property
        was modified due to atpVariation (DirectedAssociationPattern).
    :ivar max_number_freeze_frame_records: This attribute defines the
        number of according freeze frame records, which can maximal be
        stored for this event. Therefore all these freeze frame records
        have the same freeze frame class.
    :ivar memory_destination_refs: The event destination assigns events
        to none, one or multiple origins.
    :ivar priority: Priority of the event, in view of full event buffer.
        A lower value means higher priority.
    :ivar significance: Significance of the event, which indicates
        additional information concerning fault classification and
        resolution.
    :ivar snapshot_record_contents: This represents the freeze frame
        layout as a set of DIDs. This property was modified due to
        atpVariation (DirectedAssociationPattern).
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
        name = "DIAGNOSTIC-TROUBLE-CODE-PROPS"

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
        "DiagnosticTroubleCodeProps.ShortNameFragments"
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
    annotations: Optional["DiagnosticTroubleCodeProps.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: Optional[VariationPoint] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    aging_allowed: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "AGING-ALLOWED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    aging_ref: Optional["DiagnosticTroubleCodeProps.AgingRef"] = field(
        default=None,
        metadata={
            "name": "AGING-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    environment_capture_to_reporting: Optional[
        EnvironmentCaptureToReportingEnum
    ] = field(
        default=None,
        metadata={
            "name": "ENVIRONMENT-CAPTURE-TO-REPORTING",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    extended_data_records: Optional[
        "DiagnosticTroubleCodeProps.ExtendedDataRecords"
    ] = field(
        default=None,
        metadata={
            "name": "EXTENDED-DATA-RECORDS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    fdc_threshold_storage_value: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "FDC-THRESHOLD-STORAGE-VALUE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    freeze_frames: Optional["DiagnosticTroubleCodeProps.FreezeFrames"] = field(
        default=None,
        metadata={
            "name": "FREEZE-FRAMES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    freeze_frame_content_ref: Optional[
        "DiagnosticTroubleCodeProps.FreezeFrameContentRef"
    ] = field(
        default=None,
        metadata={
            "name": "FREEZE-FRAME-CONTENT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    freeze_frame_content_wwh_obd_ref: Optional[
        "DiagnosticTroubleCodeProps.FreezeFrameContentWwhObdRef"
    ] = field(
        default=None,
        metadata={
            "name": "FREEZE-FRAME-CONTENT-WWH-OBD-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    immediate_nv_data_storage: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "IMMEDIATE-NV-DATA-STORAGE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    legislated_freeze_frame_content_wwh_obds: Optional[
        "DiagnosticTroubleCodeProps.LegislatedFreezeFrameContentWwhObds"
    ] = field(
        default=None,
        metadata={
            "name": "LEGISLATED-FREEZE-FRAME-CONTENT-WWH-OBDS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    max_number_freeze_frame_records: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "MAX-NUMBER-FREEZE-FRAME-RECORDS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    memory_destination_refs: Optional[
        "DiagnosticTroubleCodeProps.MemoryDestinationRefs"
    ] = field(
        default=None,
        metadata={
            "name": "MEMORY-DESTINATION-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    priority: Optional[PositiveIntegerValueVariationPoint] = field(
        default=None,
        metadata={
            "name": "PRIORITY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    significance: Optional[DiagnosticSignificanceEnum] = field(
        default=None,
        metadata={
            "name": "SIGNIFICANCE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    snapshot_record_contents: Optional[
        "DiagnosticTroubleCodeProps.SnapshotRecordContents"
    ] = field(
        default=None,
        metadata={
            "name": "SNAPSHOT-RECORD-CONTENTS",
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
        short_name_fragment: list[ShortNameFragment] = field(
            default_factory=list,
            metadata={
                "name": "SHORT-NAME-FRAGMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class Annotations:
        annotation: list[Annotation] = field(
            default_factory=list,
            metadata={
                "name": "ANNOTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class AgingRef(Ref):
        dest: Optional[DiagnosticAgingSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class ExtendedDataRecords:
        diagnostic_extended_data_record_ref_conditional: list[
            DiagnosticExtendedDataRecordRefConditional
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-EXTENDED-DATA-RECORD-REF-CONDITIONAL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class FreezeFrames:
        diagnostic_freeze_frame_ref_conditional: list[
            DiagnosticFreezeFrameRefConditional
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-FREEZE-FRAME-REF-CONDITIONAL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class FreezeFrameContentRef(Ref):
        dest: Optional[DiagnosticDataIdentifierSetSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class FreezeFrameContentWwhObdRef(Ref):
        dest: Optional[DiagnosticDataIdentifierSetSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class LegislatedFreezeFrameContentWwhObds:
        diagnostic_data_identifier_set_ref_conditional: list[
            DiagnosticDataIdentifierSetRefConditional
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-DATA-IDENTIFIER-SET-REF-CONDITIONAL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class MemoryDestinationRefs:
        memory_destination_ref: list[
            "DiagnosticTroubleCodeProps.MemoryDestinationRefs.MemoryDestinationRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "MEMORY-DESTINATION-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class MemoryDestinationRef(Ref):
            dest: Optional[DiagnosticMemoryDestinationSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class SnapshotRecordContents:
        diagnostic_data_identifier_set_ref_conditional: list[
            DiagnosticDataIdentifierSetRefConditional
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-DATA-IDENTIFIER-SET-REF-CONDITIONAL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
