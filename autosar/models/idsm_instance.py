from dataclasses import dataclass, field
from typing import List, Optional
from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .block_state import BlockState
from .category_string import CategoryString
from .ecu_instance_ref_conditional import EcuInstanceRefConditional
from .identifier import Identifier
from .idsm_module_instantiation_subtypes_enum import (
    IdsmModuleInstantiationSubtypesEnum,
)
from .idsm_rate_limitation_ref_conditional import (
    IdsmRateLimitationRefConditional,
)
from .idsm_signature_support_ap import IdsmSignatureSupportAp
from .idsm_signature_support_cp import IdsmSignatureSupportCp
from .idsm_traffic_limitation_ref_conditional import (
    IdsmTrafficLimitationRefConditional,
)
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .positive_integer import PositiveInteger
from .ref import Ref
from .short_name_fragment import ShortNameFragment
from .string import String

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class IdsmInstance:
    """
    This meta-class provides the ability to create a relation between an
    EcuInstance and a specific class of filters for security events that apply for
    all security events reported on the referenced EcuInstance.

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
    :ivar block_states: This reference defines the BlockState in the
        collection BlockStateSet.
    :ivar ecu_instances: This reference identifies the EcuInstance whose
        security events (of any type) shall be limited by the specific
        class of filters. This property was modified due to atpVariation
        (DirectedAssociationPattern).
    :ivar idsm_instance_id: This attribute is used to provide a source
        identification in the context of reporting security events..
    :ivar idsm_module_instantiation_ref: This reference identifies the
        meta-class that defines the attributes for the IdsM
        configuration on a specific machine.
    :ivar rate_limitation_filters: This reference identifies the
        applicable rate limitation filter for all security events on the
        related EcuInstance. This property was modified due to
        atpVariation (DirectedAssociationPattern).
    :ivar signature_support_ap: The existence of this aggregation
        specifies that the IdsM shall add a signature to the QSEv
        messages it sends onto the network. The cryptographic algorithm
        and key to be used for this signature is further specified by
        the aggregated meta-class specifically for the Adaptive
        Platform.
    :ivar signature_support_cp: The existence of this aggregation
        specifies that the IdsM shall add a signature to the QSEv
        messages it sends onto the network. The cryptographic algorithm
        and key to be used for this signature is further specified by
        the aggregated meta-class specifically for the Classic Platform.
    :ivar timestamp_format: The existence of this attribute specifies
        that the IdsM shall add a timestamp to the QSEv messages it
        sends onto the network. I.e., if this attribute does not exist,
        no timestamp shall be added to the QSEv messages. The content of
        this attribute further specifies the timestamp format as
        follows: - "AUTOSAR" defines AUTOSAR standardized timestamp
        format according to the Synchronized Time-Base Manager - Any
        other string defines a proprietary timestamp format. Note: A
        string defining a proprietary timestamp format shall be prefixed
        by a company-specific name fragment to avoid collisions.
    :ivar traffic_limitation_filters: This reference identifies the
        applicable traffic limitation filter for all security events on
        the related EcuInstance. This property was modified due to
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
        name = "IDSM-INSTANCE"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: Optional["IdsmInstance.ShortNameFragments"] = field(
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
    annotations: Optional["IdsmInstance.Annotations"] = field(
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
    block_states: Optional["IdsmInstance.BlockStates"] = field(
        default=None,
        metadata={
            "name": "BLOCK-STATES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    ecu_instances: Optional["IdsmInstance.EcuInstances"] = field(
        default=None,
        metadata={
            "name": "ECU-INSTANCES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    idsm_instance_id: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "IDSM-INSTANCE-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    idsm_module_instantiation_ref: Optional[
        "IdsmInstance.IdsmModuleInstantiationRef"
    ] = field(
        default=None,
        metadata={
            "name": "IDSM-MODULE-INSTANTIATION-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    rate_limitation_filters: Optional[
        "IdsmInstance.RateLimitationFilters"
    ] = field(
        default=None,
        metadata={
            "name": "RATE-LIMITATION-FILTERS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    signature_support_ap: Optional[IdsmSignatureSupportAp] = field(
        default=None,
        metadata={
            "name": "SIGNATURE-SUPPORT-AP",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    signature_support_cp: Optional[IdsmSignatureSupportCp] = field(
        default=None,
        metadata={
            "name": "SIGNATURE-SUPPORT-CP",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    timestamp_format: Optional[String] = field(
        default=None,
        metadata={
            "name": "TIMESTAMP-FORMAT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    traffic_limitation_filters: Optional[
        "IdsmInstance.TrafficLimitationFilters"
    ] = field(
        default=None,
        metadata={
            "name": "TRAFFIC-LIMITATION-FILTERS",
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
    class BlockStates:
        block_state: List[BlockState] = field(
            default_factory=list,
            metadata={
                "name": "BLOCK-STATE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class EcuInstances:
        ecu_instance_ref_conditional: List[EcuInstanceRefConditional] = field(
            default_factory=list,
            metadata={
                "name": "ECU-INSTANCE-REF-CONDITIONAL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class IdsmModuleInstantiationRef(Ref):
        dest: Optional[IdsmModuleInstantiationSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class RateLimitationFilters:
        idsm_rate_limitation_ref_conditional: List[
            IdsmRateLimitationRefConditional
        ] = field(
            default_factory=list,
            metadata={
                "name": "IDSM-RATE-LIMITATION-REF-CONDITIONAL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class TrafficLimitationFilters:
        idsm_traffic_limitation_ref_conditional: List[
            IdsmTrafficLimitationRefConditional
        ] = field(
            default_factory=list,
            metadata={
                "name": "IDSM-TRAFFIC-LIMITATION-REF-CONDITIONAL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
