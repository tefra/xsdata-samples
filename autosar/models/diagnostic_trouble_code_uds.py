from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .boolean import Boolean
from .category_string import CategoryString
from .diagnostic_trouble_code_props_subtypes_enum import (
    DiagnosticTroubleCodePropsSubtypesEnum,
)
from .diagnostic_uds_severity_enum import DiagnosticUdsSeverityEnum
from .diagnostic_wwh_obd_dtc_class_enum_value_variation_point import (
    DiagnosticWwhObdDtcClassEnumValueVariationPoint,
)
from .identifier import Identifier
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .nmtoken_string import NmtokenString
from .positive_integer import PositiveInteger
from .positive_integer_value_variation_point import (
    PositiveIntegerValueVariationPoint,
)
from .ref import Ref
from .short_name_fragment import ShortNameFragment

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class DiagnosticTroubleCodeUds:
    """
    This element is used to describe non OBD-relevant DTCs.

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
    :ivar consider_pto_status: This attribute describes the affection of
        the event by the Dem PTO handling. True: the event is affected
        by the Dem PTO handling. False: the event is not affected by the
        Dem PTO handling.
    :ivar dtc_props_ref: Defined properties associated with the DemDTC.
    :ivar event_obd_readiness_group: This attribute specifies the Event
        OBD Readiness group for PID $01 and PID $41 computation. This
        attribute is only applicable for emission-related ECUs.
    :ivar functional_unit: This attribute specifies a 1-byte value which
        identifies the corresponding basic vehicle / system function
        which reports the DTC. This parameter is necessary for the
        report of severity information.
    :ivar severity: DTC severity according to ISO 14229-1.
    :ivar uds_dtc_value: Unique Diagnostic Trouble Code value for UDS.
    :ivar wwh_obd_dtc_class: This attribute is used to identify (if
        applicable) the corresponding severity class of an WWH-OBD DTC.
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
        name = "DIAGNOSTIC-TROUBLE-CODE-UDS"

    short_name: Identifier = field(
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        }
    )
    short_name_fragments: (
        None | DiagnosticTroubleCodeUds.ShortNameFragments
    ) = field(
        default=None,
        metadata={
            "name": "SHORT-NAME-FRAGMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    long_name: None | MultilanguageLongName = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    desc: None | MultiLanguageOverviewParagraph = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    category: None | CategoryString = field(
        default=None,
        metadata={
            "name": "CATEGORY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    admin_data: None | AdminData = field(
        default=None,
        metadata={
            "name": "ADMIN-DATA",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    introduction: None | DocumentationBlock = field(
        default=None,
        metadata={
            "name": "INTRODUCTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    annotations: None | DiagnosticTroubleCodeUds.Annotations = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: None | VariationPoint = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    consider_pto_status: None | Boolean = field(
        default=None,
        metadata={
            "name": "CONSIDER-PTO-STATUS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    dtc_props_ref: None | DiagnosticTroubleCodeUds.DtcPropsRef = field(
        default=None,
        metadata={
            "name": "DTC-PROPS-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    event_obd_readiness_group: None | NmtokenString = field(
        default=None,
        metadata={
            "name": "EVENT-OBD-READINESS-GROUP",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    functional_unit: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "FUNCTIONAL-UNIT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    severity: None | DiagnosticUdsSeverityEnum = field(
        default=None,
        metadata={
            "name": "SEVERITY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    uds_dtc_value: None | PositiveIntegerValueVariationPoint = field(
        default=None,
        metadata={
            "name": "UDS-DTC-VALUE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    wwh_obd_dtc_class: (
        None | DiagnosticWwhObdDtcClassEnumValueVariationPoint
    ) = field(
        default=None,
        metadata={
            "name": "WWH-OBD-DTC-CLASS",
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
    uuid: None | str = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class ShortNameFragments:
        short_name_fragment: list[ShortNameFragment] = field(
            default_factory=list,
            metadata={
                "name": "SHORT-NAME-FRAGMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass(kw_only=True)
    class Annotations:
        annotation: list[Annotation] = field(
            default_factory=list,
            metadata={
                "name": "ANNOTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass(kw_only=True)
    class DtcPropsRef(Ref):
        dest: DiagnosticTroubleCodePropsSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
