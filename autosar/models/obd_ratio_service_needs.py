from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.annotation import (
    AdminData,
    Annotation,
    DocumentationBlock,
)
from autosar.models.category_string import CategoryString
from autosar.models.diag_requirement_id_string import DiagRequirementIdString
from autosar.models.diagnostic_audience_enum import DiagnosticAudienceEnum
from autosar.models.diagnostic_denominator_condition_enum import DiagnosticDenominatorConditionEnum
from autosar.models.diagnostic_event_needs_subtypes_enum import DiagnosticEventNeedsSubtypesEnum
from autosar.models.function_inhibition_needs_subtypes_enum import FunctionInhibitionNeedsSubtypesEnum
from autosar.models.identifier import Identifier
from autosar.models.multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from autosar.models.multilanguage_long_name import MultilanguageLongName
from autosar.models.nmtoken_string import NmtokenString
from autosar.models.obd_ratio_connection_kind_enum import ObdRatioConnectionKindEnum
from autosar.models.positive_integer import PositiveInteger
from autosar.models.ref import Ref
from autosar.models.short_name_fragment import ShortNameFragment

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ObdRatioServiceNeeds:
    """
    Specifies the abstract needs of a component or module on the configuration
    of OBD Services in relation to a particular "ratio monitoring" which is
    supported by this component or module.

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
        object in question.  More elaborate documentation, (in
        particular how the object is built or used) should go to
        "introduction".
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
        which the object can be linked to.  Note that with the
        implementation of a generic tracing concept in AUTOSAR this
        attribute might become obsolete.
    :ivar security_access_level: This attribute denotes the level of
        security which is touched by the diagnostic object. The higher
        the level the more relevance for the security exists.  This
        level shall be mapped to the security level in the ECU.
    :ivar connection_type: Defines how the DEM is connected to the
        component or module to perform the IUMPR (In use monitor
        performance ratio) service.
    :ivar denominator_group: The denominator Dem shall use to compute
        the ratio.
    :ivar iumpr_group: Defines the IUMPR (In use monitor performance
        ratio) Group of the SAE standard. Note that possible values are
        not predefined by an enumeration meta-type in order to make the
        meta-model independent of the details of the SAE standard.
    :ivar rate_based_monitored_event_ref: The rate based monitored
        Diagnostic Event.
    :ivar used_fid_ref: This represents the primary Function Inhibition
        Identifier used for the rate based monitor. This is an optional
        attribute.
    :ivar used_secondary_fid_refs: This represents the secondary
        Function Inhibition Identifier used for the rate based monitor.
        This is an optional attribute. Any of the FID inhibitions leads
        to an inhibition of the IUMPR calculation
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
        different AUTOSAR models.  The form of the UUID (Universally
        Unique Identifier) is taken from a standard defined by the Open
        Group (was Open Software Foundation). This standard is widely
        used, including by Microsoft for COM (GUIDs) and by many
        companies for DCE, which is based on CORBA. The method for
        generating these 128-bit IDs is published in the standard and
        the effectiveness and uniqueness of the IDs is not in practice
        disputed. If the id namespace is omitted, DCE is assumed.  An
        example is "DCE:2fac1234-31f8-11b4-a222-08002b34c003". The uuid
        attribute has no semantic meaning for an AUTOSAR model and there
        is no requirement for AUTOSAR tools to manage the timestamp.
    """
    class Meta:
        name = "OBD-RATIO-SERVICE-NEEDS"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        }
    )
    short_name_fragments: Optional["ObdRatioServiceNeeds.ShortNameFragments"] = field(
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
    annotations: Optional["ObdRatioServiceNeeds.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    audiences: Optional["ObdRatioServiceNeeds.Audiences"] = field(
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
    connection_type: Optional[ObdRatioConnectionKindEnum] = field(
        default=None,
        metadata={
            "name": "CONNECTION-TYPE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    denominator_group: Optional[DiagnosticDenominatorConditionEnum] = field(
        default=None,
        metadata={
            "name": "DENOMINATOR-GROUP",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    iumpr_group: Optional[NmtokenString] = field(
        default=None,
        metadata={
            "name": "IUMPR-GROUP",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    rate_based_monitored_event_ref: Optional["ObdRatioServiceNeeds.RateBasedMonitoredEventRef"] = field(
        default=None,
        metadata={
            "name": "RATE-BASED-MONITORED-EVENT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    used_fid_ref: Optional["ObdRatioServiceNeeds.UsedFidRef"] = field(
        default=None,
        metadata={
            "name": "USED-FID-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    used_secondary_fid_refs: Optional["ObdRatioServiceNeeds.UsedSecondaryFidRefs"] = field(
        default=None,
        metadata={
            "name": "USED-SECONDARY-FID-REFS",
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
    class RateBasedMonitoredEventRef(Ref):
        dest: Optional[DiagnosticEventNeedsSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class UsedFidRef(Ref):
        dest: Optional[FunctionInhibitionNeedsSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class UsedSecondaryFidRefs:
        used_secondary_fid_ref: List["ObdRatioServiceNeeds.UsedSecondaryFidRefs.UsedSecondaryFidRef"] = field(
            default_factory=list,
            metadata={
                "name": "USED-SECONDARY-FID-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

        @dataclass
        class UsedSecondaryFidRef(Ref):
            dest: Optional[FunctionInhibitionNeedsSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )
