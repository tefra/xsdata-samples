from dataclasses import dataclass, field
from typing import Optional

from .abstract_implementation_data_type_subtypes_enum import (
    AbstractImplementationDataTypeSubtypesEnum,
)
from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
)
from .application_assoc_map_element_value_specification import (
    ApplicationAssocMapValueSpecification,
    ArrayValueSpecification,
    CompositeRuleBasedValueSpecification,
    RecordValueSpecification,
)
from .application_rule_based_value_specification import (
    ApplicationRuleBasedValueSpecification,
)
from .application_value_specification import ApplicationValueSpecification
from .category_string import CategoryString
from .constant_reference import ConstantReference
from .identifier import Identifier
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .not_available_value_specification import NotAvailableValueSpecification
from .numerical_rule_based_value_specification import (
    NumericalRuleBasedValueSpecification,
)
from .numerical_value_specification import NumericalValueSpecification
from .persistency_element_level_update_strategy_enum import (
    PersistencyElementLevelUpdateStrategyEnum,
)
from .ref import Ref
from .reference_value_specification import ReferenceValueSpecification
from .short_name_fragment import ShortNameFragment
from .text_value_specification import TextValueSpecification

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class PersistencyKeyValuePair:
    """
    This meta-class represents the ability to formally model a key-value pair in
    the context of the deployment of persistency.

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
    :ivar update_strategy: This attribute can be used to specify the
        update strategy of the respective PersistencyDeploymentElement.
    :ivar init_value: This aggregation represents the ability to define
        an initial value for the value side of the key-value pair.
        Please note that it does not make sense to configure an initial
        value if the PersistencyDeploymentElement.updateStrategy is set
        to the value delete.
    :ivar value_data_type_ref: This reference represents the data type
        applicable for the value of the key-value pair.
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
        name = "PERSISTENCY-KEY-VALUE-PAIR"

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
        "PersistencyKeyValuePair.ShortNameFragments"
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
    annotations: Optional["PersistencyKeyValuePair.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    update_strategy: Optional[PersistencyElementLevelUpdateStrategyEnum] = (
        field(
            default=None,
            metadata={
                "name": "UPDATE-STRATEGY",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    init_value: Optional["PersistencyKeyValuePair.InitValue"] = field(
        default=None,
        metadata={
            "name": "INIT-VALUE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    value_data_type_ref: Optional[
        "PersistencyKeyValuePair.ValueDataTypeRef"
    ] = field(
        default=None,
        metadata={
            "name": "VALUE-DATA-TYPE-REF",
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
    class InitValue:
        application_assoc_map_value_specification: Optional[
            ApplicationAssocMapValueSpecification
        ] = field(
            default=None,
            metadata={
                "name": "APPLICATION-ASSOC-MAP-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        application_rule_based_value_specification: Optional[
            ApplicationRuleBasedValueSpecification
        ] = field(
            default=None,
            metadata={
                "name": "APPLICATION-RULE-BASED-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        application_value_specification: Optional[
            ApplicationValueSpecification
        ] = field(
            default=None,
            metadata={
                "name": "APPLICATION-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        array_value_specification: Optional[ArrayValueSpecification] = field(
            default=None,
            metadata={
                "name": "ARRAY-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        composite_rule_based_value_specification: Optional[
            CompositeRuleBasedValueSpecification
        ] = field(
            default=None,
            metadata={
                "name": "COMPOSITE-RULE-BASED-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        constant_reference: Optional[ConstantReference] = field(
            default=None,
            metadata={
                "name": "CONSTANT-REFERENCE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        not_available_value_specification: Optional[
            NotAvailableValueSpecification
        ] = field(
            default=None,
            metadata={
                "name": "NOT-AVAILABLE-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        numerical_rule_based_value_specification: Optional[
            NumericalRuleBasedValueSpecification
        ] = field(
            default=None,
            metadata={
                "name": "NUMERICAL-RULE-BASED-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        numerical_value_specification: Optional[
            NumericalValueSpecification
        ] = field(
            default=None,
            metadata={
                "name": "NUMERICAL-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        record_value_specification: Optional[RecordValueSpecification] = field(
            default=None,
            metadata={
                "name": "RECORD-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        reference_value_specification: Optional[
            ReferenceValueSpecification
        ] = field(
            default=None,
            metadata={
                "name": "REFERENCE-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        text_value_specification: Optional[TextValueSpecification] = field(
            default=None,
            metadata={
                "name": "TEXT-VALUE-SPECIFICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class ValueDataTypeRef(Ref):
        dest: Optional[AbstractImplementationDataTypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
