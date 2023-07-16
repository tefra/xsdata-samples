from dataclasses import dataclass, field
from typing import List, Optional, Union
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

    identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class AttributeValueBoolean:
    class Meta:
        name = "ATTRIBUTE-VALUE-BOOLEAN"

    definition: Optional["AttributeValueBoolean.Definition"] = field(
        default=None,
        metadata={
            "name": "DEFINITION",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        }
    )
    the_value: Optional[bool] = field(
        default=None,
        metadata={
            "name": "THE-VALUE",
            "type": "Attribute",
            "required": True,
        }
    )

    @dataclass
    class Definition:
        attribute_definition_boolean_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-BOOLEAN-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                "required": True,
            }
        )


@dataclass
class AttributeValueDate:
    class Meta:
        name = "ATTRIBUTE-VALUE-DATE"

    definition: Optional["AttributeValueDate.Definition"] = field(
        default=None,
        metadata={
            "name": "DEFINITION",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        }
    )
    the_value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "THE-VALUE",
            "type": "Attribute",
            "required": True,
        }
    )

    @dataclass
    class Definition:
        attribute_definition_date_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-DATE-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                "required": True,
            }
        )


@dataclass
class AttributeValueEnumeration:
    class Meta:
        name = "ATTRIBUTE-VALUE-ENUMERATION"

    definition: Optional["AttributeValueEnumeration.Definition"] = field(
        default=None,
        metadata={
            "name": "DEFINITION",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        }
    )
    values: Optional["AttributeValueEnumeration.Values"] = field(
        default=None,
        metadata={
            "name": "VALUES",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        }
    )

    @dataclass
    class Definition:
        attribute_definition_enumeration_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-ENUMERATION-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                "required": True,
            }
        )

    @dataclass
    class Values:
        enum_value_ref: List[str] = field(
            default_factory=list,
            metadata={
                "name": "ENUM-VALUE-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )


@dataclass
class AttributeValueInteger:
    class Meta:
        name = "ATTRIBUTE-VALUE-INTEGER"

    definition: Optional["AttributeValueInteger.Definition"] = field(
        default=None,
        metadata={
            "name": "DEFINITION",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        }
    )
    the_value: Optional[int] = field(
        default=None,
        metadata={
            "name": "THE-VALUE",
            "type": "Attribute",
            "required": True,
        }
    )

    @dataclass
    class Definition:
        attribute_definition_integer_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-INTEGER-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                "required": True,
            }
        )


@dataclass
class AttributeValueReal:
    class Meta:
        name = "ATTRIBUTE-VALUE-REAL"

    definition: Optional["AttributeValueReal.Definition"] = field(
        default=None,
        metadata={
            "name": "DEFINITION",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        }
    )
    the_value: Optional[float] = field(
        default=None,
        metadata={
            "name": "THE-VALUE",
            "type": "Attribute",
            "required": True,
        }
    )

    @dataclass
    class Definition:
        attribute_definition_real_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-REAL-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                "required": True,
            }
        )


@dataclass
class AttributeValueString:
    class Meta:
        name = "ATTRIBUTE-VALUE-STRING"

    definition: Optional["AttributeValueString.Definition"] = field(
        default=None,
        metadata={
            "name": "DEFINITION",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        }
    )
    the_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "THE-VALUE",
            "type": "Attribute",
            "required": True,
        }
    )

    @dataclass
    class Definition:
        attribute_definition_string_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-STRING-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                "required": True,
            }
        )


@dataclass
class EmbeddedValue:
    class Meta:
        name = "EMBEDDED-VALUE"

    key: Optional[int] = field(
        default=None,
        metadata={
            "name": "KEY",
            "type": "Attribute",
            "required": True,
        }
    )
    other_content: Optional[str] = field(
        default=None,
        metadata={
            "name": "OTHER-CONTENT",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class ReqIfHeader:
    class Meta:
        name = "REQ-IF-HEADER"

    comment: Optional[str] = field(
        default=None,
        metadata={
            "name": "COMMENT",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        }
    )
    creation_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CREATION-TIME",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        }
    )
    repository_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "REPOSITORY-ID",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        }
    )
    req_if_tool_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "REQ-IF-TOOL-ID",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        }
    )
    req_if_version: str = field(
        init=False,
        default="1.0",
        metadata={
            "name": "REQ-IF-VERSION",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        }
    )
    source_tool_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SOURCE-TOOL-ID",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "name": "TITLE",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        }
    )
    identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class ReqIfToolExtension:
    class Meta:
        name = "REQ-IF-TOOL-EXTENSION"

    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )


