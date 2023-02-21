from dataclasses import dataclass, field
from typing import List, Optional
from .annotation import (
    AdminData,
    Annotation,
    DocumentationBlock,
)
from .boolean import Boolean
from .category_string import CategoryString
from .diag_event_debounce_counter_based import DiagEventDebounceCounterBased
from .diag_event_debounce_monitor_internal import DiagEventDebounceMonitorInternal
from .diag_event_debounce_time_based import DiagEventDebounceTimeBased
from .diag_requirement_id_string import DiagRequirementIdString
from .diagnostic_audience_enum import DiagnosticAudienceEnum
from .dtc_kind_enum import DtcKindEnum
from .function_inhibition_needs_subtypes_enum import FunctionInhibitionNeedsSubtypesEnum
from .identifier import Identifier
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .positive_integer import PositiveInteger
from .ref import Ref
from .report_behavior_enum import ReportBehaviorEnum
from .short_name_fragment import ShortNameFragment

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class DiagnosticEventNeeds:
    """Specifies the abstract needs on the configuration of the Diagnostic Event
    Manager for one diagnostic event.

    Its shortName can be regarded as a symbol identifying the diagnostic
    event from the viewpoint of the component or module which owns this
    element. In case the diagnostic event specifies a production error,
    the shortName shall be the name of the production error.

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
    :ivar consider_pto_status: PTO (Power Take Off) has an impact on the
        respective emission-related event (OBD). This information shall
        be provided by SW-C description in order to consider the PTO
        relevance e.g. for readiness (PID $01) computation. For events
        with dtcKind set to 'nonEmmissionRelatedDtc' this attribute is
        typically false.
    :ivar deferring_fid_refs: This reference contains the link to a
        function identifier within the FiM which is used by the monitor
        before delivering a result.
    :ivar diag_event_debounce_algorithm: Specifies the abstract need on
        the Debounce Algorithm applied by the Diagnostic Event Manager.
    :ivar dtc_kind: This attribute indicates the kind of the diagnostic
        monitor according to the SWS Diagnostic Event Manger. This
        attribute applies for the UDS diagnostics use case.
    :ivar dtc_number: This represents a reasonable Diagnostic Trouble
        Code. This allows to predefine the Diagnostic Trouble Code if
        the a function developer has received a particular requirement
        from the OEM or from a standardization body.
    :ivar inhibiting_fid_ref: This represents the primary Function
        Inhibition Identifier used for inhibition of the diagnostic
        monitor. The FID might either inhibit the monitoring of a
        symptom or the reporting of detected faults.
    :ivar inhibiting_secondary_fid_refs: This represents the secondary
        Function Inhibition Identifier used for inhibition of the
        diagnostic monitor. Any of the FID inhibitions leads to an
        inhibition of the monitoring of a symptom or the reporting of
        detected faults.
    :ivar obd_dtc_number: This represents a reasonable Diagnostic
        Trouble Code. This allows to predefine the Diagnostic Trouble
        Code, e.g. if the a function developer has received a particular
        requirement from the OEM or from a standardization body. This
        attribute applies for the OBD diagnostics use case.
    :ivar prestored_freezeframe_stored_in_nvm: If the Event uses a
        prestored freeze-frame (using the operations PrestoreFreezeFrame
        and ClearPrestoredFreezeFrame of the service interface
        DiagnosticMonitor) this attribute indicates if the Event
        requires the data to be stored in non-volatile memory. TRUE =
        Dem shall store the prestored data in non-volatile memory, FALSE
        = Data can be lost at shutdown (not stored in Nvm).
    :ivar report_behavior: This switch indicates whether or not the BSW
        module is allowed to report the related Events before
        Dem_Init().
    :ivar uds_dtc_number: This represents a reasonable Diagnostic
        Trouble Code. This allows to predefine the Diagnostic Trouble
        Code, e.g. if the a function developer has received a particular
        requirement from the OEM or from a standardization body. This
        attribute applies for the UDS diagnostics use case.
    :ivar uses_monitor_data: This attribute defines whether additional
        monitor data shall be added to the reporting of events.
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
        name = "DIAGNOSTIC-EVENT-NEEDS"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        }
    )
    short_name_fragments: Optional["DiagnosticEventNeeds.ShortNameFragments"] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME-FRAGMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    long_name: Optional[MultilanguageLongName] = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    desc: Optional[MultiLanguageOverviewParagraph] = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    category: Optional[CategoryString] = field(
        default=None,
        metadata={
            "name": "CATEGORY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    admin_data: Optional[AdminData] = field(
        default=None,
        metadata={
            "name": "ADMIN-DATA",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    introduction: Optional[DocumentationBlock] = field(
        default=None,
        metadata={
            "name": "INTRODUCTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    annotations: Optional["DiagnosticEventNeeds.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    audiences: Optional["DiagnosticEventNeeds.Audiences"] = field(
        default=None,
        metadata={
            "name": "AUDIENCES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    diag_requirement: Optional[DiagRequirementIdString] = field(
        default=None,
        metadata={
            "name": "DIAG-REQUIREMENT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    security_access_level: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "SECURITY-ACCESS-LEVEL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    consider_pto_status: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "CONSIDER-PTO-STATUS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    deferring_fid_refs: Optional["DiagnosticEventNeeds.DeferringFidRefs"] = field(
        default=None,
        metadata={
            "name": "DEFERRING-FID-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    diag_event_debounce_algorithm: Optional["DiagnosticEventNeeds.DiagEventDebounceAlgorithm"] = field(
        default=None,
        metadata={
            "name": "DIAG-EVENT-DEBOUNCE-ALGORITHM",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    dtc_kind: Optional[DtcKindEnum] = field(
        default=None,
        metadata={
            "name": "DTC-KIND",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    dtc_number: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "DTC-NUMBER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    inhibiting_fid_ref: Optional["DiagnosticEventNeeds.InhibitingFidRef"] = field(
        default=None,
        metadata={
            "name": "INHIBITING-FID-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    inhibiting_secondary_fid_refs: Optional["DiagnosticEventNeeds.InhibitingSecondaryFidRefs"] = field(
        default=None,
        metadata={
            "name": "INHIBITING-SECONDARY-FID-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    obd_dtc_number: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "OBD-DTC-NUMBER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    prestored_freezeframe_stored_in_nvm: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "PRESTORED-FREEZEFRAME-STORED-IN-NVM",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    report_behavior: Optional[ReportBehaviorEnum] = field(
        default=None,
        metadata={
            "name": "REPORT-BEHAVIOR",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    uds_dtc_number: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "UDS-DTC-NUMBER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    uses_monitor_data: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "USES-MONITOR-DATA",
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
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Attribute",
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

    @dataclass
    class Annotations:
        annotation: List[Annotation] = field(
            default_factory=list,
            metadata={
                "name": "ANNOTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
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
            }
        )

    @dataclass
    class DeferringFidRefs:
        deferring_fid_ref: List["DiagnosticEventNeeds.DeferringFidRefs.DeferringFidRef"] = field(
            default_factory=list,
            metadata={
                "name": "DEFERRING-FID-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

        @dataclass
        class DeferringFidRef(Ref):
            dest: Optional[FunctionInhibitionNeedsSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )

    @dataclass
    class DiagEventDebounceAlgorithm:
        diag_event_debounce_counter_based: Optional[DiagEventDebounceCounterBased] = field(
            default=None,
            metadata={
                "name": "DIAG-EVENT-DEBOUNCE-COUNTER-BASED",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        diag_event_debounce_monitor_internal: Optional[DiagEventDebounceMonitorInternal] = field(
            default=None,
            metadata={
                "name": "DIAG-EVENT-DEBOUNCE-MONITOR-INTERNAL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        diag_event_debounce_time_based: Optional[DiagEventDebounceTimeBased] = field(
            default=None,
            metadata={
                "name": "DIAG-EVENT-DEBOUNCE-TIME-BASED",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class InhibitingFidRef(Ref):
        dest: Optional[FunctionInhibitionNeedsSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class InhibitingSecondaryFidRefs:
        inhibiting_secondary_fid_ref: List["DiagnosticEventNeeds.InhibitingSecondaryFidRefs.InhibitingSecondaryFidRef"] = field(
            default_factory=list,
            metadata={
                "name": "INHIBITING-SECONDARY-FID-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

        @dataclass
        class InhibitingSecondaryFidRef(Ref):
            dest: Optional[FunctionInhibitionNeedsSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )
