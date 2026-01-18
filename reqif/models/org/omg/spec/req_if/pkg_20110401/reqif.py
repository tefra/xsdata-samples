from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

from reqif.models.org.w3.xml.pkg_1998.namespace import LangValue
from reqif.models.xtml import (
    XhtmlDivType,
    XhtmlPType,
)

__NAMESPACE__ = "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"


@dataclass(kw_only=True)
class AlternativeId:
    class Meta:
        name = "ALTERNATIVE-ID"

    identifier: str = field(
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AttributeValueBoolean:
    class Meta:
        name = "ATTRIBUTE-VALUE-BOOLEAN"

    definition: AttributeValueBoolean.Definition = field(
        metadata={
            "name": "DEFINITION",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        }
    )
    the_value: bool = field(
        metadata={
            "name": "THE-VALUE",
            "type": "Attribute",
            "required": True,
        }
    )

    @dataclass(kw_only=True)
    class Definition:
        attribute_definition_boolean_ref: None | str = field(
            default=None,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-BOOLEAN-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )


@dataclass(kw_only=True)
class AttributeValueDate:
    class Meta:
        name = "ATTRIBUTE-VALUE-DATE"

    definition: AttributeValueDate.Definition = field(
        metadata={
            "name": "DEFINITION",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        }
    )
    the_value: XmlDateTime = field(
        metadata={
            "name": "THE-VALUE",
            "type": "Attribute",
            "required": True,
        }
    )

    @dataclass(kw_only=True)
    class Definition:
        attribute_definition_date_ref: None | str = field(
            default=None,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-DATE-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )


@dataclass(kw_only=True)
class AttributeValueEnumeration:
    class Meta:
        name = "ATTRIBUTE-VALUE-ENUMERATION"

    definition: AttributeValueEnumeration.Definition = field(
        metadata={
            "name": "DEFINITION",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        }
    )
    values: None | AttributeValueEnumeration.Values = field(
        default=None,
        metadata={
            "name": "VALUES",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        },
    )

    @dataclass(kw_only=True)
    class Definition:
        attribute_definition_enumeration_ref: None | str = field(
            default=None,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-ENUMERATION-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass(kw_only=True)
    class Values:
        enum_value_ref: list[str] = field(
            default_factory=list,
            metadata={
                "name": "ENUM-VALUE-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )


@dataclass(kw_only=True)
class AttributeValueInteger:
    class Meta:
        name = "ATTRIBUTE-VALUE-INTEGER"

    definition: AttributeValueInteger.Definition = field(
        metadata={
            "name": "DEFINITION",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        }
    )
    the_value: int = field(
        metadata={
            "name": "THE-VALUE",
            "type": "Attribute",
            "required": True,
        }
    )

    @dataclass(kw_only=True)
    class Definition:
        attribute_definition_integer_ref: None | str = field(
            default=None,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-INTEGER-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )


@dataclass(kw_only=True)
class AttributeValueReal:
    class Meta:
        name = "ATTRIBUTE-VALUE-REAL"

    definition: AttributeValueReal.Definition = field(
        metadata={
            "name": "DEFINITION",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        }
    )
    the_value: float = field(
        metadata={
            "name": "THE-VALUE",
            "type": "Attribute",
            "required": True,
        }
    )

    @dataclass(kw_only=True)
    class Definition:
        attribute_definition_real_ref: None | str = field(
            default=None,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-REAL-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )


@dataclass(kw_only=True)
class AttributeValueString:
    class Meta:
        name = "ATTRIBUTE-VALUE-STRING"

    definition: AttributeValueString.Definition = field(
        metadata={
            "name": "DEFINITION",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        }
    )
    the_value: str = field(
        metadata={
            "name": "THE-VALUE",
            "type": "Attribute",
            "required": True,
        }
    )

    @dataclass(kw_only=True)
    class Definition:
        attribute_definition_string_ref: None | str = field(
            default=None,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-STRING-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )


@dataclass(kw_only=True)
class EmbeddedValue:
    class Meta:
        name = "EMBEDDED-VALUE"

    key: int = field(
        metadata={
            "name": "KEY",
            "type": "Attribute",
            "required": True,
        }
    )
    other_content: str = field(
        metadata={
            "name": "OTHER-CONTENT",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
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
    creation_time: XmlDateTime = field(
        metadata={
            "name": "CREATION-TIME",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        }
    )
    repository_id: None | str = field(
        default=None,
        metadata={
            "name": "REPOSITORY-ID",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        },
    )
    req_if_tool_id: str = field(
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
        },
    )
    source_tool_id: str = field(
        metadata={
            "name": "SOURCE-TOOL-ID",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        }
    )
    title: str = field(
        metadata={
            "name": "TITLE",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        }
    )
    identifier: str = field(
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
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


@dataclass(kw_only=True)
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
    type_value: AttributeDefinitionBoolean.Type = field(
        metadata={
            "name": "TYPE",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        }
    )
    desc: None | str = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        },
    )
    identifier: str = field(
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        }
    )
    is_editable: None | bool = field(
        default=None,
        metadata={
            "name": "IS-EDITABLE",
            "type": "Attribute",
        },
    )
    last_change: XmlDateTime = field(
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        }
    )
    long_name: None | str = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class AlternativeId:
        alternative_id: None | AlternativeId = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass(kw_only=True)
    class DefaultValue:
        attribute_value_boolean: None | AttributeValueBoolean = field(
            default=None,
            metadata={
                "name": "ATTRIBUTE-VALUE-BOOLEAN",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass(kw_only=True)
    class Type:
        datatype_definition_boolean_ref: None | str = field(
            default=None,
            metadata={
                "name": "DATATYPE-DEFINITION-BOOLEAN-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )


@dataclass(kw_only=True)
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
    type_value: AttributeDefinitionDate.Type = field(
        metadata={
            "name": "TYPE",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        }
    )
    desc: None | str = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        },
    )
    identifier: str = field(
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        }
    )
    is_editable: None | bool = field(
        default=None,
        metadata={
            "name": "IS-EDITABLE",
            "type": "Attribute",
        },
    )
    last_change: XmlDateTime = field(
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        }
    )
    long_name: None | str = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class AlternativeId:
        alternative_id: None | AlternativeId = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass(kw_only=True)
    class DefaultValue:
        attribute_value_date: None | AttributeValueDate = field(
            default=None,
            metadata={
                "name": "ATTRIBUTE-VALUE-DATE",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass(kw_only=True)
    class Type:
        datatype_definition_date_ref: None | str = field(
            default=None,
            metadata={
                "name": "DATATYPE-DEFINITION-DATE-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )


@dataclass(kw_only=True)
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
    type_value: AttributeDefinitionEnumeration.Type = field(
        metadata={
            "name": "TYPE",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        }
    )
    desc: None | str = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        },
    )
    identifier: str = field(
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        }
    )
    is_editable: None | bool = field(
        default=None,
        metadata={
            "name": "IS-EDITABLE",
            "type": "Attribute",
        },
    )
    last_change: XmlDateTime = field(
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        }
    )
    long_name: None | str = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        },
    )
    multi_valued: bool = field(
        metadata={
            "name": "MULTI-VALUED",
            "type": "Attribute",
            "required": True,
        }
    )

    @dataclass(kw_only=True)
    class DefaultValue:
        attribute_value_enumeration: None | AttributeValueEnumeration = field(
            default=None,
            metadata={
                "name": "ATTRIBUTE-VALUE-ENUMERATION",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass(kw_only=True)
    class AlternativeId:
        alternative_id: None | AlternativeId = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass(kw_only=True)
    class Type:
        datatype_definition_enumeration_ref: None | str = field(
            default=None,
            metadata={
                "name": "DATATYPE-DEFINITION-ENUMERATION-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )


@dataclass(kw_only=True)
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
    type_value: AttributeDefinitionInteger.Type = field(
        metadata={
            "name": "TYPE",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        }
    )
    desc: None | str = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        },
    )
    identifier: str = field(
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        }
    )
    is_editable: None | bool = field(
        default=None,
        metadata={
            "name": "IS-EDITABLE",
            "type": "Attribute",
        },
    )
    last_change: XmlDateTime = field(
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        }
    )
    long_name: None | str = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class AlternativeId:
        alternative_id: None | AlternativeId = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass(kw_only=True)
    class DefaultValue:
        attribute_value_integer: None | AttributeValueInteger = field(
            default=None,
            metadata={
                "name": "ATTRIBUTE-VALUE-INTEGER",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass(kw_only=True)
    class Type:
        datatype_definition_integer_ref: None | str = field(
            default=None,
            metadata={
                "name": "DATATYPE-DEFINITION-INTEGER-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )


@dataclass(kw_only=True)
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
    type_value: AttributeDefinitionReal.Type = field(
        metadata={
            "name": "TYPE",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        }
    )
    desc: None | str = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        },
    )
    identifier: str = field(
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        }
    )
    is_editable: None | bool = field(
        default=None,
        metadata={
            "name": "IS-EDITABLE",
            "type": "Attribute",
        },
    )
    last_change: XmlDateTime = field(
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        }
    )
    long_name: None | str = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class AlternativeId:
        alternative_id: None | AlternativeId = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass(kw_only=True)
    class DefaultValue:
        attribute_value_real: None | AttributeValueReal = field(
            default=None,
            metadata={
                "name": "ATTRIBUTE-VALUE-REAL",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass(kw_only=True)
    class Type:
        datatype_definition_real_ref: None | str = field(
            default=None,
            metadata={
                "name": "DATATYPE-DEFINITION-REAL-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )


@dataclass(kw_only=True)
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
    type_value: AttributeDefinitionString.Type = field(
        metadata={
            "name": "TYPE",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        }
    )
    desc: None | str = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        },
    )
    identifier: str = field(
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        }
    )
    is_editable: None | bool = field(
        default=None,
        metadata={
            "name": "IS-EDITABLE",
            "type": "Attribute",
        },
    )
    last_change: XmlDateTime = field(
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        }
    )
    long_name: None | str = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class AlternativeId:
        alternative_id: None | AlternativeId = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass(kw_only=True)
    class DefaultValue:
        attribute_value_string: None | AttributeValueString = field(
            default=None,
            metadata={
                "name": "ATTRIBUTE-VALUE-STRING",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass(kw_only=True)
    class Type:
        datatype_definition_string_ref: None | str = field(
            default=None,
            metadata={
                "name": "DATATYPE-DEFINITION-STRING-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )


@dataclass(kw_only=True)
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
    identifier: str = field(
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        }
    )
    long_name: None | str = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class AlternativeId:
        alternative_id: None | AlternativeId = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )


@dataclass(kw_only=True)
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
    identifier: str = field(
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        }
    )
    long_name: None | str = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class AlternativeId:
        alternative_id: None | AlternativeId = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )


@dataclass(kw_only=True)
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
    identifier: str = field(
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        }
    )
    long_name: None | str = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        },
    )
    max: int = field(
        metadata={
            "name": "MAX",
            "type": "Attribute",
            "required": True,
        }
    )
    min: int = field(
        metadata={
            "name": "MIN",
            "type": "Attribute",
            "required": True,
        }
    )

    @dataclass(kw_only=True)
    class AlternativeId:
        alternative_id: None | AlternativeId = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )


@dataclass(kw_only=True)
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
    accuracy: int = field(
        metadata={
            "name": "ACCURACY",
            "type": "Attribute",
            "required": True,
        }
    )
    desc: None | str = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        },
    )
    identifier: str = field(
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        }
    )
    long_name: None | str = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        },
    )
    max: float = field(
        metadata={
            "name": "MAX",
            "type": "Attribute",
            "required": True,
        }
    )
    min: float = field(
        metadata={
            "name": "MIN",
            "type": "Attribute",
            "required": True,
        }
    )

    @dataclass(kw_only=True)
    class AlternativeId:
        alternative_id: None | AlternativeId = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )


@dataclass(kw_only=True)
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
    identifier: str = field(
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        }
    )
    long_name: None | str = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        },
    )
    max_length: int = field(
        metadata={
            "name": "MAX-LENGTH",
            "type": "Attribute",
            "required": True,
        }
    )

    @dataclass(kw_only=True)
    class AlternativeId:
        alternative_id: None | AlternativeId = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )


@dataclass(kw_only=True)
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
    identifier: str = field(
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        }
    )
    long_name: None | str = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class AlternativeId:
        alternative_id: None | AlternativeId = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )


@dataclass(kw_only=True)
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
    properties: EnumValue.Properties = field(
        metadata={
            "name": "PROPERTIES",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        }
    )
    desc: None | str = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        },
    )
    identifier: str = field(
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        }
    )
    long_name: None | str = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class AlternativeId:
        alternative_id: None | AlternativeId = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass(kw_only=True)
    class Properties:
        embedded_value: None | EmbeddedValue = field(
            default=None,
            metadata={
                "name": "EMBEDDED-VALUE",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )


@dataclass(kw_only=True)
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
    source_specification: RelationGroup.SourceSpecification = field(
        metadata={
            "name": "SOURCE-SPECIFICATION",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        }
    )
    spec_relations: None | RelationGroup.SpecRelations = field(
        default=None,
        metadata={
            "name": "SPEC-RELATIONS",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        },
    )
    target_specification: RelationGroup.TargetSpecification = field(
        metadata={
            "name": "TARGET-SPECIFICATION",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        }
    )
    type_value: RelationGroup.Type = field(
        metadata={
            "name": "TYPE",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        }
    )
    desc: None | str = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        },
    )
    identifier: str = field(
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        }
    )
    long_name: None | str = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class AlternativeId:
        alternative_id: None | AlternativeId = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass(kw_only=True)
    class SourceSpecification:
        specification_ref: None | str = field(
            default=None,
            metadata={
                "name": "SPECIFICATION-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass(kw_only=True)
    class SpecRelations:
        spec_relation_ref: list[str] = field(
            default_factory=list,
            metadata={
                "name": "SPEC-RELATION-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass(kw_only=True)
    class TargetSpecification:
        specification_ref: None | str = field(
            default=None,
            metadata={
                "name": "SPECIFICATION-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass(kw_only=True)
    class Type:
        relation_group_type_ref: None | str = field(
            default=None,
            metadata={
                "name": "RELATION-GROUP-TYPE-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )


@dataclass(kw_only=True)
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
    object_value: SpecHierarchy.Object = field(
        metadata={
            "name": "OBJECT",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        }
    )
    desc: None | str = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        },
    )
    identifier: str = field(
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        }
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
    last_change: XmlDateTime = field(
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        }
    )
    long_name: None | str = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class AlternativeId:
        alternative_id: None | AlternativeId = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass(kw_only=True)
    class Children:
        spec_hierarchy: list[SpecHierarchy] = field(
            default_factory=list,
            metadata={
                "name": "SPEC-HIERARCHY",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass(kw_only=True)
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

    @dataclass(kw_only=True)
    class Object:
        spec_object_ref: None | str = field(
            default=None,
            metadata={
                "name": "SPEC-OBJECT-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )


@dataclass(kw_only=True)
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


@dataclass(kw_only=True)
class AttributeValueXhtml:
    class Meta:
        name = "ATTRIBUTE-VALUE-XHTML"

    the_value: XhtmlContent = field(
        metadata={
            "name": "THE-VALUE",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        }
    )
    the_original_value: None | XhtmlContent = field(
        default=None,
        metadata={
            "name": "THE-ORIGINAL-VALUE",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
        },
    )
    definition: AttributeValueXhtml.Definition = field(
        metadata={
            "name": "DEFINITION",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        }
    )
    is_simplified: None | bool = field(
        default=None,
        metadata={
            "name": "IS-SIMPLIFIED",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class Definition:
        attribute_definition_xhtml_ref: None | str = field(
            default=None,
            metadata={
                "name": "ATTRIBUTE-DEFINITION-XHTML-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )


@dataclass(kw_only=True)
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
    identifier: str = field(
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        }
    )
    long_name: None | str = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class AlternativeId:
        alternative_id: None | AlternativeId = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass(kw_only=True)
    class SpecifiedValues:
        enum_value: list[EnumValue] = field(
            default_factory=list,
            metadata={
                "name": "ENUM-VALUE",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )


@dataclass(kw_only=True)
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
    type_value: AttributeDefinitionXhtml.Type = field(
        metadata={
            "name": "TYPE",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        }
    )
    desc: None | str = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        },
    )
    identifier: str = field(
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        }
    )
    is_editable: None | bool = field(
        default=None,
        metadata={
            "name": "IS-EDITABLE",
            "type": "Attribute",
        },
    )
    last_change: XmlDateTime = field(
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        }
    )
    long_name: None | str = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class AlternativeId:
        alternative_id: None | AlternativeId = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass(kw_only=True)
    class DefaultValue:
        attribute_value_xhtml: None | AttributeValueXhtml = field(
            default=None,
            metadata={
                "name": "ATTRIBUTE-VALUE-XHTML",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass(kw_only=True)
    class Type:
        datatype_definition_xhtml_ref: None | str = field(
            default=None,
            metadata={
                "name": "DATATYPE-DEFINITION-XHTML-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )


@dataclass(kw_only=True)
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
    type_value: SpecObject.Type = field(
        metadata={
            "name": "TYPE",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        }
    )
    desc: None | str = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        },
    )
    identifier: str = field(
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        }
    )
    long_name: None | str = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class AlternativeId:
        alternative_id: None | AlternativeId = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass(kw_only=True)
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

    @dataclass(kw_only=True)
    class Type:
        spec_object_type_ref: None | str = field(
            default=None,
            metadata={
                "name": "SPEC-OBJECT-TYPE-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )


@dataclass(kw_only=True)
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
    source: SpecRelation.Source = field(
        metadata={
            "name": "SOURCE",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        }
    )
    target: SpecRelation.Target = field(
        metadata={
            "name": "TARGET",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        }
    )
    type_value: SpecRelation.Type = field(
        metadata={
            "name": "TYPE",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        }
    )
    desc: None | str = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        },
    )
    identifier: str = field(
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        }
    )
    long_name: None | str = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class AlternativeId:
        alternative_id: None | AlternativeId = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass(kw_only=True)
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

    @dataclass(kw_only=True)
    class Source:
        spec_object_ref: None | str = field(
            default=None,
            metadata={
                "name": "SPEC-OBJECT-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass(kw_only=True)
    class Target:
        spec_object_ref: None | str = field(
            default=None,
            metadata={
                "name": "SPEC-OBJECT-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass(kw_only=True)
    class Type:
        spec_relation_type_ref: None | str = field(
            default=None,
            metadata={
                "name": "SPEC-RELATION-TYPE-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )


@dataclass(kw_only=True)
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
    type_value: Specification.Type = field(
        metadata={
            "name": "TYPE",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            "required": True,
        }
    )
    desc: None | str = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Attribute",
        },
    )
    identifier: str = field(
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        }
    )
    long_name: None | str = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class AlternativeId:
        alternative_id: None | AlternativeId = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass(kw_only=True)
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

    @dataclass(kw_only=True)
    class Children:
        spec_hierarchy: list[SpecHierarchy] = field(
            default_factory=list,
            metadata={
                "name": "SPEC-HIERARCHY",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass(kw_only=True)
    class Type:
        specification_type_ref: None | str = field(
            default=None,
            metadata={
                "name": "SPECIFICATION-TYPE-REF",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )


@dataclass(kw_only=True)
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
    identifier: str = field(
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        }
    )
    long_name: None | str = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class AlternativeId:
        alternative_id: None | AlternativeId = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass(kw_only=True)
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


@dataclass(kw_only=True)
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
    identifier: str = field(
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        }
    )
    long_name: None | str = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class AlternativeId:
        alternative_id: None | AlternativeId = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass(kw_only=True)
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


@dataclass(kw_only=True)
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
    identifier: str = field(
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        }
    )
    long_name: None | str = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class AlternativeId:
        alternative_id: None | AlternativeId = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass(kw_only=True)
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


@dataclass(kw_only=True)
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
    identifier: str = field(
        metadata={
            "name": "IDENTIFIER",
            "type": "Attribute",
            "required": True,
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "name": "LAST-CHANGE",
            "type": "Attribute",
            "required": True,
        }
    )
    long_name: None | str = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class AlternativeId:
        alternative_id: None | AlternativeId = field(
            default=None,
            metadata={
                "name": "ALTERNATIVE-ID",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass(kw_only=True)
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


@dataclass(kw_only=True)
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

    @dataclass(kw_only=True)
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

    @dataclass(kw_only=True)
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

    @dataclass(kw_only=True)
    class SpecObjects:
        spec_object: list[SpecObject] = field(
            default_factory=list,
            metadata={
                "name": "SPEC-OBJECT",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass(kw_only=True)
    class SpecRelations:
        spec_relation: list[SpecRelation] = field(
            default_factory=list,
            metadata={
                "name": "SPEC-RELATION",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass(kw_only=True)
    class Specifications:
        specification: list[Specification] = field(
            default_factory=list,
            metadata={
                "name": "SPECIFICATION",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )

    @dataclass(kw_only=True)
    class SpecRelationGroups:
        relation_group: list[RelationGroup] = field(
            default_factory=list,
            metadata={
                "name": "RELATION-GROUP",
                "type": "Element",
                "namespace": "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            },
        )


@dataclass(kw_only=True)
class ReqIf:
    class Meta:
        name = "REQ-IF"
        namespace = "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"

    the_header: ReqIf.TheHeader = field(
        metadata={
            "name": "THE-HEADER",
            "type": "Element",
            "required": True,
        }
    )
    core_content: ReqIf.CoreContent = field(
        metadata={
            "name": "CORE-CONTENT",
            "type": "Element",
            "required": True,
        }
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

    @dataclass(kw_only=True)
    class TheHeader:
        req_if_header: None | ReqIfHeader = field(
            default=None,
            metadata={
                "name": "REQ-IF-HEADER",
                "type": "Element",
            },
        )

    @dataclass(kw_only=True)
    class CoreContent:
        req_if_content: None | ReqIfContent = field(
            default=None,
            metadata={
                "name": "REQ-IF-CONTENT",
                "type": "Element",
            },
        )

    @dataclass(kw_only=True)
    class ToolExtensions:
        req_if_tool_extension: list[ReqIfToolExtension] = field(
            default_factory=list,
            metadata={
                "name": "REQ-IF-TOOL-EXTENSION",
                "type": "Element",
            },
        )