@dataclass
class AttributeDefinitionBoolean:
    class Meta:
        name = "ATTRIBUTE-DEFINITION-BOOLEAN"

    alternative_id: Optional["AttributeDefinitionBoolean.AlternativeId"] = field(
        default=None,
        metadata={
            "name": "ALTERNATIVE-ID",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        }
    )
    default_value: Optional["AttributeDefinitionBoolean.DefaultValue"] = field(
        default=None,
        metadata={
            "name": "DEFAULT-VALUE",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        }
    )
    type_value: Optional["AttributeDefinitionBoolean.TypeType"] = field(
        default=None,
        metadata={
            "name": "TYPE",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        }
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        }
    )
    identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        }
    )
    is_editable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IS-EDITABLE",
            "type": "Attribute",
        }
    )
    last_change: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        }
    )
    long_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        }
    )

    @dataclass
    class AlternativeId:
        alternative_id: Optional[AlternativeId] = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )

    @dataclass
    class DefaultValue:
        attribute_value_boolean: Optional[AttributeValueBoolean] = field(
            default=None,
            metadata={
                "name": "ATTRIBUTE-VALUE-BOOLEAN",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )

    @dataclass
    class TypeType:
        datatype_definition_boolean_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "DATATYPE-DEFINITION-BOOLEAN-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                "required": True,
            }
        )


@dataclass
class AttributeDefinitionDate:
    class Meta:
        name = "ATTRIBUTE-DEFINITION-DATE"

    alternative_id: Optional["AttributeDefinitionDate.AlternativeId"] = field(
        default=None,
        metadata={
            "name": "ALTERNATIVE-ID",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        }
    )
    default_value: Optional["AttributeDefinitionDate.DefaultValue"] = field(
        default=None,
        metadata={
            "name": "DEFAULT-VALUE",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        }
    )
    type_value: Optional["AttributeDefinitionDate.TypeType"] = field(
        default=None,
        metadata={
            "name": "TYPE",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        }
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        }
    )
    identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        }
    )
    is_editable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IS-EDITABLE",
            "type": "Attribute",
        }
    )
    last_change: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        }
    )
    long_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        }
    )

    @dataclass
    class AlternativeId:
        alternative_id: Optional[AlternativeId] = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )

    @dataclass
    class DefaultValue:
        attribute_value_date: Optional[AttributeValueDate] = field(
            default=None,
            metadata={
                "name": "ATTRIBUTE-VALUE-DATE",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )

    @dataclass
    class TypeType:
        datatype_definition_date_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "DATATYPE-DEFINITION-DATE-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                "required": True,
            }
        )


@dataclass
class AttributeDefinitionEnumeration:
    class Meta:
        name = "ATTRIBUTE-DEFINITION-ENUMERATION"

    default_value: Optional["AttributeDefinitionEnumeration.DefaultValue"] = field(
        default=None,
        metadata={
            "name": "DEFAULT-VALUE",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        }
    )
    alternative_id: Optional["AttributeDefinitionEnumeration.AlternativeId"] = field(
        default=None,
        metadata={
            "name": "ALTERNATIVE-ID",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        }
    )
    type_value: Optional["AttributeDefinitionEnumeration.TypeType"] = field(
        default=None,
        metadata={
            "name": "TYPE",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        }
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        }
    )
    identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        }
    )
    is_editable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IS-EDITABLE",
            "type": "Attribute",
        }
    )
    last_change: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        }
    )
    long_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        }
    )
    multi_valued: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MULTI-VALUED",
            "type": "Attribute",
            "required": True,
        }
    )

    @dataclass
    class DefaultValue:
        attribute_value_enumeration: Optional[AttributeValueEnumeration] = field(
            default=None,
            metadata={
                "name": "ATTRIBUTE-VALUE-ENUMERATION",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )

    @dataclass
    class AlternativeId:
        alternative_id: Optional[AlternativeId] = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )

    @dataclass
    class TypeType:
        datatype_definition_enumeration_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "DATATYPE-DEFINITION-ENUMERATION-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                "required": True,
            }
        )


@dataclass
class AttributeDefinitionInteger:
    class Meta:
        name = "ATTRIBUTE-DEFINITION-INTEGER"

    alternative_id: Optional["AttributeDefinitionInteger.AlternativeId"] = field(
        default=None,
        metadata={
            "name": "ALTERNATIVE-ID",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        }
    )
    default_value: Optional["AttributeDefinitionInteger.DefaultValue"] = field(
        default=None,
        metadata={
            "name": "DEFAULT-VALUE",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        }
    )
    type_value: Optional["AttributeDefinitionInteger.TypeType"] = field(
        default=None,
        metadata={
            "name": "TYPE",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        }
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        }
    )
    identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        }
    )
    is_editable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IS-EDITABLE",
            "type": "Attribute",
        }
    )
    last_change: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        }
    )
    long_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        }
    )

    @dataclass
    class AlternativeId:
        alternative_id: Optional[AlternativeId] = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )

    @dataclass
    class DefaultValue:
        attribute_value_integer: Optional[AttributeValueInteger] = field(
            default=None,
            metadata={
                "name": "ATTRIBUTE-VALUE-INTEGER",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )

    @dataclass
    class TypeType:
        datatype_definition_integer_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "DATATYPE-DEFINITION-INTEGER-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                "required": True,
            }
        )


@dataclass
class AttributeDefinitionReal:
    class Meta:
        name = "ATTRIBUTE-DEFINITION-REAL"

    alternative_id: Optional["AttributeDefinitionReal.AlternativeId"] = field(
        default=None,
        metadata={
            "name": "ALTERNATIVE-ID",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        }
    )
    default_value: Optional["AttributeDefinitionReal.DefaultValue"] = field(
        default=None,
        metadata={
            "name": "DEFAULT-VALUE",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        }
    )
    type_value: Optional["AttributeDefinitionReal.TypeType"] = field(
        default=None,
        metadata={
            "name": "TYPE",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        }
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        }
    )
    identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        }
    )
    is_editable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IS-EDITABLE",
            "type": "Attribute",
        }
    )
    last_change: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        }
    )
    long_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        }
    )

    @dataclass
    class AlternativeId:
        alternative_id: Optional[AlternativeId] = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )

    @dataclass
    class DefaultValue:
        attribute_value_real: Optional[AttributeValueReal] = field(
            default=None,
            metadata={
                "name": "ATTRIBUTE-VALUE-REAL",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )

    @dataclass
    class TypeType:
        datatype_definition_real_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "DATATYPE-DEFINITION-REAL-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                "required": True,
            }
        )


@dataclass
class AttributeDefinitionString:
    class Meta:
        name = "ATTRIBUTE-DEFINITION-STRING"

    alternative_id: Optional["AttributeDefinitionString.AlternativeId"] = field(
        default=None,
        metadata={
            "name": "ALTERNATIVE-ID",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        }
    )
    default_value: Optional["AttributeDefinitionString.DefaultValue"] = field(
        default=None,
        metadata={
            "name": "DEFAULT-VALUE",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        }
    )
    type_value: Optional["AttributeDefinitionString.TypeType"] = field(
        default=None,
        metadata={
            "name": "TYPE",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        }
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        }
    )
    identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        }
    )
    is_editable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IS-EDITABLE",
            "type": "Attribute",
        }
    )
    last_change: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        }
    )
    long_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        }
    )

    @dataclass
    class AlternativeId:
        alternative_id: Optional[AlternativeId] = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )

    @dataclass
    class DefaultValue:
        attribute_value_string: Optional[AttributeValueString] = field(
            default=None,
            metadata={
                "name": "ATTRIBUTE-VALUE-STRING",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )

    @dataclass
    class TypeType:
        datatype_definition_string_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "DATATYPE-DEFINITION-STRING-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                "required": True,
            }
        )


@dataclass
class DatatypeDefinitionBoolean:
    class Meta:
        name = "DATATYPE-DEFINITION-BOOLEAN"

    alternative_id: Optional["DatatypeDefinitionBoolean.AlternativeId"] = field(
        default=None,
        metadata={
            "name": "ALTERNATIVE-ID",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        }
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        }
    )
    identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        }
    )
    last_change: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        }
    )
    long_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        }
    )

    @dataclass
    class AlternativeId:
        alternative_id: Optional[AlternativeId] = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )


@dataclass
class DatatypeDefinitionDate:
    class Meta:
        name = "DATATYPE-DEFINITION-DATE"

    alternative_id: Optional["DatatypeDefinitionDate.AlternativeId"] = field(
        default=None,
        metadata={
            "name": "ALTERNATIVE-ID",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        }
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        }
    )
    identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        }
    )
    last_change: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        }
    )
    long_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        }
    )

    @dataclass
    class AlternativeId:
        alternative_id: Optional[AlternativeId] = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )


@dataclass
class DatatypeDefinitionInteger:
    class Meta:
        name = "DATATYPE-DEFINITION-INTEGER"

    alternative_id: Optional["DatatypeDefinitionInteger.AlternativeId"] = field(
        default=None,
        metadata={
            "name": "ALTERNATIVE-ID",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        }
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        }
    )
    identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        }
    )
    last_change: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        }
    )
    long_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        }
    )
    max: Optional[int] = field(
        default=None,
        metadata={
            "name": "MAX",
            "type": "Attribute",
            "required": True,
        }
    )
    min: Optional[int] = field(
        default=None,
        metadata={
            "name": "MIN",
            "type": "Attribute",
            "required": True,
        }
    )

    @dataclass
    class AlternativeId:
        alternative_id: Optional[AlternativeId] = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )


@dataclass
class DatatypeDefinitionReal:
    class Meta:
        name = "DATATYPE-DEFINITION-REAL"

    alternative_id: Optional["DatatypeDefinitionReal.AlternativeId"] = field(
        default=None,
        metadata={
            "name": "ALTERNATIVE-ID",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        }
    )
    accuracy: Optional[int] = field(
        default=None,
        metadata={
            "name": "ACCURACY",
            "type": "Attribute",
            "required": True,
        }
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        }
    )
    identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        }
    )
    last_change: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        }
    )
    long_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        }
    )
    max: Optional[float] = field(
        default=None,
        metadata={
            "name": "MAX",
            "type": "Attribute",
            "required": True,
        }
    )
    min: Optional[float] = field(
        default=None,
        metadata={
            "name": "MIN",
            "type": "Attribute",
            "required": True,
        }
    )

    @dataclass
    class AlternativeId:
        alternative_id: Optional[AlternativeId] = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )


@dataclass
class DatatypeDefinitionString:
    class Meta:
        name = "DATATYPE-DEFINITION-STRING"

    alternative_id: Optional["DatatypeDefinitionString.AlternativeId"] = field(
        default=None,
        metadata={
            "name": "ALTERNATIVE-ID",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        }
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        }
    )
    identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        }
    )
    last_change: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        }
    )
    long_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        }
    )
    max_length: Optional[int] = field(
        default=None,
        metadata={
            "name": "MAX-LENGTH",
            "type": "Attribute",
            "required": True,
        }
    )

    @dataclass
    class AlternativeId:
        alternative_id: Optional[AlternativeId] = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )


@dataclass
class DatatypeDefinitionXhtml:
    class Meta:
        name = "DATATYPE-DEFINITION-XHTML"

    alternative_id: Optional["DatatypeDefinitionXhtml.AlternativeId"] = field(
        default=None,
        metadata={
            "name": "ALTERNATIVE-ID",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        }
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        }
    )
    identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        }
    )
    last_change: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        }
    )
    long_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        }
    )

    @dataclass
    class AlternativeId:
        alternative_id: Optional[AlternativeId] = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )


@dataclass
class EnumValue:
    class Meta:
        name = "ENUM-VALUE"

    alternative_id: Optional["EnumValue.AlternativeId"] = field(
        default=None,
        metadata={
            "name": "ALTERNATIVE-ID",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        }
    )
    properties: Optional["EnumValue.Properties"] = field(
        default=None,
        metadata={
            "name": "PROPERTIES",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        }
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        }
    )
    identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        }
    )
    last_change: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        }
    )
    long_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        }
    )

    @dataclass
    class AlternativeId:
        alternative_id: Optional[AlternativeId] = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )

    @dataclass
    class Properties:
        embedded_value: Optional[EmbeddedValue] = field(
            default=None,
            metadata={
                "name": "EMBEDDED-VALUE",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                "required": True,
            }
        )


@dataclass
class RelationGroup:
    class Meta:
        name = "RELATION-GROUP"

    alternative_id: Optional["RelationGroup.AlternativeId"] = field(
        default=None,
        metadata={
            "name": "ALTERNATIVE-ID",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        }
    )
    source_specification: Optional["RelationGroup.SourceSpecification"] = field(
        default=None,
        metadata={
            "name": "SOURCE-SPECIFICATION",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        }
    )
    spec_relations: Optional["RelationGroup.SpecRelations"] = field(
        default=None,
        metadata={
            "name": "SPEC-RELATIONS",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        }
    )
    target_specification: Optional["RelationGroup.TargetSpecification"] = field(
        default=None,
        metadata={
            "name": "TARGET-SPECIFICATION",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        }
    )
    type_value: Optional["RelationGroup.TypeType"] = field(
        default=None,
        metadata={
            "name": "TYPE",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        }
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        }
    )
    identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        }
    )
    last_change: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        }
    )
    long_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        }
    )

    @dataclass
    class AlternativeId:
        alternative_id: Optional[AlternativeId] = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )

    @dataclass
    class SourceSpecification:
        specification_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "SPECIFICATION-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                "required": True,
            }
        )

    @dataclass
    class SpecRelations:
        spec_relation_ref: List[str] = field(
            default_factory=list,
            metadata={
                "name": "SPEC-RELATION-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )

    @dataclass
    class TargetSpecification:
        specification_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "SPECIFICATION-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                "required": True,
            }
        )

    @dataclass
    class TypeType:
        relation_group_type_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "RELATION-GROUP-TYPE-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                "required": True,
            }
        )


@dataclass
class SpecHierarchy:
    class Meta:
        name = "SPEC-HIERARCHY"

    alternative_id: Optional["SpecHierarchy.AlternativeId"] = field(
        default=None,
        metadata={
            "name": "ALTERNATIVE-ID",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        }
    )
    children: Optional["SpecHierarchy.Children"] = field(
        default=None,
        metadata={
            "name": "CHILDREN",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        }
    )
    editable_atts: Optional["SpecHierarchy.EditableAtts"] = field(
        default=None,
        metadata={
            "name": "EDITABLE-ATTS",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        }
    )
    object_value: Optional["SpecHierarchy.Object"] = field(
        default=None,
        metadata={
            "name": "OBJECT",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        }
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        }
    )
    identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        }
    )
    is_editable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IS-EDITABLE",
            "type": "Attribute",
        }
    )
    is_table_internal: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IS-TABLE-INTERNAL",
            "type": "Attribute",
        }
    )
    last_change: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        }
    )
    long_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        }
    )

    @dataclass
    class AlternativeId:
        alternative_id: Optional[AlternativeId] = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )

    @dataclass
    class Children:
        spec_hierarchy: List["SpecHierarchy"] = field(
            default_factory=list,
            metadata={
                "name": "SPEC-HIERARCHY",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )

    @dataclass
    class EditableAtts:
        attribute_definition_boolean_ref: List[str] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-BOOLEAN-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )
        attribute_definition_date_ref: List[str] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-DATE-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )
        attribute_definition_enumeration_ref: List[str] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-ENUMERATION-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )
        attribute_definition_integer_ref: List[str] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-INTEGER-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )
        attribute_definition_real_ref: List[str] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-REAL-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )
        attribute_definition_string_ref: List[str] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-STRING-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )
        attribute_definition_xhtml_ref: List[str] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-XHTML-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )

    @dataclass
    class Object:
        spec_object_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "SPEC-OBJECT-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                "required": True,
            }
        )


@dataclass
class XhtmlContent:
    class Meta:
        name = "XHTML-CONTENT"

    p: Optional[XhtmlPType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )
    div: Optional[XhtmlDivType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1999/xhtml",
        }
    )


@dataclass
class AttributeValueXhtml:
    class Meta:
        name = "ATTRIBUTE-VALUE-XHTML"

    the_value: Optional[XhtmlContent] = field(
        default=None,
        metadata={
            "name": "THE-VALUE",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        }
    )
    the_original_value: Optional[XhtmlContent] = field(
        default=None,
        metadata={
            "name": "THE-ORIGINAL-VALUE",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        }
    )
    definition: Optional["AttributeValueXhtml.Definition"] = field(
        default=None,
        metadata={
            "name": "DEFINITION",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        }
    )
    is_simplified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IS-SIMPLIFIED",
            "type": "Attribute",
        }
    )

    @dataclass
    class Definition:
        attribute_definition_xhtml_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-XHTML-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                "required": True,
            }
        )


@dataclass
class DatatypeDefinitionEnumeration:
    class Meta:
        name = "DATATYPE-DEFINITION-ENUMERATION"

    alternative_id: Optional["DatatypeDefinitionEnumeration.AlternativeId"] = field(
        default=None,
        metadata={
            "name": "ALTERNATIVE-ID",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        }
    )
    specified_values: Optional["DatatypeDefinitionEnumeration.SpecifiedValues"] = field(
        default=None,
        metadata={
            "name": "SPECIFIED-VALUES",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        }
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        }
    )
    identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        }
    )
    last_change: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        }
    )
    long_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        }
    )

    @dataclass
    class AlternativeId:
        alternative_id: Optional[AlternativeId] = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )

    @dataclass
    class SpecifiedValues:
        enum_value: List[EnumValue] = field(
            default_factory=list,
            metadata={
                "name": "ENUM-VALUE",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )


@dataclass
class AttributeDefinitionXhtml:
    class Meta:
        name = "ATTRIBUTE-DEFINITION-XHTML"

    alternative_id: Optional["AttributeDefinitionXhtml.AlternativeId"] = field(
        default=None,
        metadata={
            "name": "ALTERNATIVE-ID",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        }
    )
    default_value: Optional["AttributeDefinitionXhtml.DefaultValue"] = field(
        default=None,
        metadata={
            "name": "DEFAULT-VALUE",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        }
    )
    type_value: Optional["AttributeDefinitionXhtml.TypeType"] = field(
        default=None,
        metadata={
            "name": "TYPE",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        }
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        }
    )
    identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        }
    )
    is_editable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IS-EDITABLE",
            "type": "Attribute",
        }
    )
    last_change: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        }
    )
    long_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        }
    )

    @dataclass
    class AlternativeId:
        alternative_id: Optional[AlternativeId] = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )

    @dataclass
    class DefaultValue:
        attribute_value_xhtml: Optional[AttributeValueXhtml] = field(
            default=None,
            metadata={
                "name": "ATTRIBUTE-VALUE-XHTML",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )

    @dataclass
    class TypeType:
        datatype_definition_xhtml_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "DATATYPE-DEFINITION-XHTML-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                "required": True,
            }
        )


@dataclass
class SpecObject:
    class Meta:
        name = "SPEC-OBJECT"

    alternative_id: Optional["SpecObject.AlternativeId"] = field(
        default=None,
        metadata={
            "name": "ALTERNATIVE-ID",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        }
    )
    values: Optional["SpecObject.Values"] = field(
        default=None,
        metadata={
            "name": "VALUES",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        }
    )
    type_value: Optional["SpecObject.TypeType"] = field(
        default=None,
        metadata={
            "name": "TYPE",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        }
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        }
    )
    identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        }
    )
    last_change: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        }
    )
    long_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        }
    )

    @dataclass
    class AlternativeId:
        alternative_id: Optional[AlternativeId] = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )

    @dataclass
    class Values:
        attribute_value_boolean: List[AttributeValueBoolean] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-VALUE-BOOLEAN",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )
        attribute_value_date: List[AttributeValueDate] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-VALUE-DATE",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )
        attribute_value_enumeration: List[AttributeValueEnumeration] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-VALUE-ENUMERATION",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )
        attribute_value_integer: List[AttributeValueInteger] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-VALUE-INTEGER",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )
        attribute_value_real: List[AttributeValueReal] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-VALUE-REAL",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )
        attribute_value_string: List[AttributeValueString] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-VALUE-STRING",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )
        attribute_value_xhtml: List[AttributeValueXhtml] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-VALUE-XHTML",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )

    @dataclass
    class TypeType:
        spec_object_type_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "SPEC-OBJECT-TYPE-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                "required": True,
            }
        )


@dataclass
class SpecRelation:
    class Meta:
        name = "SPEC-RELATION"

    alternative_id: Optional["SpecRelation.AlternativeId"] = field(
        default=None,
        metadata={
            "name": "ALTERNATIVE-ID",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        }
    )
    values: Optional["SpecRelation.Values"] = field(
        default=None,
        metadata={
            "name": "VALUES",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        }
    )
    source: Optional["SpecRelation.Source"] = field(
        default=None,
        metadata={
            "name": "SOURCE",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        }
    )
    target: Optional["SpecRelation.Target"] = field(
        default=None,
        metadata={
            "name": "TARGET",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        }
    )
    type_value: Optional["SpecRelation.TypeType"] = field(
        default=None,
        metadata={
            "name": "TYPE",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        }
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        }
    )
    identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        }
    )
    last_change: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        }
    )
    long_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        }
    )

    @dataclass
    class AlternativeId:
        alternative_id: Optional[AlternativeId] = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )

    @dataclass
    class Values:
        attribute_value_boolean: List[AttributeValueBoolean] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-VALUE-BOOLEAN",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )
        attribute_value_date: List[AttributeValueDate] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-VALUE-DATE",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )
        attribute_value_enumeration: List[AttributeValueEnumeration] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-VALUE-ENUMERATION",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )
        attribute_value_integer: List[AttributeValueInteger] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-VALUE-INTEGER",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )
        attribute_value_real: List[AttributeValueReal] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-VALUE-REAL",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )
        attribute_value_string: List[AttributeValueString] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-VALUE-STRING",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )
        attribute_value_xhtml: List[AttributeValueXhtml] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-VALUE-XHTML",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )

    @dataclass
    class Source:
        spec_object_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "SPEC-OBJECT-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                "required": True,
            }
        )

    @dataclass
    class Target:
        spec_object_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "SPEC-OBJECT-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                "required": True,
            }
        )

    @dataclass
    class TypeType:
        spec_relation_type_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "SPEC-RELATION-TYPE-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                "required": True,
            }
        )


@dataclass
class Specification:
    class Meta:
        name = "SPECIFICATION"

    alternative_id: Optional["Specification.AlternativeId"] = field(
        default=None,
        metadata={
            "name": "ALTERNATIVE-ID",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        }
    )
    values: Optional["Specification.Values"] = field(
        default=None,
        metadata={
            "name": "VALUES",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        }
    )
    children: Optional["Specification.Children"] = field(
        default=None,
        metadata={
            "name": "CHILDREN",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        }
    )
    type_value: Optional["Specification.TypeType"] = field(
        default=None,
        metadata={
            "name": "TYPE",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        }
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        }
    )
    identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        }
    )
    last_change: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        }
    )
    long_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        }
    )

    @dataclass
    class AlternativeId:
        alternative_id: Optional[AlternativeId] = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )

    @dataclass
    class Values:
        attribute_value_boolean: List[AttributeValueBoolean] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-VALUE-BOOLEAN",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )
        attribute_value_date: List[AttributeValueDate] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-VALUE-DATE",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )
        attribute_value_enumeration: List[AttributeValueEnumeration] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-VALUE-ENUMERATION",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )
        attribute_value_integer: List[AttributeValueInteger] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-VALUE-INTEGER",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )
        attribute_value_real: List[AttributeValueReal] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-VALUE-REAL",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )
        attribute_value_string: List[AttributeValueString] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-VALUE-STRING",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )
        attribute_value_xhtml: List[AttributeValueXhtml] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-VALUE-XHTML",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )

    @dataclass
    class Children:
        spec_hierarchy: List[SpecHierarchy] = field(
            default_factory=list,
            metadata={
                "name": "SPEC-HIERARCHY",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )

    @dataclass
    class TypeType:
        specification_type_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "SPECIFICATION-TYPE-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                "required": True,
            }
        )


@dataclass
class RelationGroupType:
    class Meta:
        name = "RELATION-GROUP-TYPE"

    alternative_id: Optional["RelationGroupType.AlternativeId"] = field(
        default=None,
        metadata={
            "name": "ALTERNATIVE-ID",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        }
    )
    spec_attributes: Optional["RelationGroupType.SpecAttributes"] = field(
        default=None,
        metadata={
            "name": "SPEC-ATTRIBUTES",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        }
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        }
    )
    identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        }
    )
    last_change: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        }
    )
    long_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        }
    )

    @dataclass
    class AlternativeId:
        alternative_id: Optional[AlternativeId] = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )

    @dataclass
    class SpecAttributes:
        attribute_definition_boolean: List[AttributeDefinitionBoolean] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-BOOLEAN",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )
        attribute_definition_date: List[AttributeDefinitionDate] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-DATE",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )
        attribute_definition_enumeration: List[AttributeDefinitionEnumeration] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-ENUMERATION",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )
        attribute_definition_integer: List[AttributeDefinitionInteger] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-INTEGER",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )
        attribute_definition_real: List[AttributeDefinitionReal] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-REAL",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )
        attribute_definition_string: List[AttributeDefinitionString] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-STRING",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )
        attribute_definition_xhtml: List[AttributeDefinitionXhtml] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-XHTML",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )


@dataclass
class SpecObjectType:
    class Meta:
        name = "SPEC-OBJECT-TYPE"

    alternative_id: Optional["SpecObjectType.AlternativeId"] = field(
        default=None,
        metadata={
            "name": "ALTERNATIVE-ID",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        }
    )
    spec_attributes: Optional["SpecObjectType.SpecAttributes"] = field(
        default=None,
        metadata={
            "name": "SPEC-ATTRIBUTES",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        }
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        }
    )
    identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        }
    )
    last_change: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        }
    )
    long_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        }
    )

    @dataclass
    class AlternativeId:
        alternative_id: Optional[AlternativeId] = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )

    @dataclass
    class SpecAttributes:
        attribute_definition_boolean: List[AttributeDefinitionBoolean] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-BOOLEAN",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )
        attribute_definition_date: List[AttributeDefinitionDate] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-DATE",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )
        attribute_definition_enumeration: List[AttributeDefinitionEnumeration] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-ENUMERATION",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )
        attribute_definition_integer: List[AttributeDefinitionInteger] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-INTEGER",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )
        attribute_definition_real: List[AttributeDefinitionReal] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-REAL",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )
        attribute_definition_string: List[AttributeDefinitionString] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-STRING",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )
        attribute_definition_xhtml: List[AttributeDefinitionXhtml] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-XHTML",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )


@dataclass
class SpecRelationType:
    class Meta:
        name = "SPEC-RELATION-TYPE"

    alternative_id: Optional["SpecRelationType.AlternativeId"] = field(
        default=None,
        metadata={
            "name": "ALTERNATIVE-ID",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        }
    )
    spec_attributes: Optional["SpecRelationType.SpecAttributes"] = field(
        default=None,
        metadata={
            "name": "SPEC-ATTRIBUTES",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        }
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        }
    )
    identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        }
    )
    last_change: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        }
    )
    long_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        }
    )

    @dataclass
    class AlternativeId:
        alternative_id: Optional[AlternativeId] = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )

    @dataclass
    class SpecAttributes:
        attribute_definition_boolean: List[AttributeDefinitionBoolean] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-BOOLEAN",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )
        attribute_definition_date: List[AttributeDefinitionDate] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-DATE",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )
        attribute_definition_enumeration: List[AttributeDefinitionEnumeration] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-ENUMERATION",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )
        attribute_definition_integer: List[AttributeDefinitionInteger] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-INTEGER",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )
        attribute_definition_real: List[AttributeDefinitionReal] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-REAL",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )
        attribute_definition_string: List[AttributeDefinitionString] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-STRING",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )
        attribute_definition_xhtml: List[AttributeDefinitionXhtml] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-XHTML",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )


