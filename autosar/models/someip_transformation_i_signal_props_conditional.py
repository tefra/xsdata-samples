from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import VariationPoint
from .boolean import Boolean
from .cs_transformer_error_reaction_enum import CsTransformerErrorReactionEnum
from .data_prototype_transformation_props import (
    DataPrototypeTransformationProps,
)
from .positive_integer import PositiveInteger
from .ref import Ref
from .someip_message_type_enum import SomeipMessageTypeEnum
from .someip_transformer_session_handling_enum import (
    SomeipTransformerSessionHandlingEnum,
)
from .tlv_data_id_definition import TlvDataIdDefinition
from .tlv_data_id_definition_set_subtypes_enum import (
    TlvDataIdDefinitionSetSubtypesEnum,
)
from .transformation_technology_subtypes_enum import (
    TransformationTechnologySubtypesEnum,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SomeipTransformationISignalPropsConditional:
    """
    This element was generated/modified due to an atpVariation stereotype.

    :ivar cs_error_reaction: Defines whether the transformer chain of
        client/server communication coordinates an autonomous error
        reaction together with the RTE or whether any error reaction is
        the responsibility of the application.
    :ivar data_prototype_transformation_propss: Fine granular modeling
        of TransfromationProps on the level of DataPrototypes.
    :ivar transformer_ref: Reference to the TransformationTechnology
        description that contains transformer specific and ISignal
        independent configuration properties.
    :ivar implements_legacy_string_serialization: This attribute
        indicates that Strings in the SOME/IP message shall NOT be
        serialized according to the SOME/IP specification for Strings.
        If this attribute is set to true, BOM and null-termination shall
        NOT be added in the serialization for Strings in the payload. If
        this attribute is set to false (or not set) BOM and null-
        termination shall be added in the serialization for Strings in
        the payload according to the SOME/IP specification for Strings.
        NOTE! This attribute is not future safe, and will be removed in
        an upcoming AUTOSAR release!"
    :ivar implements_someip_string_handling: This attribute indicates
        whether Strings in the SOME/IP message shall be processed
        according to the SOME/IP specification for Strings. This
        attribute has been introduced due to compatibility reasons for
        AUTOSAR before R4.3. If this attribute is set to true Strings in
        the payload shall be handled according to the SOME/IP
        specification on Strings. If this attribute is set to false (or
        not set) no special handling for Strings in the payload shall be
        performed.
    :ivar interface_version: The interface version the SOME/IP
        transformer shall use.
    :ivar is_dynamic_length_field_size: This attribute shall be used to
        determine the wire type in the context of using the TLV
        encoding.
    :ivar message_type: The Message Type which shall be placed into the
        SOME/IP header.
    :ivar session_handling_sr: Defines whether the SOME/IP transformer
        shall use session handling for Sender/Receiver communication.
    :ivar size_of_array_length_fields: The size of all length fields (in
        Bytes) of fixed-size arrays or dynamic size arrays in the
        SOME/IP message. This attribute is valid for all available
        occurrences of fixed-size arrays or dynamic size arrays in the
        SOME/IP message.
    :ivar size_of_string_length_fields: The size of all length fields
        (in Bytes) of dynamic length strings in the SOME/IP message.
        This attribute is valid for all available occurrences of strings
        in the SOME/IP message.
    :ivar size_of_struct_length_fields: The size of all length fields
        (in Bytes) of structs in the SOME/IP message. This attribute is
        valid for all available occurrences of structures in the SOME/IP
        message. For a more fine granular modeling on the level of
        DataPrototypes the DataPrototypeTransformationProps shall be
        used.
    :ivar size_of_union_length_fields: The size of all length fields (in
        Bytes) of unions in the SOME/IP message. This attribute is valid
        for all available occurrences of Unions in the SOME/IP message.
        For a more fine granular modeling on the level of DataPrototypes
        the DataPrototypeTransformationProps shall be used.
    :ivar tlv_data_ids: This aggregation represents the collection of
        tlvDataIds defined in the enclosing context.
    :ivar tlv_data_id_0_refs: This reference identifies the
        TlvDataIdDefinitions relevant for the enclosing
        SOMEIPTransformationISignalProps.
    :ivar tlv_data_id_definition_refs: This reference identifies the
        TlvDataIdDefinitions relevant for the enclosing
        SOMEIPTransformationISignalProps
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
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
        name = "SOMEIP-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL"

    cs_error_reaction: None | CsTransformerErrorReactionEnum = field(
        default=None,
        metadata={
            "name": "CS-ERROR-REACTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    data_prototype_transformation_propss: (
        None
        | SomeipTransformationISignalPropsConditional.DataPrototypeTransformationPropss
    ) = field(
        default=None,
        metadata={
            "name": "DATA-PROTOTYPE-TRANSFORMATION-PROPSS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    transformer_ref: (
        None | SomeipTransformationISignalPropsConditional.TransformerRef
    ) = field(
        default=None,
        metadata={
            "name": "TRANSFORMER-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    implements_legacy_string_serialization: None | Boolean = field(
        default=None,
        metadata={
            "name": "IMPLEMENTS-LEGACY-STRING-SERIALIZATION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    implements_someip_string_handling: None | Boolean = field(
        default=None,
        metadata={
            "name": "IMPLEMENTS-SOMEIP-STRING-HANDLING",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    interface_version: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "INTERFACE-VERSION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    is_dynamic_length_field_size: None | Boolean = field(
        default=None,
        metadata={
            "name": "IS-DYNAMIC-LENGTH-FIELD-SIZE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    message_type: None | SomeipMessageTypeEnum = field(
        default=None,
        metadata={
            "name": "MESSAGE-TYPE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    session_handling_sr: None | SomeipTransformerSessionHandlingEnum = field(
        default=None,
        metadata={
            "name": "SESSION-HANDLING-SR",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    size_of_array_length_fields: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "SIZE-OF-ARRAY-LENGTH-FIELDS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    size_of_string_length_fields: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "SIZE-OF-STRING-LENGTH-FIELDS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    size_of_struct_length_fields: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "SIZE-OF-STRUCT-LENGTH-FIELDS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    size_of_union_length_fields: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "SIZE-OF-UNION-LENGTH-FIELDS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tlv_data_ids: (
        None | SomeipTransformationISignalPropsConditional.TlvDataIds
    ) = field(
        default=None,
        metadata={
            "name": "TLV-DATA-IDS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tlv_data_id_0_refs: (
        None | SomeipTransformationISignalPropsConditional.TlvDataId0Refs
    ) = field(
        default=None,
        metadata={
            "name": "TLV-DATA-ID-0-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tlv_data_id_definition_refs: (
        None
        | SomeipTransformationISignalPropsConditional.TlvDataIdDefinitionRefs
    ) = field(
        default=None,
        metadata={
            "name": "TLV-DATA-ID-DEFINITION-REFS",
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

    @dataclass
    class DataPrototypeTransformationPropss:
        data_prototype_transformation_props: list[
            DataPrototypeTransformationProps
        ] = field(
            default_factory=list,
            metadata={
                "name": "DATA-PROTOTYPE-TRANSFORMATION-PROPS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class TransformerRef(Ref):
        dest: None | TransformationTechnologySubtypesEnum = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class TlvDataIds:
        tlv_data_id_definition: list[TlvDataIdDefinition] = field(
            default_factory=list,
            metadata={
                "name": "TLV-DATA-ID-DEFINITION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class TlvDataId0Refs:
        tlv_data_id_0_ref: list[
            SomeipTransformationISignalPropsConditional.TlvDataId0Refs.TlvDataId0Ref
        ] = field(
            default_factory=list,
            metadata={
                "name": "TLV-DATA-ID-0-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class TlvDataId0Ref(Ref):
            dest: None | TlvDataIdDefinitionSetSubtypesEnum = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class TlvDataIdDefinitionRefs:
        tlv_data_id_definition_ref: list[
            SomeipTransformationISignalPropsConditional.TlvDataIdDefinitionRefs.TlvDataIdDefinitionRef
        ] = field(
            default_factory=list,
            metadata={
                "name": "TLV-DATA-ID-DEFINITION-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class TlvDataIdDefinitionRef(Ref):
            dest: None | TlvDataIdDefinitionSetSubtypesEnum = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )
