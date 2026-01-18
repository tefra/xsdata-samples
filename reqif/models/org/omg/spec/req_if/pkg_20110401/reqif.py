from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

from reqif.models.org.w3.xml.pkg_1998.namespace import LangValue
from reqif.models.xtml import (
    XhtmlDivType,
    XhtmlPType,
)

__NAMESPACE__ = "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"


@dataclass
class AlternativeId:
    class Meta:
        name = "ALTERNATIVE-ID"

    identifier: None | str = field(
        default=None,
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class AttributeValueBoolean:
    class Meta:
        name = "ATTRIBUTE-VALUE-BOOLEAN"

    definition: None | AttributeValueBoolean.Definition = field(
        default=None,
        metadata={
            "name": "DEFINITION",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        },
    )
    the_value: None | bool = field(
        default=None,
        metadata={
            "name": "THE-VALUE",
            "type": "Attribute",
            "required": True,
        },
    )

    @dataclass
    class Definition:
        attribute_definition_boolean_ref: None | str = field(
            default=None,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-BOOLEAN-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                "required": True,
            },
        )


@dataclass
class AttributeValueDate:
    class Meta:
        name = "ATTRIBUTE-VALUE-DATE"

    definition: None | AttributeValueDate.Definition = field(
        default=None,
        metadata={
            "name": "DEFINITION",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        },
    )
    the_value: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "THE-VALUE",
            "type": "Attribute",
            "required": True,
        },
    )

    @dataclass
    class Definition:
        attribute_definition_date_ref: None | str = field(
            default=None,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-DATE-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                "required": True,
            },
        )


@dataclass
class AttributeValueEnumeration:
    class Meta:
        name = "ATTRIBUTE-VALUE-ENUMERATION"

    definition: None | AttributeValueEnumeration.Definition = field(
        default=None,
        metadata={
            "name": "DEFINITION",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        },
    )
    values: None | AttributeValueEnumeration.Values = field(
        default=None,
        metadata={
            "name": "VALUES",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        },
    )

    @dataclass
    class Definition:
        attribute_definition_enumeration_ref: None | str = field(
            default=None,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-ENUMERATION-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                "required": True,
            },
        )

    @dataclass
    class Values:
        enum_value_ref: list[str] = field(
            default_factory=list,
            metadata={
                "name": "ENUM-VALUE-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )


@dataclass
class AttributeValueInteger:
    class Meta:
        name = "ATTRIBUTE-VALUE-INTEGER"

    definition: None | AttributeValueInteger.Definition = field(
        default=None,
        metadata={
            "name": "DEFINITION",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        },
    )
    the_value: None | int = field(
        default=None,
        metadata={
            "name": "THE-VALUE",
            "type": "Attribute",
            "required": True,
        },
    )

    @dataclass
    class Definition:
        attribute_definition_integer_ref: None | str = field(
            default=None,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-INTEGER-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                "required": True,
            },
        )


@dataclass
class AttributeValueReal:
    class Meta:
        name = "ATTRIBUTE-VALUE-REAL"

    definition: None | AttributeValueReal.Definition = field(
        default=None,
        metadata={
            "name": "DEFINITION",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        },
    )
    the_value: None | float = field(
        default=None,
        metadata={
            "name": "THE-VALUE",
            "type": "Attribute",
            "required": True,
        },
    )

    @dataclass
    class Definition:
        attribute_definition_real_ref: None | str = field(
            default=None,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-REAL-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                "required": True,
            },
        )


@dataclass
class AttributeValueString:
    class Meta:
        name = "ATTRIBUTE-VALUE-STRING"

    definition: None | AttributeValueString.Definition = field(
        default=None,
        metadata={
            "name": "DEFINITION",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        },
    )
    the_value: None | str = field(
        default=None,
        metadata={
            "name": "THE-VALUE",
            "type": "Attribute",
            "required": True,
        },
    )

    @dataclass
    class Definition:
        attribute_definition_string_ref: None | str = field(
            default=None,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-STRING-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                "required": True,
            },
        )


@dataclass
class EmbeddedValue:
    class Meta:
        name = "EMBEDDED-VALUE"

    key: None | int = field(
        default=None,
        metadata={
            "name": "KEY",
            "type": "Attribute",
            "required": True,
        },
    )
    other_content: None | str = field(
        default=None,
        metadata={
            "name": "OTHER-CONTENT",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ReqIfHeader:
    class Meta:
        name = "REQ-IF-HEADER"

    comment: None | str = field(
        default=None,
        metadata={
            "name": "COMMENT",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        },
    )
    creation_time: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "CREATION-TIME",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        },
    )
    repository_id: None | str = field(
        default=None,
        metadata={
            "name": "REPOSITORY-ID",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        },
    )
    req_if_tool_id: None | str = field(
        default=None,
        metadata={
            "name": "REQ-IF-TOOL-ID",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        },
    )
    req_if_version: str = field(
        init=False,
        default="1.0",
        metadata={
            "name": "REQ-IF-VERSION",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        },
    )
    source_tool_id: None | str = field(
        default=None,
        metadata={
            "name": "SOURCE-TOOL-ID",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "name": "TITLE",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        },
    )
    identifier: None | str = field(
        default=None,
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ReqIfToolExtension:
    class Meta:
        name = "REQ-IF-TOOL-EXTENSION"

    other_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )


@dataclass
class AttributeDefinitionBoolean:
    class Meta:
        name = "ATTRIBUTE-DEFINITION-BOOLEAN"

    alternative_id: None | AttributeDefinitionBoolean.AlternativeId = field(
        default=None,
        metadata={
            "name": "ALTERNATIVE-ID",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        },
    )
    default_value: None | AttributeDefinitionBoolean.DefaultValue = field(
        default=None,
        metadata={
            "name": "DEFAULT-VALUE",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        },
    )
    type_value: None | AttributeDefinitionBoolean.Type = field(
        default=None,
        metadata={
            "name": "TYPE",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        },
    )
    desc: None | str = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        },
    )
    identifier: None | str = field(
        default=None,
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        },
    )
    is_editable: None | bool = field(
        default=None,
        metadata={
            "name": "IS-EDITABLE",
            "type": "Attribute",
        },
    )
    last_change: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        },
    )
    long_name: None | str = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        },
    )

    @dataclass
    class AlternativeId:
        alternative_id: None | AlternativeId = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass
    class DefaultValue:
        attribute_value_boolean: None | AttributeValueBoolean = field(
            default=None,
            metadata={
                "name": "ATTRIBUTE-VALUE-BOOLEAN",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass
    class Type:
        datatype_definition_boolean_ref: None | str = field(
            default=None,
            metadata={
                "name": "DATATYPE-DEFINITION-BOOLEAN-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                "required": True,
            },
        )


@dataclass
class AttributeDefinitionDate:
    class Meta:
        name = "ATTRIBUTE-DEFINITION-DATE"

    alternative_id: None | AttributeDefinitionDate.AlternativeId = field(
        default=None,
        metadata={
            "name": "ALTERNATIVE-ID",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        },
    )
    default_value: None | AttributeDefinitionDate.DefaultValue = field(
        default=None,
        metadata={
            "name": "DEFAULT-VALUE",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        },
    )
    type_value: None | AttributeDefinitionDate.Type = field(
        default=None,
        metadata={
            "name": "TYPE",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        },
    )
    desc: None | str = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        },
    )
    identifier: None | str = field(
        default=None,
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        },
    )
    is_editable: None | bool = field(
        default=None,
        metadata={
            "name": "IS-EDITABLE",
            "type": "Attribute",
        },
    )
    last_change: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        },
    )
    long_name: None | str = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        },
    )

    @dataclass
    class AlternativeId:
        alternative_id: None | AlternativeId = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass
    class DefaultValue:
        attribute_value_date: None | AttributeValueDate = field(
            default=None,
            metadata={
                "name": "ATTRIBUTE-VALUE-DATE",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass
    class Type:
        datatype_definition_date_ref: None | str = field(
            default=None,
            metadata={
                "name": "DATATYPE-DEFINITION-DATE-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                "required": True,
            },
        )


@dataclass
class AttributeDefinitionEnumeration:
    class Meta:
        name = "ATTRIBUTE-DEFINITION-ENUMERATION"

    default_value: None | AttributeDefinitionEnumeration.DefaultValue = field(
        default=None,
        metadata={
            "name": "DEFAULT-VALUE",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        },
    )
    alternative_id: None | AttributeDefinitionEnumeration.AlternativeId = (
        field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )
    )
    type_value: None | AttributeDefinitionEnumeration.Type = field(
        default=None,
        metadata={
            "name": "TYPE",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        },
    )
    desc: None | str = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        },
    )
    identifier: None | str = field(
        default=None,
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        },
    )
    is_editable: None | bool = field(
        default=None,
        metadata={
            "name": "IS-EDITABLE",
            "type": "Attribute",
        },
    )
    last_change: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        },
    )
    long_name: None | str = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        },
    )
    multi_valued: None | bool = field(
        default=None,
        metadata={
            "name": "MULTI-VALUED",
            "type": "Attribute",
            "required": True,
        },
    )

    @dataclass
    class DefaultValue:
        attribute_value_enumeration: None | AttributeValueEnumeration = field(
            default=None,
            metadata={
                "name": "ATTRIBUTE-VALUE-ENUMERATION",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass
    class AlternativeId:
        alternative_id: None | AlternativeId = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass
    class Type:
        datatype_definition_enumeration_ref: None | str = field(
            default=None,
            metadata={
                "name": "DATATYPE-DEFINITION-ENUMERATION-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                "required": True,
            },
        )


@dataclass
class AttributeDefinitionInteger:
    class Meta:
        name = "ATTRIBUTE-DEFINITION-INTEGER"

    alternative_id: None | AttributeDefinitionInteger.AlternativeId = field(
        default=None,
        metadata={
            "name": "ALTERNATIVE-ID",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        },
    )
    default_value: None | AttributeDefinitionInteger.DefaultValue = field(
        default=None,
        metadata={
            "name": "DEFAULT-VALUE",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        },
    )
    type_value: None | AttributeDefinitionInteger.Type = field(
        default=None,
        metadata={
            "name": "TYPE",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        },
    )
    desc: None | str = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        },
    )
    identifier: None | str = field(
        default=None,
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        },
    )
    is_editable: None | bool = field(
        default=None,
        metadata={
            "name": "IS-EDITABLE",
            "type": "Attribute",
        },
    )
    last_change: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        },
    )
    long_name: None | str = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        },
    )

    @dataclass
    class AlternativeId:
        alternative_id: None | AlternativeId = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass
    class DefaultValue:
        attribute_value_integer: None | AttributeValueInteger = field(
            default=None,
            metadata={
                "name": "ATTRIBUTE-VALUE-INTEGER",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass
    class Type:
        datatype_definition_integer_ref: None | str = field(
            default=None,
            metadata={
                "name": "DATATYPE-DEFINITION-INTEGER-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                "required": True,
            },
        )


@dataclass
class AttributeDefinitionReal:
    class Meta:
        name = "ATTRIBUTE-DEFINITION-REAL"

    alternative_id: None | AttributeDefinitionReal.AlternativeId = field(
        default=None,
        metadata={
            "name": "ALTERNATIVE-ID",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        },
    )
    default_value: None | AttributeDefinitionReal.DefaultValue = field(
        default=None,
        metadata={
            "name": "DEFAULT-VALUE",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        },
    )
    type_value: None | AttributeDefinitionReal.Type = field(
        default=None,
        metadata={
            "name": "TYPE",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        },
    )
    desc: None | str = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        },
    )
    identifier: None | str = field(
        default=None,
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        },
    )
    is_editable: None | bool = field(
        default=None,
        metadata={
            "name": "IS-EDITABLE",
            "type": "Attribute",
        },
    )
    last_change: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        },
    )
    long_name: None | str = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        },
    )

    @dataclass
    class AlternativeId:
        alternative_id: None | AlternativeId = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass
    class DefaultValue:
        attribute_value_real: None | AttributeValueReal = field(
            default=None,
            metadata={
                "name": "ATTRIBUTE-VALUE-REAL",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass
    class Type:
        datatype_definition_real_ref: None | str = field(
            default=None,
            metadata={
                "name": "DATATYPE-DEFINITION-REAL-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                "required": True,
            },
        )


@dataclass
class AttributeDefinitionString:
    class Meta:
        name = "ATTRIBUTE-DEFINITION-STRING"

    alternative_id: None | AttributeDefinitionString.AlternativeId = field(
        default=None,
        metadata={
            "name": "ALTERNATIVE-ID",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        },
    )
    default_value: None | AttributeDefinitionString.DefaultValue = field(
        default=None,
        metadata={
            "name": "DEFAULT-VALUE",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        },
    )
    type_value: None | AttributeDefinitionString.Type = field(
        default=None,
        metadata={
            "name": "TYPE",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        },
    )
    desc: None | str = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        },
    )
    identifier: None | str = field(
        default=None,
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        },
    )
    is_editable: None | bool = field(
        default=None,
        metadata={
            "name": "IS-EDITABLE",
            "type": "Attribute",
        },
    )
    last_change: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        },
    )
    long_name: None | str = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        },
    )

    @dataclass
    class AlternativeId:
        alternative_id: None | AlternativeId = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass
    class DefaultValue:
        attribute_value_string: None | AttributeValueString = field(
            default=None,
            metadata={
                "name": "ATTRIBUTE-VALUE-STRING",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass
    class Type:
        datatype_definition_string_ref: None | str = field(
            default=None,
            metadata={
                "name": "DATATYPE-DEFINITION-STRING-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                "required": True,
            },
        )


@dataclass
class DatatypeDefinitionBoolean:
    class Meta:
        name = "DATATYPE-DEFINITION-BOOLEAN"

    alternative_id: None | DatatypeDefinitionBoolean.AlternativeId = field(
        default=None,
        metadata={
            "name": "ALTERNATIVE-ID",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        },
    )
    desc: None | str = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        },
    )
    identifier: None | str = field(
        default=None,
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        },
    )
    last_change: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        },
    )
    long_name: None | str = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        },
    )

    @dataclass
    class AlternativeId:
        alternative_id: None | AlternativeId = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )


@dataclass
class DatatypeDefinitionDate:
    class Meta:
        name = "DATATYPE-DEFINITION-DATE"

    alternative_id: None | DatatypeDefinitionDate.AlternativeId = field(
        default=None,
        metadata={
            "name": "ALTERNATIVE-ID",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        },
    )
    desc: None | str = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        },
    )
    identifier: None | str = field(
        default=None,
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        },
    )
    last_change: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        },
    )
    long_name: None | str = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        },
    )

    @dataclass
    class AlternativeId:
        alternative_id: None | AlternativeId = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )


@dataclass
class DatatypeDefinitionInteger:
    class Meta:
        name = "DATATYPE-DEFINITION-INTEGER"

    alternative_id: None | DatatypeDefinitionInteger.AlternativeId = field(
        default=None,
        metadata={
            "name": "ALTERNATIVE-ID",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        },
    )
    desc: None | str = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        },
    )
    identifier: None | str = field(
        default=None,
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        },
    )
    last_change: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        },
    )
    long_name: None | str = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        },
    )
    max: None | int = field(
        default=None,
        metadata={
            "name": "MAX",
            "type": "Attribute",
            "required": True,
        },
    )
    min: None | int = field(
        default=None,
        metadata={
            "name": "MIN",
            "type": "Attribute",
            "required": True,
        },
    )

    @dataclass
    class AlternativeId:
        alternative_id: None | AlternativeId = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )


@dataclass
class DatatypeDefinitionReal:
    class Meta:
        name = "DATATYPE-DEFINITION-REAL"

    alternative_id: None | DatatypeDefinitionReal.AlternativeId = field(
        default=None,
        metadata={
            "name": "ALTERNATIVE-ID",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        },
    )
    accuracy: None | int = field(
        default=None,
        metadata={
            "name": "ACCURACY",
            "type": "Attribute",
            "required": True,
        },
    )
    desc: None | str = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        },
    )
    identifier: None | str = field(
        default=None,
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        },
    )
    last_change: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        },
    )
    long_name: None | str = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        },
    )
    max: None | float = field(
        default=None,
        metadata={
            "name": "MAX",
            "type": "Attribute",
            "required": True,
        },
    )
    min: None | float = field(
        default=None,
        metadata={
            "name": "MIN",
            "type": "Attribute",
            "required": True,
        },
    )

    @dataclass
    class AlternativeId:
        alternative_id: None | AlternativeId = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )


@dataclass
class DatatypeDefinitionString:
    class Meta:
        name = "DATATYPE-DEFINITION-STRING"

    alternative_id: None | DatatypeDefinitionString.AlternativeId = field(
        default=None,
        metadata={
            "name": "ALTERNATIVE-ID",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        },
    )
    desc: None | str = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        },
    )
    identifier: None | str = field(
        default=None,
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        },
    )
    last_change: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        },
    )
    long_name: None | str = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        },
    )
    max_length: None | int = field(
        default=None,
        metadata={
            "name": "MAX-LENGTH",
            "type": "Attribute",
            "required": True,
        },
    )

    @dataclass
    class AlternativeId:
        alternative_id: None | AlternativeId = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )


@dataclass
class DatatypeDefinitionXhtml:
    class Meta:
        name = "DATATYPE-DEFINITION-XHTML"

    alternative_id: None | DatatypeDefinitionXhtml.AlternativeId = field(
        default=None,
        metadata={
            "name": "ALTERNATIVE-ID",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        },
    )
    desc: None | str = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        },
    )
    identifier: None | str = field(
        default=None,
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        },
    )
    last_change: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        },
    )
    long_name: None | str = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        },
    )

    @dataclass
    class AlternativeId:
        alternative_id: None | AlternativeId = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )


@dataclass
class EnumValue:
    class Meta:
        name = "ENUM-VALUE"

    alternative_id: None | EnumValue.AlternativeId = field(
        default=None,
        metadata={
            "name": "ALTERNATIVE-ID",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        },
    )
    properties: None | EnumValue.Properties = field(
        default=None,
        metadata={
            "name": "PROPERTIES",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        },
    )
    desc: None | str = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        },
    )
    identifier: None | str = field(
        default=None,
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        },
    )
    last_change: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        },
    )
    long_name: None | str = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        },
    )

    @dataclass
    class AlternativeId:
        alternative_id: None | AlternativeId = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass
    class Properties:
        embedded_value: None | EmbeddedValue = field(
            default=None,
            metadata={
                "name": "EMBEDDED-VALUE",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                "required": True,
            },
        )


@dataclass
class RelationGroup:
    class Meta:
        name = "RELATION-GROUP"

    alternative_id: None | RelationGroup.AlternativeId = field(
        default=None,
        metadata={
            "name": "ALTERNATIVE-ID",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        },
    )
    source_specification: None | RelationGroup.SourceSpecification = field(
        default=None,
        metadata={
            "name": "SOURCE-SPECIFICATION",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        },
    )
    spec_relations: None | RelationGroup.SpecRelations = field(
        default=None,
        metadata={
            "name": "SPEC-RELATIONS",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        },
    )
    target_specification: None | RelationGroup.TargetSpecification = field(
        default=None,
        metadata={
            "name": "TARGET-SPECIFICATION",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        },
    )
    type_value: None | RelationGroup.Type = field(
        default=None,
        metadata={
            "name": "TYPE",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        },
    )
    desc: None | str = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        },
    )
    identifier: None | str = field(
        default=None,
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        },
    )
    last_change: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        },
    )
    long_name: None | str = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        },
    )

    @dataclass
    class AlternativeId:
        alternative_id: None | AlternativeId = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass
    class SourceSpecification:
        specification_ref: None | str = field(
            default=None,
            metadata={
                "name": "SPECIFICATION-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                "required": True,
            },
        )

    @dataclass
    class SpecRelations:
        spec_relation_ref: list[str] = field(
            default_factory=list,
            metadata={
                "name": "SPEC-RELATION-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass
    class TargetSpecification:
        specification_ref: None | str = field(
            default=None,
            metadata={
                "name": "SPECIFICATION-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                "required": True,
            },
        )

    @dataclass
    class Type:
        relation_group_type_ref: None | str = field(
            default=None,
            metadata={
                "name": "RELATION-GROUP-TYPE-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                "required": True,
            },
        )


@dataclass
class SpecHierarchy:
    class Meta:
        name = "SPEC-HIERARCHY"

    alternative_id: None | SpecHierarchy.AlternativeId = field(
        default=None,
        metadata={
            "name": "ALTERNATIVE-ID",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        },
    )
    children: None | SpecHierarchy.Children = field(
        default=None,
        metadata={
            "name": "CHILDREN",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        },
    )
    editable_atts: None | SpecHierarchy.EditableAtts = field(
        default=None,
        metadata={
            "name": "EDITABLE-ATTS",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        },
    )
    object_value: None | SpecHierarchy.Object = field(
        default=None,
        metadata={
            "name": "OBJECT",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        },
    )
    desc: None | str = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        },
    )
    identifier: None | str = field(
        default=None,
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        },
    )
    is_editable: None | bool = field(
        default=None,
        metadata={
            "name": "IS-EDITABLE",
            "type": "Attribute",
        },
    )
    is_table_internal: None | bool = field(
        default=None,
        metadata={
            "name": "IS-TABLE-INTERNAL",
            "type": "Attribute",
        },
    )
    last_change: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        },
    )
    long_name: None | str = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        },
    )

    @dataclass
    class AlternativeId:
        alternative_id: None | AlternativeId = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass
    class Children:
        spec_hierarchy: list[SpecHierarchy] = field(
            default_factory=list,
            metadata={
                "name": "SPEC-HIERARCHY",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass
    class EditableAtts:
        attribute_definition_boolean_ref: list[str] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-BOOLEAN-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )
        attribute_definition_date_ref: list[str] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-DATE-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )
        attribute_definition_enumeration_ref: list[str] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-ENUMERATION-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )
        attribute_definition_integer_ref: list[str] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-INTEGER-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )
        attribute_definition_real_ref: list[str] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-REAL-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )
        attribute_definition_string_ref: list[str] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-STRING-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )
        attribute_definition_xhtml_ref: list[str] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-XHTML-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass
    class Object:
        spec_object_ref: None | str = field(
            default=None,
            metadata={
                "name": "SPEC-OBJECT-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                "required": True,
            },
        )


@dataclass
class XhtmlContent:
    class Meta:
        name = "XHTML-CONTENT"

    p: None | XhtmlPType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )
    div: None | XhtmlDivType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        },
    )


@dataclass
class AttributeValueXhtml:
    class Meta:
        name = "ATTRIBUTE-VALUE-XHTML"

    the_value: None | XhtmlContent = field(
        default=None,
        metadata={
            "name": "THE-VALUE",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        },
    )
    the_original_value: None | XhtmlContent = field(
        default=None,
        metadata={
            "name": "THE-ORIGINAL-VALUE",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        },
    )
    definition: None | AttributeValueXhtml.Definition = field(
        default=None,
        metadata={
            "name": "DEFINITION",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        },
    )
    is_simplified: None | bool = field(
        default=None,
        metadata={
            "name": "IS-SIMPLIFIED",
            "type": "Attribute",
        },
    )

    @dataclass
    class Definition:
        attribute_definition_xhtml_ref: None | str = field(
            default=None,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-XHTML-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                "required": True,
            },
        )


@dataclass
class DatatypeDefinitionEnumeration:
    class Meta:
        name = "DATATYPE-DEFINITION-ENUMERATION"

    alternative_id: None | DatatypeDefinitionEnumeration.AlternativeId = field(
        default=None,
        metadata={
            "name": "ALTERNATIVE-ID",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        },
    )
    specified_values: None | DatatypeDefinitionEnumeration.SpecifiedValues = (
        field(
            default=None,
            metadata={
                "name": "SPECIFIED-VALUES",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )
    )
    desc: None | str = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        },
    )
    identifier: None | str = field(
        default=None,
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        },
    )
    last_change: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        },
    )
    long_name: None | str = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        },
    )

    @dataclass
    class AlternativeId:
        alternative_id: None | AlternativeId = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass
    class SpecifiedValues:
        enum_value: list[EnumValue] = field(
            default_factory=list,
            metadata={
                "name": "ENUM-VALUE",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )


@dataclass
class AttributeDefinitionXhtml:
    class Meta:
        name = "ATTRIBUTE-DEFINITION-XHTML"

    alternative_id: None | AttributeDefinitionXhtml.AlternativeId = field(
        default=None,
        metadata={
            "name": "ALTERNATIVE-ID",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        },
    )
    default_value: None | AttributeDefinitionXhtml.DefaultValue = field(
        default=None,
        metadata={
            "name": "DEFAULT-VALUE",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        },
    )
    type_value: None | AttributeDefinitionXhtml.Type = field(
        default=None,
        metadata={
            "name": "TYPE",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        },
    )
    desc: None | str = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        },
    )
    identifier: None | str = field(
        default=None,
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        },
    )
    is_editable: None | bool = field(
        default=None,
        metadata={
            "name": "IS-EDITABLE",
            "type": "Attribute",
        },
    )
    last_change: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        },
    )
    long_name: None | str = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        },
    )

    @dataclass
    class AlternativeId:
        alternative_id: None | AlternativeId = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass
    class DefaultValue:
        attribute_value_xhtml: None | AttributeValueXhtml = field(
            default=None,
            metadata={
                "name": "ATTRIBUTE-VALUE-XHTML",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass
    class Type:
        datatype_definition_xhtml_ref: None | str = field(
            default=None,
            metadata={
                "name": "DATATYPE-DEFINITION-XHTML-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                "required": True,
            },
        )


@dataclass
class SpecObject:
    class Meta:
        name = "SPEC-OBJECT"

    alternative_id: None | SpecObject.AlternativeId = field(
        default=None,
        metadata={
            "name": "ALTERNATIVE-ID",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        },
    )
    values: None | SpecObject.Values = field(
        default=None,
        metadata={
            "name": "VALUES",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        },
    )
    type_value: None | SpecObject.Type = field(
        default=None,
        metadata={
            "name": "TYPE",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        },
    )
    desc: None | str = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        },
    )
    identifier: None | str = field(
        default=None,
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        },
    )
    last_change: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        },
    )
    long_name: None | str = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        },
    )

    @dataclass
    class AlternativeId:
        alternative_id: None | AlternativeId = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass
    class Values:
        attribute_value_boolean: list[AttributeValueBoolean] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-VALUE-BOOLEAN",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )
        attribute_value_date: list[AttributeValueDate] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-VALUE-DATE",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )
        attribute_value_enumeration: list[AttributeValueEnumeration] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-VALUE-ENUMERATION",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )
        attribute_value_integer: list[AttributeValueInteger] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-VALUE-INTEGER",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )
        attribute_value_real: list[AttributeValueReal] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-VALUE-REAL",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )
        attribute_value_string: list[AttributeValueString] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-VALUE-STRING",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )
        attribute_value_xhtml: list[AttributeValueXhtml] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-VALUE-XHTML",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass
    class Type:
        spec_object_type_ref: None | str = field(
            default=None,
            metadata={
                "name": "SPEC-OBJECT-TYPE-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                "required": True,
            },
        )


@dataclass
class SpecRelation:
    class Meta:
        name = "SPEC-RELATION"

    alternative_id: None | SpecRelation.AlternativeId = field(
        default=None,
        metadata={
            "name": "ALTERNATIVE-ID",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        },
    )
    values: None | SpecRelation.Values = field(
        default=None,
        metadata={
            "name": "VALUES",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        },
    )
    source: None | SpecRelation.Source = field(
        default=None,
        metadata={
            "name": "SOURCE",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        },
    )
    target: None | SpecRelation.Target = field(
        default=None,
        metadata={
            "name": "TARGET",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        },
    )
    type_value: None | SpecRelation.Type = field(
        default=None,
        metadata={
            "name": "TYPE",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        },
    )
    desc: None | str = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        },
    )
    identifier: None | str = field(
        default=None,
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        },
    )
    last_change: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        },
    )
    long_name: None | str = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        },
    )

    @dataclass
    class AlternativeId:
        alternative_id: None | AlternativeId = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass
    class Values:
        attribute_value_boolean: list[AttributeValueBoolean] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-VALUE-BOOLEAN",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )
        attribute_value_date: list[AttributeValueDate] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-VALUE-DATE",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )
        attribute_value_enumeration: list[AttributeValueEnumeration] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-VALUE-ENUMERATION",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )
        attribute_value_integer: list[AttributeValueInteger] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-VALUE-INTEGER",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )
        attribute_value_real: list[AttributeValueReal] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-VALUE-REAL",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )
        attribute_value_string: list[AttributeValueString] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-VALUE-STRING",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )
        attribute_value_xhtml: list[AttributeValueXhtml] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-VALUE-XHTML",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass
    class Source:
        spec_object_ref: None | str = field(
            default=None,
            metadata={
                "name": "SPEC-OBJECT-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                "required": True,
            },
        )

    @dataclass
    class Target:
        spec_object_ref: None | str = field(
            default=None,
            metadata={
                "name": "SPEC-OBJECT-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                "required": True,
            },
        )

    @dataclass
    class Type:
        spec_relation_type_ref: None | str = field(
            default=None,
            metadata={
                "name": "SPEC-RELATION-TYPE-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                "required": True,
            },
        )


@dataclass
class Specification:
    class Meta:
        name = "SPECIFICATION"

    alternative_id: None | Specification.AlternativeId = field(
        default=None,
        metadata={
            "name": "ALTERNATIVE-ID",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        },
    )
    values: None | Specification.Values = field(
        default=None,
        metadata={
            "name": "VALUES",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        },
    )
    children: None | Specification.Children = field(
        default=None,
        metadata={
            "name": "CHILDREN",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        },
    )
    type_value: None | Specification.Type = field(
        default=None,
        metadata={
            "name": "TYPE",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        },
    )
    desc: None | str = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        },
    )
    identifier: None | str = field(
        default=None,
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        },
    )
    last_change: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        },
    )
    long_name: None | str = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        },
    )

    @dataclass
    class AlternativeId:
        alternative_id: None | AlternativeId = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass
    class Values:
        attribute_value_boolean: list[AttributeValueBoolean] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-VALUE-BOOLEAN",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )
        attribute_value_date: list[AttributeValueDate] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-VALUE-DATE",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )
        attribute_value_enumeration: list[AttributeValueEnumeration] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-VALUE-ENUMERATION",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )
        attribute_value_integer: list[AttributeValueInteger] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-VALUE-INTEGER",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )
        attribute_value_real: list[AttributeValueReal] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-VALUE-REAL",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )
        attribute_value_string: list[AttributeValueString] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-VALUE-STRING",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )
        attribute_value_xhtml: list[AttributeValueXhtml] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-VALUE-XHTML",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass
    class Children:
        spec_hierarchy: list[SpecHierarchy] = field(
            default_factory=list,
            metadata={
                "name": "SPEC-HIERARCHY",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass
    class Type:
        specification_type_ref: None | str = field(
            default=None,
            metadata={
                "name": "SPECIFICATION-TYPE-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                "required": True,
            },
        )


@dataclass
class RelationGroupType:
    class Meta:
        name = "RELATION-GROUP-TYPE"

    alternative_id: None | RelationGroupType.AlternativeId = field(
        default=None,
        metadata={
            "name": "ALTERNATIVE-ID",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        },
    )
    spec_attributes: None | RelationGroupType.SpecAttributes = field(
        default=None,
        metadata={
            "name": "SPEC-ATTRIBUTES",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        },
    )
    desc: None | str = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        },
    )
    identifier: None | str = field(
        default=None,
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        },
    )
    last_change: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        },
    )
    long_name: None | str = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        },
    )

    @dataclass
    class AlternativeId:
        alternative_id: None | AlternativeId = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass
    class SpecAttributes:
        attribute_definition_boolean: list[AttributeDefinitionBoolean] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-BOOLEAN",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )
        attribute_definition_date: list[AttributeDefinitionDate] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-DATE",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )
        attribute_definition_enumeration: list[
            AttributeDefinitionEnumeration
        ] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-ENUMERATION",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )
        attribute_definition_integer: list[AttributeDefinitionInteger] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-INTEGER",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )
        attribute_definition_real: list[AttributeDefinitionReal] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-REAL",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )
        attribute_definition_string: list[AttributeDefinitionString] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-STRING",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )
        attribute_definition_xhtml: list[AttributeDefinitionXhtml] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-XHTML",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )


@dataclass
class SpecObjectType:
    class Meta:
        name = "SPEC-OBJECT-TYPE"

    alternative_id: None | SpecObjectType.AlternativeId = field(
        default=None,
        metadata={
            "name": "ALTERNATIVE-ID",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        },
    )
    spec_attributes: None | SpecObjectType.SpecAttributes = field(
        default=None,
        metadata={
            "name": "SPEC-ATTRIBUTES",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        },
    )
    desc: None | str = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        },
    )
    identifier: None | str = field(
        default=None,
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        },
    )
    last_change: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        },
    )
    long_name: None | str = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        },
    )

    @dataclass
    class AlternativeId:
        alternative_id: None | AlternativeId = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass
    class SpecAttributes:
        attribute_definition_boolean: list[AttributeDefinitionBoolean] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-BOOLEAN",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )
        attribute_definition_date: list[AttributeDefinitionDate] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-DATE",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )
        attribute_definition_enumeration: list[
            AttributeDefinitionEnumeration
        ] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-ENUMERATION",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )
        attribute_definition_integer: list[AttributeDefinitionInteger] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-INTEGER",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )
        attribute_definition_real: list[AttributeDefinitionReal] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-REAL",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )
        attribute_definition_string: list[AttributeDefinitionString] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-STRING",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )
        attribute_definition_xhtml: list[AttributeDefinitionXhtml] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-XHTML",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )


@dataclass
class SpecRelationType:
    class Meta:
        name = "SPEC-RELATION-TYPE"

    alternative_id: None | SpecRelationType.AlternativeId = field(
        default=None,
        metadata={
            "name": "ALTERNATIVE-ID",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        },
    )
    spec_attributes: None | SpecRelationType.SpecAttributes = field(
        default=None,
        metadata={
            "name": "SPEC-ATTRIBUTES",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        },
    )
    desc: None | str = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        },
    )
    identifier: None | str = field(
        default=None,
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        },
    )
    last_change: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        },
    )
    long_name: None | str = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        },
    )

    @dataclass
    class AlternativeId:
        alternative_id: None | AlternativeId = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass
    class SpecAttributes:
        attribute_definition_boolean: list[AttributeDefinitionBoolean] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-BOOLEAN",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )
        attribute_definition_date: list[AttributeDefinitionDate] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-DATE",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )
        attribute_definition_enumeration: list[
            AttributeDefinitionEnumeration
        ] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-ENUMERATION",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )
        attribute_definition_integer: list[AttributeDefinitionInteger] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-INTEGER",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )
        attribute_definition_real: list[AttributeDefinitionReal] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-REAL",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )
        attribute_definition_string: list[AttributeDefinitionString] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-STRING",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )
        attribute_definition_xhtml: list[AttributeDefinitionXhtml] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-XHTML",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )


@dataclass
class SpecificationType:
    class Meta:
        name = "SPECIFICATION-TYPE"

    alternative_id: None | SpecificationType.AlternativeId = field(
        default=None,
        metadata={
            "name": "ALTERNATIVE-ID",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        },
    )
    spec_attributes: None | SpecificationType.SpecAttributes = field(
        default=None,
        metadata={
            "name": "SPEC-ATTRIBUTES",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        },
    )
    desc: None | str = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        },
    )
    identifier: None | str = field(
        default=None,
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        },
    )
    last_change: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        },
    )
    long_name: None | str = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        },
    )

    @dataclass
    class AlternativeId:
        alternative_id: None | AlternativeId = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass
    class SpecAttributes:
        attribute_definition_boolean: list[AttributeDefinitionBoolean] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-BOOLEAN",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )
        attribute_definition_date: list[AttributeDefinitionDate] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-DATE",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )
        attribute_definition_enumeration: list[
            AttributeDefinitionEnumeration
        ] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-ENUMERATION",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )
        attribute_definition_integer: list[AttributeDefinitionInteger] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-INTEGER",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )
        attribute_definition_real: list[AttributeDefinitionReal] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-REAL",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )
        attribute_definition_string: list[AttributeDefinitionString] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-STRING",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )
        attribute_definition_xhtml: list[AttributeDefinitionXhtml] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-XHTML",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )


@dataclass
class ReqIfContent:
    class Meta:
        name = "REQ-IF-CONTENT"

    datatypes: None | ReqIfContent.Datatypes = field(
        default=None,
        metadata={
            "name": "DATATYPES",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        },
    )
    spec_types: None | ReqIfContent.SpecTypes = field(
        default=None,
        metadata={
            "name": "SPEC-TYPES",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        },
    )
    spec_objects: None | ReqIfContent.SpecObjects = field(
        default=None,
        metadata={
            "name": "SPEC-OBJECTS",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        },
    )
    spec_relations: None | ReqIfContent.SpecRelations = field(
        default=None,
        metadata={
            "name": "SPEC-RELATIONS",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        },
    )
    specifications: None | ReqIfContent.Specifications = field(
        default=None,
        metadata={
            "name": "SPECIFICATIONS",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        },
    )
    spec_relation_groups: None | ReqIfContent.SpecRelationGroups = field(
        default=None,
        metadata={
            "name": "SPEC-RELATION-GROUPS",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        },
    )

    @dataclass
    class Datatypes:
        datatype_definition_boolean: list[DatatypeDefinitionBoolean] = field(
            default_factory=list,
            metadata={
                "name": "DATATYPE-DEFINITION-BOOLEAN",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )
        datatype_definition_date: list[DatatypeDefinitionDate] = field(
            default_factory=list,
            metadata={
                "name": "DATATYPE-DEFINITION-DATE",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )
        datatype_definition_enumeration: list[
            DatatypeDefinitionEnumeration
        ] = field(
            default_factory=list,
            metadata={
                "name": "DATATYPE-DEFINITION-ENUMERATION",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )
        datatype_definition_integer: list[DatatypeDefinitionInteger] = field(
            default_factory=list,
            metadata={
                "name": "DATATYPE-DEFINITION-INTEGER",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )
        datatype_definition_real: list[DatatypeDefinitionReal] = field(
            default_factory=list,
            metadata={
                "name": "DATATYPE-DEFINITION-REAL",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )
        datatype_definition_string: list[DatatypeDefinitionString] = field(
            default_factory=list,
            metadata={
                "name": "DATATYPE-DEFINITION-STRING",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )
        datatype_definition_xhtml: list[DatatypeDefinitionXhtml] = field(
            default_factory=list,
            metadata={
                "name": "DATATYPE-DEFINITION-XHTML",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass
    class SpecTypes:
        relation_group_type: list[RelationGroupType] = field(
            default_factory=list,
            metadata={
                "name": "RELATION-GROUP-TYPE",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )
        spec_object_type: list[SpecObjectType] = field(
            default_factory=list,
            metadata={
                "name": "SPEC-OBJECT-TYPE",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )
        spec_relation_type: list[SpecRelationType] = field(
            default_factory=list,
            metadata={
                "name": "SPEC-RELATION-TYPE",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )
        specification_type: list[SpecificationType] = field(
            default_factory=list,
            metadata={
                "name": "SPECIFICATION-TYPE",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass
    class SpecObjects:
        spec_object: list[SpecObject] = field(
            default_factory=list,
            metadata={
                "name": "SPEC-OBJECT",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass
    class SpecRelations:
        spec_relation: list[SpecRelation] = field(
            default_factory=list,
            metadata={
                "name": "SPEC-RELATION",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass
    class Specifications:
        specification: list[Specification] = field(
            default_factory=list,
            metadata={
                "name": "SPECIFICATION",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass
    class SpecRelationGroups:
        relation_group: list[RelationGroup] = field(
            default_factory=list,
            metadata={
                "name": "RELATION-GROUP",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )


@dataclass
class ReqIf:
    class Meta:
        name = "REQ-IF"
        namespace = "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"

    the_header: None | ReqIf.TheHeader = field(
        default=None,
        metadata={
            "name": "THE-HEADER",
            "type": "Element",
            "required": True,
        },
    )
    core_content: None | ReqIf.CoreContent = field(
        default=None,
        metadata={
            "name": "CORE-CONTENT",
            "type": "Element",
            "required": True,
        },
    )
    tool_extensions: None | ReqIf.ToolExtensions = field(
        default=None,
        metadata={
            "name": "TOOL-EXTENSIONS",
            "type": "Element",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )

    @dataclass
    class TheHeader:
        req_if_header: None | ReqIfHeader = field(
            default=None,
            metadata={
                "name": "REQ-IF-HEADER",
                "type": "Element",
                "required": True,
            },
        )

    @dataclass
    class CoreContent:
        req_if_content: None | ReqIfContent = field(
            default=None,
            metadata={
                "name": "REQ-IF-CONTENT",
                "type": "Element",
                "required": True,
            },
        )

    @dataclass
    class ToolExtensions:
        req_if_tool_extension: list[ReqIfToolExtension] = field(
            default_factory=list,
            metadata={
                "name": "REQ-IF-TOOL-EXTENSION",
                "type": "Element",
            },
        )