@dataclass
class SpecificationType:
    class Meta:
        name = "SPECIFICATION-TYPE"

    alternative_id: Optional["SpecificationType.AlternativeId"] = field(
        default=None,
        metadata={
            "name": "ALTERNATIVE-ID",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        }
    )
    spec_attributes: Optional["SpecificationType.SpecAttributes"] = field(
        default=None,
        metadata={
            "name": "SPEC-ATTRIBUTES",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        }
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        }
    )
    identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        }
    )
    last_change: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        }
    )
    long_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        }
    )

    @dataclass
    class AlternativeId:
        alternative_id: Optional[AlternativeId] = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )

    @dataclass
    class SpecAttributes:
        attribute_definition_boolean: List[AttributeDefinitionBoolean] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-BOOLEAN",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )
        attribute_definition_date: List[AttributeDefinitionDate] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-DATE",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )
        attribute_definition_enumeration: List[AttributeDefinitionEnumeration] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-ENUMERATION",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )
        attribute_definition_integer: List[AttributeDefinitionInteger] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-INTEGER",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )
        attribute_definition_real: List[AttributeDefinitionReal] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-REAL",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )
        attribute_definition_string: List[AttributeDefinitionString] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-STRING",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )
        attribute_definition_xhtml: List[AttributeDefinitionXhtml] = field(
            default_factory=list,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-XHTML",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )


@dataclass
class ReqIfContent:
    class Meta:
        name = "REQ-IF-CONTENT"

    datatypes: Optional["ReqIfContent.Datatypes"] = field(
        default=None,
        metadata={
            "name": "DATATYPES",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        }
    )
    spec_types: Optional["ReqIfContent.SpecTypes"] = field(
        default=None,
        metadata={
            "name": "SPEC-TYPES",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        }
    )
    spec_objects: Optional["ReqIfContent.SpecObjects"] = field(
        default=None,
        metadata={
            "name": "SPEC-OBJECTS",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        }
    )
    spec_relations: Optional["ReqIfContent.SpecRelations"] = field(
        default=None,
        metadata={
            "name": "SPEC-RELATIONS",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        }
    )
    specifications: Optional["ReqIfContent.Specifications"] = field(
        default=None,
        metadata={
            "name": "SPECIFICATIONS",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        }
    )
    spec_relation_groups: Optional["ReqIfContent.SpecRelationGroups"] = field(
        default=None,
        metadata={
            "name": "SPEC-RELATION-GROUPS",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        }
    )

    @dataclass
    class Datatypes:
        datatype_definition_boolean: List[DatatypeDefinitionBoolean] = field(
            default_factory=list,
            metadata={
                "name": "DATATYPE-DEFINITION-BOOLEAN",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )
        datatype_definition_date: List[DatatypeDefinitionDate] = field(
            default_factory=list,
            metadata={
                "name": "DATATYPE-DEFINITION-DATE",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )
        datatype_definition_enumeration: List[DatatypeDefinitionEnumeration] = field(
            default_factory=list,
            metadata={
                "name": "DATATYPE-DEFINITION-ENUMERATION",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )
        datatype_definition_integer: List[DatatypeDefinitionInteger] = field(
            default_factory=list,
            metadata={
                "name": "DATATYPE-DEFINITION-INTEGER",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )
        datatype_definition_real: List[DatatypeDefinitionReal] = field(
            default_factory=list,
            metadata={
                "name": "DATATYPE-DEFINITION-REAL",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )
        datatype_definition_string: List[DatatypeDefinitionString] = field(
            default_factory=list,
            metadata={
                "name": "DATATYPE-DEFINITION-STRING",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )
        datatype_definition_xhtml: List[DatatypeDefinitionXhtml] = field(
            default_factory=list,
            metadata={
                "name": "DATATYPE-DEFINITION-XHTML",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )

    @dataclass
    class SpecTypes:
        relation_group_type: List[RelationGroupType] = field(
            default_factory=list,
            metadata={
                "name": "RELATION-GROUP-TYPE",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )
        spec_object_type: List[SpecObjectType] = field(
            default_factory=list,
            metadata={
                "name": "SPEC-OBJECT-TYPE",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )
        spec_relation_type: List[SpecRelationType] = field(
            default_factory=list,
            metadata={
                "name": "SPEC-RELATION-TYPE",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )
        specification_type: List[SpecificationType] = field(
            default_factory=list,
            metadata={
                "name": "SPECIFICATION-TYPE",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )

    @dataclass
    class SpecObjects:
        spec_object: List[SpecObject] = field(
            default_factory=list,
            metadata={
                "name": "SPEC-OBJECT",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )

    @dataclass
    class SpecRelations:
        spec_relation: List[SpecRelation] = field(
            default_factory=list,
            metadata={
                "name": "SPEC-RELATION",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )

    @dataclass
    class Specifications:
        specification: List[Specification] = field(
            default_factory=list,
            metadata={
                "name": "SPECIFICATION",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )

    @dataclass
    class SpecRelationGroups:
        relation_group: List[RelationGroup] = field(
            default_factory=list,
            metadata={
                "name": "RELATION-GROUP",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            }
        )


@dataclass
class ReqIf:
    class Meta:
        name = "REQ-IF"
        namespace = "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"

    the_header: Optional["ReqIf.TheHeader"] = field(
        default=None,
        metadata={
            "name": "THE-HEADER",
            "type": "Element",
            "required": True,
        }
    )
    core_content: Optional["ReqIf.CoreContent"] = field(
        default=None,
        metadata={
            "name": "CORE-CONTENT",
            "type": "Element",
            "required": True,
        }
    )
    tool_extensions: Optional["ReqIf.ToolExtensions"] = field(
        default=None,
        metadata={
            "name": "TOOL-EXTENSIONS",
            "type": "Element",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )

    @dataclass
    class TheHeader:
        req_if_header: Optional[ReqIfHeader] = field(
            default=None,
            metadata={
                "name": "REQ-IF-HEADER",
                "type": "Element",
                "required": True,
            }
        )

    @dataclass
    class CoreContent:
        req_if_content: Optional[ReqIfContent] = field(
            default=None,
            metadata={
                "name": "REQ-IF-CONTENT",
                "type": "Element",
                "required": True,
            }
        )

    @dataclass
    class ToolExtensions:
        req_if_tool_extension: List[ReqIfToolExtension] = field(
            default_factory=list,
            metadata={
                "name": "REQ-IF-TOOL-EXTENSION",
                "type": "Element",
            }
        )
