from decimal import Decimal
from dataclasses import dataclass, field
from typing import List, Optional
from reqif.models.w3_org_1999_xhtml import (
    XhtmlDivType,
    XhtmlPType,
)

__NAMESPACE__ = "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"


@dataclass
class AlternativeId:
    """
    :ivar identifier:
    """
    class Meta:
        name = "ALTERNATIVE-ID"

    identifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="IDENTIFIER",
            type="Attribute",
            required=True
        )
    )


@dataclass
class AttributeValueBoolean:
    """
    :ivar definition:
    :ivar the_value:
    """
    class Meta:
        name = "ATTRIBUTE-VALUE-BOOLEAN"

    definition: Optional["AttributeValueBoolean.Definition"] = field(
        default=None,
        metadata=dict(
            name="DEFINITION",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            required=True
        )
    )
    the_value: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="THE-VALUE",
            type="Attribute",
            required=True
        )
    )

    @dataclass
    class Definition:
        """
        :ivar attribute_definition_boolean_ref:
        """
        attribute_definition_boolean_ref: Optional[str] = field(
            default=None,
            metadata=dict(
                name="ATTRIBUTE-DEFINITION-BOOLEAN-REF",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
            )
        )


@dataclass
class AttributeValueDate:
    """
    :ivar definition:
    :ivar the_value:
    """
    class Meta:
        name = "ATTRIBUTE-VALUE-DATE"

    definition: Optional["AttributeValueDate.Definition"] = field(
        default=None,
        metadata=dict(
            name="DEFINITION",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            required=True
        )
    )
    the_value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="THE-VALUE",
            type="Attribute",
            required=True
        )
    )

    @dataclass
    class Definition:
        """
        :ivar attribute_definition_date_ref:
        """
        attribute_definition_date_ref: Optional[str] = field(
            default=None,
            metadata=dict(
                name="ATTRIBUTE-DEFINITION-DATE-REF",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
            )
        )


@dataclass
class AttributeValueEnumeration:
    """
    :ivar definition:
    :ivar values:
    """
    class Meta:
        name = "ATTRIBUTE-VALUE-ENUMERATION"

    definition: Optional["AttributeValueEnumeration.Definition"] = field(
        default=None,
        metadata=dict(
            name="DEFINITION",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            required=True
        )
    )
    values: Optional["AttributeValueEnumeration.Values"] = field(
        default=None,
        metadata=dict(
            name="VALUES",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
        )
    )

    @dataclass
    class Definition:
        """
        :ivar attribute_definition_enumeration_ref:
        """
        attribute_definition_enumeration_ref: Optional[str] = field(
            default=None,
            metadata=dict(
                name="ATTRIBUTE-DEFINITION-ENUMERATION-REF",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
            )
        )

    @dataclass
    class Values:
        """
        :ivar enum_value_ref:
        """
        enum_value_ref: List[str] = field(
            default_factory=list,
            metadata=dict(
                name="ENUM-VALUE-REF",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )


@dataclass
class AttributeValueInteger:
    """
    :ivar definition:
    :ivar the_value:
    """
    class Meta:
        name = "ATTRIBUTE-VALUE-INTEGER"

    definition: Optional["AttributeValueInteger.Definition"] = field(
        default=None,
        metadata=dict(
            name="DEFINITION",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            required=True
        )
    )
    the_value: Optional[int] = field(
        default=None,
        metadata=dict(
            name="THE-VALUE",
            type="Attribute",
            required=True
        )
    )

    @dataclass
    class Definition:
        """
        :ivar attribute_definition_integer_ref:
        """
        attribute_definition_integer_ref: Optional[str] = field(
            default=None,
            metadata=dict(
                name="ATTRIBUTE-DEFINITION-INTEGER-REF",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
            )
        )


@dataclass
class AttributeValueReal:
    """
    :ivar definition:
    :ivar the_value:
    """
    class Meta:
        name = "ATTRIBUTE-VALUE-REAL"

    definition: Optional["AttributeValueReal.Definition"] = field(
        default=None,
        metadata=dict(
            name="DEFINITION",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            required=True
        )
    )
    the_value: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            name="THE-VALUE",
            type="Attribute",
            required=True
        )
    )

    @dataclass
    class Definition:
        """
        :ivar attribute_definition_real_ref:
        """
        attribute_definition_real_ref: Optional[str] = field(
            default=None,
            metadata=dict(
                name="ATTRIBUTE-DEFINITION-REAL-REF",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
            )
        )


@dataclass
class AttributeValueString:
    """
    :ivar definition:
    :ivar the_value:
    """
    class Meta:
        name = "ATTRIBUTE-VALUE-STRING"

    definition: Optional["AttributeValueString.Definition"] = field(
        default=None,
        metadata=dict(
            name="DEFINITION",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            required=True
        )
    )
    the_value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="THE-VALUE",
            type="Attribute",
            required=True
        )
    )

    @dataclass
    class Definition:
        """
        :ivar attribute_definition_string_ref:
        """
        attribute_definition_string_ref: Optional[str] = field(
            default=None,
            metadata=dict(
                name="ATTRIBUTE-DEFINITION-STRING-REF",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
            )
        )


@dataclass
class EmbeddedValue:
    """
    :ivar key:
    :ivar other_content:
    """
    class Meta:
        name = "EMBEDDED-VALUE"

    key: Optional[int] = field(
        default=None,
        metadata=dict(
            name="KEY",
            type="Attribute",
            required=True
        )
    )
    other_content: Optional[str] = field(
        default=None,
        metadata=dict(
            name="OTHER-CONTENT",
            type="Attribute",
            required=True
        )
    )


@dataclass
class ReqIfHeader:
    """
    :ivar comment:
    :ivar creation_time:
    :ivar repository_id:
    :ivar req_if_tool_id:
    :ivar req_if_version:
    :ivar source_tool_id:
    :ivar title:
    :ivar identifier:
    """
    class Meta:
        name = "REQ-IF-HEADER"

    comment: Optional[str] = field(
        default=None,
        metadata=dict(
            name="COMMENT",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
        )
    )
    creation_time: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CREATION-TIME",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            required=True
        )
    )
    repository_id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="REPOSITORY-ID",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
        )
    )
    req_if_tool_id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="REQ-IF-TOOL-ID",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            required=True
        )
    )
    req_if_version: str = field(
        init=False,
        default="1.0",
        metadata=dict(
            name="REQ-IF-VERSION",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            required=True
        )
    )
    source_tool_id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="SOURCE-TOOL-ID",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            required=True
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TITLE",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            required=True
        )
    )
    identifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="IDENTIFIER",
            type="Attribute",
            required=True
        )
    )


@dataclass
class ReqIfToolExtension:
    """
    :ivar other_element:
    """
    class Meta:
        name = "REQ-IF-TOOL-EXTENSION"

    other_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##other",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class AttributeDefinitionBoolean:
    """
    :ivar alternative_id:
    :ivar default_value:
    :ivar type:
    :ivar desc:
    :ivar identifier:
    :ivar is_editable:
    :ivar last_change:
    :ivar long_name:
    """
    class Meta:
        name = "ATTRIBUTE-DEFINITION-BOOLEAN"

    alternative_id: Optional["AttributeDefinitionBoolean.AlternativeId"] = field(
        default=None,
        metadata=dict(
            name="ALTERNATIVE-ID",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
        )
    )
    default_value: Optional["AttributeDefinitionBoolean.DefaultValue"] = field(
        default=None,
        metadata=dict(
            name="DEFAULT-VALUE",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
        )
    )
    type: Optional["AttributeDefinitionBoolean.Type"] = field(
        default=None,
        metadata=dict(
            name="TYPE",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            required=True
        )
    )
    desc: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DESC",
            type="Attribute"
        )
    )
    identifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="IDENTIFIER",
            type="Attribute",
            required=True
        )
    )
    is_editable: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="IS-EDITABLE",
            type="Attribute"
        )
    )
    last_change: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LAST-CHANGE",
            type="Attribute",
            required=True
        )
    )
    long_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LONG-NAME",
            type="Attribute"
        )
    )

    @dataclass
    class AlternativeId:
        """
        :ivar alternative_id:
        """
        alternative_id: Optional[AlternativeId] = field(
            default=None,
            metadata=dict(
                name="ALTERNATIVE-ID",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
            )
        )

    @dataclass
    class DefaultValue:
        """
        :ivar attribute_value_boolean:
        """
        attribute_value_boolean: Optional[AttributeValueBoolean] = field(
            default=None,
            metadata=dict(
                name="ATTRIBUTE-VALUE-BOOLEAN",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
            )
        )

    @dataclass
    class Type:
        """
        :ivar datatype_definition_boolean_ref:
        """
        datatype_definition_boolean_ref: Optional[str] = field(
            default=None,
            metadata=dict(
                name="DATATYPE-DEFINITION-BOOLEAN-REF",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
            )
        )


@dataclass
class AttributeDefinitionDate:
    """
    :ivar alternative_id:
    :ivar default_value:
    :ivar type:
    :ivar desc:
    :ivar identifier:
    :ivar is_editable:
    :ivar last_change:
    :ivar long_name:
    """
    class Meta:
        name = "ATTRIBUTE-DEFINITION-DATE"

    alternative_id: Optional["AttributeDefinitionDate.AlternativeId"] = field(
        default=None,
        metadata=dict(
            name="ALTERNATIVE-ID",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
        )
    )
    default_value: Optional["AttributeDefinitionDate.DefaultValue"] = field(
        default=None,
        metadata=dict(
            name="DEFAULT-VALUE",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
        )
    )
    type: Optional["AttributeDefinitionDate.Type"] = field(
        default=None,
        metadata=dict(
            name="TYPE",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            required=True
        )
    )
    desc: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DESC",
            type="Attribute"
        )
    )
    identifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="IDENTIFIER",
            type="Attribute",
            required=True
        )
    )
    is_editable: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="IS-EDITABLE",
            type="Attribute"
        )
    )
    last_change: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LAST-CHANGE",
            type="Attribute",
            required=True
        )
    )
    long_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LONG-NAME",
            type="Attribute"
        )
    )

    @dataclass
    class AlternativeId:
        """
        :ivar alternative_id:
        """
        alternative_id: Optional[AlternativeId] = field(
            default=None,
            metadata=dict(
                name="ALTERNATIVE-ID",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
            )
        )

    @dataclass
    class DefaultValue:
        """
        :ivar attribute_value_date:
        """
        attribute_value_date: Optional[AttributeValueDate] = field(
            default=None,
            metadata=dict(
                name="ATTRIBUTE-VALUE-DATE",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
            )
        )

    @dataclass
    class Type:
        """
        :ivar datatype_definition_date_ref:
        """
        datatype_definition_date_ref: Optional[str] = field(
            default=None,
            metadata=dict(
                name="DATATYPE-DEFINITION-DATE-REF",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
            )
        )


@dataclass
class AttributeDefinitionEnumeration:
    """
    :ivar default_value:
    :ivar alternative_id:
    :ivar type:
    :ivar desc:
    :ivar identifier:
    :ivar is_editable:
    :ivar last_change:
    :ivar long_name:
    :ivar multi_valued:
    """
    class Meta:
        name = "ATTRIBUTE-DEFINITION-ENUMERATION"

    default_value: Optional["AttributeDefinitionEnumeration.DefaultValue"] = field(
        default=None,
        metadata=dict(
            name="DEFAULT-VALUE",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
        )
    )
    alternative_id: Optional["AttributeDefinitionEnumeration.AlternativeId"] = field(
        default=None,
        metadata=dict(
            name="ALTERNATIVE-ID",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
        )
    )
    type: Optional["AttributeDefinitionEnumeration.Type"] = field(
        default=None,
        metadata=dict(
            name="TYPE",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            required=True
        )
    )
    desc: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DESC",
            type="Attribute"
        )
    )
    identifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="IDENTIFIER",
            type="Attribute",
            required=True
        )
    )
    is_editable: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="IS-EDITABLE",
            type="Attribute"
        )
    )
    last_change: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LAST-CHANGE",
            type="Attribute",
            required=True
        )
    )
    long_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LONG-NAME",
            type="Attribute"
        )
    )
    multi_valued: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="MULTI-VALUED",
            type="Attribute",
            required=True
        )
    )

    @dataclass
    class DefaultValue:
        """
        :ivar attribute_value_enumeration:
        """
        attribute_value_enumeration: Optional[AttributeValueEnumeration] = field(
            default=None,
            metadata=dict(
                name="ATTRIBUTE-VALUE-ENUMERATION",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
            )
        )

    @dataclass
    class AlternativeId:
        """
        :ivar alternative_id:
        """
        alternative_id: Optional[AlternativeId] = field(
            default=None,
            metadata=dict(
                name="ALTERNATIVE-ID",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
            )
        )

    @dataclass
    class Type:
        """
        :ivar datatype_definition_enumeration_ref:
        """
        datatype_definition_enumeration_ref: Optional[str] = field(
            default=None,
            metadata=dict(
                name="DATATYPE-DEFINITION-ENUMERATION-REF",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
            )
        )


@dataclass
class AttributeDefinitionInteger:
    """
    :ivar alternative_id:
    :ivar default_value:
    :ivar type:
    :ivar desc:
    :ivar identifier:
    :ivar is_editable:
    :ivar last_change:
    :ivar long_name:
    """
    class Meta:
        name = "ATTRIBUTE-DEFINITION-INTEGER"

    alternative_id: Optional["AttributeDefinitionInteger.AlternativeId"] = field(
        default=None,
        metadata=dict(
            name="ALTERNATIVE-ID",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
        )
    )
    default_value: Optional["AttributeDefinitionInteger.DefaultValue"] = field(
        default=None,
        metadata=dict(
            name="DEFAULT-VALUE",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
        )
    )
    type: Optional["AttributeDefinitionInteger.Type"] = field(
        default=None,
        metadata=dict(
            name="TYPE",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            required=True
        )
    )
    desc: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DESC",
            type="Attribute"
        )
    )
    identifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="IDENTIFIER",
            type="Attribute",
            required=True
        )
    )
    is_editable: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="IS-EDITABLE",
            type="Attribute"
        )
    )
    last_change: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LAST-CHANGE",
            type="Attribute",
            required=True
        )
    )
    long_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LONG-NAME",
            type="Attribute"
        )
    )

    @dataclass
    class AlternativeId:
        """
        :ivar alternative_id:
        """
        alternative_id: Optional[AlternativeId] = field(
            default=None,
            metadata=dict(
                name="ALTERNATIVE-ID",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
            )
        )

    @dataclass
    class DefaultValue:
        """
        :ivar attribute_value_integer:
        """
        attribute_value_integer: Optional[AttributeValueInteger] = field(
            default=None,
            metadata=dict(
                name="ATTRIBUTE-VALUE-INTEGER",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
            )
        )

    @dataclass
    class Type:
        """
        :ivar datatype_definition_integer_ref:
        """
        datatype_definition_integer_ref: Optional[str] = field(
            default=None,
            metadata=dict(
                name="DATATYPE-DEFINITION-INTEGER-REF",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
            )
        )


@dataclass
class AttributeDefinitionReal:
    """
    :ivar alternative_id:
    :ivar default_value:
    :ivar type:
    :ivar desc:
    :ivar identifier:
    :ivar is_editable:
    :ivar last_change:
    :ivar long_name:
    """
    class Meta:
        name = "ATTRIBUTE-DEFINITION-REAL"

    alternative_id: Optional["AttributeDefinitionReal.AlternativeId"] = field(
        default=None,
        metadata=dict(
            name="ALTERNATIVE-ID",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
        )
    )
    default_value: Optional["AttributeDefinitionReal.DefaultValue"] = field(
        default=None,
        metadata=dict(
            name="DEFAULT-VALUE",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
        )
    )
    type: Optional["AttributeDefinitionReal.Type"] = field(
        default=None,
        metadata=dict(
            name="TYPE",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            required=True
        )
    )
    desc: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DESC",
            type="Attribute"
        )
    )
    identifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="IDENTIFIER",
            type="Attribute",
            required=True
        )
    )
    is_editable: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="IS-EDITABLE",
            type="Attribute"
        )
    )
    last_change: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LAST-CHANGE",
            type="Attribute",
            required=True
        )
    )
    long_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LONG-NAME",
            type="Attribute"
        )
    )

    @dataclass
    class AlternativeId:
        """
        :ivar alternative_id:
        """
        alternative_id: Optional[AlternativeId] = field(
            default=None,
            metadata=dict(
                name="ALTERNATIVE-ID",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
            )
        )

    @dataclass
    class DefaultValue:
        """
        :ivar attribute_value_real:
        """
        attribute_value_real: Optional[AttributeValueReal] = field(
            default=None,
            metadata=dict(
                name="ATTRIBUTE-VALUE-REAL",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
            )
        )

    @dataclass
    class Type:
        """
        :ivar datatype_definition_real_ref:
        """
        datatype_definition_real_ref: Optional[str] = field(
            default=None,
            metadata=dict(
                name="DATATYPE-DEFINITION-REAL-REF",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
            )
        )


@dataclass
class AttributeDefinitionString:
    """
    :ivar alternative_id:
    :ivar default_value:
    :ivar type:
    :ivar desc:
    :ivar identifier:
    :ivar is_editable:
    :ivar last_change:
    :ivar long_name:
    """
    class Meta:
        name = "ATTRIBUTE-DEFINITION-STRING"

    alternative_id: Optional["AttributeDefinitionString.AlternativeId"] = field(
        default=None,
        metadata=dict(
            name="ALTERNATIVE-ID",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
        )
    )
    default_value: Optional["AttributeDefinitionString.DefaultValue"] = field(
        default=None,
        metadata=dict(
            name="DEFAULT-VALUE",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
        )
    )
    type: Optional["AttributeDefinitionString.Type"] = field(
        default=None,
        metadata=dict(
            name="TYPE",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            required=True
        )
    )
    desc: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DESC",
            type="Attribute"
        )
    )
    identifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="IDENTIFIER",
            type="Attribute",
            required=True
        )
    )
    is_editable: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="IS-EDITABLE",
            type="Attribute"
        )
    )
    last_change: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LAST-CHANGE",
            type="Attribute",
            required=True
        )
    )
    long_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LONG-NAME",
            type="Attribute"
        )
    )

    @dataclass
    class AlternativeId:
        """
        :ivar alternative_id:
        """
        alternative_id: Optional[AlternativeId] = field(
            default=None,
            metadata=dict(
                name="ALTERNATIVE-ID",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
            )
        )

    @dataclass
    class DefaultValue:
        """
        :ivar attribute_value_string:
        """
        attribute_value_string: Optional[AttributeValueString] = field(
            default=None,
            metadata=dict(
                name="ATTRIBUTE-VALUE-STRING",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
            )
        )

    @dataclass
    class Type:
        """
        :ivar datatype_definition_string_ref:
        """
        datatype_definition_string_ref: Optional[str] = field(
            default=None,
            metadata=dict(
                name="DATATYPE-DEFINITION-STRING-REF",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
            )
        )


@dataclass
class DatatypeDefinitionBoolean:
    """
    :ivar alternative_id:
    :ivar desc:
    :ivar identifier:
    :ivar last_change:
    :ivar long_name:
    """
    class Meta:
        name = "DATATYPE-DEFINITION-BOOLEAN"

    alternative_id: Optional["DatatypeDefinitionBoolean.AlternativeId"] = field(
        default=None,
        metadata=dict(
            name="ALTERNATIVE-ID",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
        )
    )
    desc: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DESC",
            type="Attribute"
        )
    )
    identifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="IDENTIFIER",
            type="Attribute",
            required=True
        )
    )
    last_change: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LAST-CHANGE",
            type="Attribute",
            required=True
        )
    )
    long_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LONG-NAME",
            type="Attribute"
        )
    )

    @dataclass
    class AlternativeId:
        """
        :ivar alternative_id:
        """
        alternative_id: Optional[AlternativeId] = field(
            default=None,
            metadata=dict(
                name="ALTERNATIVE-ID",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
            )
        )


@dataclass
class DatatypeDefinitionDate:
    """
    :ivar alternative_id:
    :ivar desc:
    :ivar identifier:
    :ivar last_change:
    :ivar long_name:
    """
    class Meta:
        name = "DATATYPE-DEFINITION-DATE"

    alternative_id: Optional["DatatypeDefinitionDate.AlternativeId"] = field(
        default=None,
        metadata=dict(
            name="ALTERNATIVE-ID",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
        )
    )
    desc: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DESC",
            type="Attribute"
        )
    )
    identifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="IDENTIFIER",
            type="Attribute",
            required=True
        )
    )
    last_change: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LAST-CHANGE",
            type="Attribute",
            required=True
        )
    )
    long_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LONG-NAME",
            type="Attribute"
        )
    )

    @dataclass
    class AlternativeId:
        """
        :ivar alternative_id:
        """
        alternative_id: Optional[AlternativeId] = field(
            default=None,
            metadata=dict(
                name="ALTERNATIVE-ID",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
            )
        )


@dataclass
class DatatypeDefinitionInteger:
    """
    :ivar alternative_id:
    :ivar desc:
    :ivar identifier:
    :ivar last_change:
    :ivar long_name:
    :ivar max:
    :ivar min:
    """
    class Meta:
        name = "DATATYPE-DEFINITION-INTEGER"

    alternative_id: Optional["DatatypeDefinitionInteger.AlternativeId"] = field(
        default=None,
        metadata=dict(
            name="ALTERNATIVE-ID",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
        )
    )
    desc: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DESC",
            type="Attribute"
        )
    )
    identifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="IDENTIFIER",
            type="Attribute",
            required=True
        )
    )
    last_change: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LAST-CHANGE",
            type="Attribute",
            required=True
        )
    )
    long_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LONG-NAME",
            type="Attribute"
        )
    )
    max: Optional[int] = field(
        default=None,
        metadata=dict(
            name="MAX",
            type="Attribute",
            required=True
        )
    )
    min: Optional[int] = field(
        default=None,
        metadata=dict(
            name="MIN",
            type="Attribute",
            required=True
        )
    )

    @dataclass
    class AlternativeId:
        """
        :ivar alternative_id:
        """
        alternative_id: Optional[AlternativeId] = field(
            default=None,
            metadata=dict(
                name="ALTERNATIVE-ID",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
            )
        )


@dataclass
class DatatypeDefinitionReal:
    """
    :ivar alternative_id:
    :ivar accuracy:
    :ivar desc:
    :ivar identifier:
    :ivar last_change:
    :ivar long_name:
    :ivar max:
    :ivar min:
    """
    class Meta:
        name = "DATATYPE-DEFINITION-REAL"

    alternative_id: Optional["DatatypeDefinitionReal.AlternativeId"] = field(
        default=None,
        metadata=dict(
            name="ALTERNATIVE-ID",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
        )
    )
    accuracy: Optional[int] = field(
        default=None,
        metadata=dict(
            name="ACCURACY",
            type="Attribute",
            required=True
        )
    )
    desc: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DESC",
            type="Attribute"
        )
    )
    identifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="IDENTIFIER",
            type="Attribute",
            required=True
        )
    )
    last_change: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LAST-CHANGE",
            type="Attribute",
            required=True
        )
    )
    long_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LONG-NAME",
            type="Attribute"
        )
    )
    max: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            name="MAX",
            type="Attribute",
            required=True
        )
    )
    min: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            name="MIN",
            type="Attribute",
            required=True
        )
    )

    @dataclass
    class AlternativeId:
        """
        :ivar alternative_id:
        """
        alternative_id: Optional[AlternativeId] = field(
            default=None,
            metadata=dict(
                name="ALTERNATIVE-ID",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
            )
        )


@dataclass
class DatatypeDefinitionString:
    """
    :ivar alternative_id:
    :ivar desc:
    :ivar identifier:
    :ivar last_change:
    :ivar long_name:
    :ivar max_length:
    """
    class Meta:
        name = "DATATYPE-DEFINITION-STRING"

    alternative_id: Optional["DatatypeDefinitionString.AlternativeId"] = field(
        default=None,
        metadata=dict(
            name="ALTERNATIVE-ID",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
        )
    )
    desc: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DESC",
            type="Attribute"
        )
    )
    identifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="IDENTIFIER",
            type="Attribute",
            required=True
        )
    )
    last_change: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LAST-CHANGE",
            type="Attribute",
            required=True
        )
    )
    long_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LONG-NAME",
            type="Attribute"
        )
    )
    max_length: Optional[int] = field(
        default=None,
        metadata=dict(
            name="MAX-LENGTH",
            type="Attribute",
            required=True
        )
    )

    @dataclass
    class AlternativeId:
        """
        :ivar alternative_id:
        """
        alternative_id: Optional[AlternativeId] = field(
            default=None,
            metadata=dict(
                name="ALTERNATIVE-ID",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
            )
        )


@dataclass
class DatatypeDefinitionXhtml:
    """
    :ivar alternative_id:
    :ivar desc:
    :ivar identifier:
    :ivar last_change:
    :ivar long_name:
    """
    class Meta:
        name = "DATATYPE-DEFINITION-XHTML"

    alternative_id: Optional["DatatypeDefinitionXhtml.AlternativeId"] = field(
        default=None,
        metadata=dict(
            name="ALTERNATIVE-ID",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
        )
    )
    desc: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DESC",
            type="Attribute"
        )
    )
    identifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="IDENTIFIER",
            type="Attribute",
            required=True
        )
    )
    last_change: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LAST-CHANGE",
            type="Attribute",
            required=True
        )
    )
    long_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LONG-NAME",
            type="Attribute"
        )
    )

    @dataclass
    class AlternativeId:
        """
        :ivar alternative_id:
        """
        alternative_id: Optional[AlternativeId] = field(
            default=None,
            metadata=dict(
                name="ALTERNATIVE-ID",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
            )
        )


@dataclass
class EnumValue:
    """
    :ivar alternative_id:
    :ivar properties:
    :ivar desc:
    :ivar identifier:
    :ivar last_change:
    :ivar long_name:
    """
    class Meta:
        name = "ENUM-VALUE"

    alternative_id: Optional["EnumValue.AlternativeId"] = field(
        default=None,
        metadata=dict(
            name="ALTERNATIVE-ID",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
        )
    )
    properties: Optional["EnumValue.Properties"] = field(
        default=None,
        metadata=dict(
            name="PROPERTIES",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            required=True
        )
    )
    desc: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DESC",
            type="Attribute"
        )
    )
    identifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="IDENTIFIER",
            type="Attribute",
            required=True
        )
    )
    last_change: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LAST-CHANGE",
            type="Attribute",
            required=True
        )
    )
    long_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LONG-NAME",
            type="Attribute"
        )
    )

    @dataclass
    class AlternativeId:
        """
        :ivar alternative_id:
        """
        alternative_id: Optional[AlternativeId] = field(
            default=None,
            metadata=dict(
                name="ALTERNATIVE-ID",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
            )
        )

    @dataclass
    class Properties:
        """
        :ivar embedded_value:
        """
        embedded_value: Optional[EmbeddedValue] = field(
            default=None,
            metadata=dict(
                name="EMBEDDED-VALUE",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
            )
        )


@dataclass
class RelationGroup:
    """
    :ivar alternative_id:
    :ivar source_specification:
    :ivar spec_relations:
    :ivar target_specification:
    :ivar type:
    :ivar desc:
    :ivar identifier:
    :ivar last_change:
    :ivar long_name:
    """
    class Meta:
        name = "RELATION-GROUP"

    alternative_id: Optional["RelationGroup.AlternativeId"] = field(
        default=None,
        metadata=dict(
            name="ALTERNATIVE-ID",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
        )
    )
    source_specification: Optional["RelationGroup.SourceSpecification"] = field(
        default=None,
        metadata=dict(
            name="SOURCE-SPECIFICATION",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            required=True
        )
    )
    spec_relations: Optional["RelationGroup.SpecRelations"] = field(
        default=None,
        metadata=dict(
            name="SPEC-RELATIONS",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
        )
    )
    target_specification: Optional["RelationGroup.TargetSpecification"] = field(
        default=None,
        metadata=dict(
            name="TARGET-SPECIFICATION",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            required=True
        )
    )
    type: Optional["RelationGroup.Type"] = field(
        default=None,
        metadata=dict(
            name="TYPE",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            required=True
        )
    )
    desc: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DESC",
            type="Attribute"
        )
    )
    identifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="IDENTIFIER",
            type="Attribute",
            required=True
        )
    )
    last_change: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LAST-CHANGE",
            type="Attribute",
            required=True
        )
    )
    long_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LONG-NAME",
            type="Attribute"
        )
    )

    @dataclass
    class AlternativeId:
        """
        :ivar alternative_id:
        """
        alternative_id: Optional[AlternativeId] = field(
            default=None,
            metadata=dict(
                name="ALTERNATIVE-ID",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
            )
        )

    @dataclass
    class SourceSpecification:
        """
        :ivar specification_ref:
        """
        specification_ref: Optional[str] = field(
            default=None,
            metadata=dict(
                name="SPECIFICATION-REF",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
            )
        )

    @dataclass
    class SpecRelations:
        """
        :ivar spec_relation_ref:
        """
        spec_relation_ref: List[str] = field(
            default_factory=list,
            metadata=dict(
                name="SPEC-RELATION-REF",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )

    @dataclass
    class TargetSpecification:
        """
        :ivar specification_ref:
        """
        specification_ref: Optional[str] = field(
            default=None,
            metadata=dict(
                name="SPECIFICATION-REF",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
            )
        )

    @dataclass
    class Type:
        """
        :ivar relation_group_type_ref:
        """
        relation_group_type_ref: Optional[str] = field(
            default=None,
            metadata=dict(
                name="RELATION-GROUP-TYPE-REF",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
            )
        )


@dataclass
class SpecHierarchy:
    """
    :ivar alternative_id:
    :ivar children:
    :ivar editable_atts:
    :ivar object:
    :ivar desc:
    :ivar identifier:
    :ivar is_editable:
    :ivar is_table_internal:
    :ivar last_change:
    :ivar long_name:
    """
    class Meta:
        name = "SPEC-HIERARCHY"

    alternative_id: Optional["SpecHierarchy.AlternativeId"] = field(
        default=None,
        metadata=dict(
            name="ALTERNATIVE-ID",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
        )
    )
    children: Optional["SpecHierarchy.Children"] = field(
        default=None,
        metadata=dict(
            name="CHILDREN",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
        )
    )
    editable_atts: Optional["SpecHierarchy.EditableAtts"] = field(
        default=None,
        metadata=dict(
            name="EDITABLE-ATTS",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
        )
    )
    object: Optional["SpecHierarchy.Object"] = field(
        default=None,
        metadata=dict(
            name="OBJECT",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            required=True
        )
    )
    desc: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DESC",
            type="Attribute"
        )
    )
    identifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="IDENTIFIER",
            type="Attribute",
            required=True
        )
    )
    is_editable: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="IS-EDITABLE",
            type="Attribute"
        )
    )
    is_table_internal: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="IS-TABLE-INTERNAL",
            type="Attribute"
        )
    )
    last_change: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LAST-CHANGE",
            type="Attribute",
            required=True
        )
    )
    long_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LONG-NAME",
            type="Attribute"
        )
    )

    @dataclass
    class AlternativeId:
        """
        :ivar alternative_id:
        """
        alternative_id: Optional[AlternativeId] = field(
            default=None,
            metadata=dict(
                name="ALTERNATIVE-ID",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
            )
        )

    @dataclass
    class Children:
        """
        :ivar spec_hierarchy:
        """
        spec_hierarchy: List["SpecHierarchy"] = field(
            default_factory=list,
            metadata=dict(
                name="SPEC-HIERARCHY",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )

    @dataclass
    class EditableAtts:
        """
        :ivar attribute_definition_boolean_ref:
        :ivar attribute_definition_date_ref:
        :ivar attribute_definition_enumeration_ref:
        :ivar attribute_definition_integer_ref:
        :ivar attribute_definition_real_ref:
        :ivar attribute_definition_string_ref:
        :ivar attribute_definition_xhtml_ref:
        """
        attribute_definition_boolean_ref: List[str] = field(
            default_factory=list,
            metadata=dict(
                name="ATTRIBUTE-DEFINITION-BOOLEAN-REF",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        attribute_definition_date_ref: List[str] = field(
            default_factory=list,
            metadata=dict(
                name="ATTRIBUTE-DEFINITION-DATE-REF",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        attribute_definition_enumeration_ref: List[str] = field(
            default_factory=list,
            metadata=dict(
                name="ATTRIBUTE-DEFINITION-ENUMERATION-REF",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        attribute_definition_integer_ref: List[str] = field(
            default_factory=list,
            metadata=dict(
                name="ATTRIBUTE-DEFINITION-INTEGER-REF",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        attribute_definition_real_ref: List[str] = field(
            default_factory=list,
            metadata=dict(
                name="ATTRIBUTE-DEFINITION-REAL-REF",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        attribute_definition_string_ref: List[str] = field(
            default_factory=list,
            metadata=dict(
                name="ATTRIBUTE-DEFINITION-STRING-REF",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        attribute_definition_xhtml_ref: List[str] = field(
            default_factory=list,
            metadata=dict(
                name="ATTRIBUTE-DEFINITION-XHTML-REF",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )

    @dataclass
    class Object:
        """
        :ivar spec_object_ref:
        """
        spec_object_ref: Optional[str] = field(
            default=None,
            metadata=dict(
                name="SPEC-OBJECT-REF",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
            )
        )


@dataclass
class XhtmlContent:
    """
    :ivar p:
    :ivar div:
    """
    class Meta:
        name = "XHTML-CONTENT"

    p: Optional[XhtmlPType] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml"
        )
    )
    div: Optional[XhtmlDivType] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xhtml"
        )
    )


@dataclass
class AttributeValueXhtml:
    """
    :ivar the_value:
    :ivar the_original_value:
    :ivar definition:
    :ivar is_simplified:
    """
    class Meta:
        name = "ATTRIBUTE-VALUE-XHTML"

    the_value: Optional[XhtmlContent] = field(
        default=None,
        metadata=dict(
            name="THE-VALUE",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            required=True
        )
    )
    the_original_value: Optional[XhtmlContent] = field(
        default=None,
        metadata=dict(
            name="THE-ORIGINAL-VALUE",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
        )
    )
    definition: Optional["AttributeValueXhtml.Definition"] = field(
        default=None,
        metadata=dict(
            name="DEFINITION",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            required=True
        )
    )
    is_simplified: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="IS-SIMPLIFIED",
            type="Attribute"
        )
    )

    @dataclass
    class Definition:
        """
        :ivar attribute_definition_xhtml_ref:
        """
        attribute_definition_xhtml_ref: Optional[str] = field(
            default=None,
            metadata=dict(
                name="ATTRIBUTE-DEFINITION-XHTML-REF",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
            )
        )


@dataclass
class DatatypeDefinitionEnumeration:
    """
    :ivar alternative_id:
    :ivar specified_values:
    :ivar desc:
    :ivar identifier:
    :ivar last_change:
    :ivar long_name:
    """
    class Meta:
        name = "DATATYPE-DEFINITION-ENUMERATION"

    alternative_id: Optional["DatatypeDefinitionEnumeration.AlternativeId"] = field(
        default=None,
        metadata=dict(
            name="ALTERNATIVE-ID",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
        )
    )
    specified_values: Optional["DatatypeDefinitionEnumeration.SpecifiedValues"] = field(
        default=None,
        metadata=dict(
            name="SPECIFIED-VALUES",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
        )
    )
    desc: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DESC",
            type="Attribute"
        )
    )
    identifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="IDENTIFIER",
            type="Attribute",
            required=True
        )
    )
    last_change: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LAST-CHANGE",
            type="Attribute",
            required=True
        )
    )
    long_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LONG-NAME",
            type="Attribute"
        )
    )

    @dataclass
    class AlternativeId:
        """
        :ivar alternative_id:
        """
        alternative_id: Optional[AlternativeId] = field(
            default=None,
            metadata=dict(
                name="ALTERNATIVE-ID",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
            )
        )

    @dataclass
    class SpecifiedValues:
        """
        :ivar enum_value:
        """
        enum_value: List[EnumValue] = field(
            default_factory=list,
            metadata=dict(
                name="ENUM-VALUE",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )


@dataclass
class AttributeDefinitionXhtml:
    """
    :ivar alternative_id:
    :ivar default_value:
    :ivar type:
    :ivar desc:
    :ivar identifier:
    :ivar is_editable:
    :ivar last_change:
    :ivar long_name:
    """
    class Meta:
        name = "ATTRIBUTE-DEFINITION-XHTML"

    alternative_id: Optional["AttributeDefinitionXhtml.AlternativeId"] = field(
        default=None,
        metadata=dict(
            name="ALTERNATIVE-ID",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
        )
    )
    default_value: Optional["AttributeDefinitionXhtml.DefaultValue"] = field(
        default=None,
        metadata=dict(
            name="DEFAULT-VALUE",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
        )
    )
    type: Optional["AttributeDefinitionXhtml.Type"] = field(
        default=None,
        metadata=dict(
            name="TYPE",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            required=True
        )
    )
    desc: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DESC",
            type="Attribute"
        )
    )
    identifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="IDENTIFIER",
            type="Attribute",
            required=True
        )
    )
    is_editable: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="IS-EDITABLE",
            type="Attribute"
        )
    )
    last_change: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LAST-CHANGE",
            type="Attribute",
            required=True
        )
    )
    long_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LONG-NAME",
            type="Attribute"
        )
    )

    @dataclass
    class AlternativeId:
        """
        :ivar alternative_id:
        """
        alternative_id: Optional[AlternativeId] = field(
            default=None,
            metadata=dict(
                name="ALTERNATIVE-ID",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
            )
        )

    @dataclass
    class DefaultValue:
        """
        :ivar attribute_value_xhtml:
        """
        attribute_value_xhtml: Optional[AttributeValueXhtml] = field(
            default=None,
            metadata=dict(
                name="ATTRIBUTE-VALUE-XHTML",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
            )
        )

    @dataclass
    class Type:
        """
        :ivar datatype_definition_xhtml_ref:
        """
        datatype_definition_xhtml_ref: Optional[str] = field(
            default=None,
            metadata=dict(
                name="DATATYPE-DEFINITION-XHTML-REF",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
            )
        )


@dataclass
class SpecObject:
    """
    :ivar alternative_id:
    :ivar values:
    :ivar type:
    :ivar desc:
    :ivar identifier:
    :ivar last_change:
    :ivar long_name:
    """
    class Meta:
        name = "SPEC-OBJECT"

    alternative_id: Optional["SpecObject.AlternativeId"] = field(
        default=None,
        metadata=dict(
            name="ALTERNATIVE-ID",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
        )
    )
    values: Optional["SpecObject.Values"] = field(
        default=None,
        metadata=dict(
            name="VALUES",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
        )
    )
    type: Optional["SpecObject.Type"] = field(
        default=None,
        metadata=dict(
            name="TYPE",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            required=True
        )
    )
    desc: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DESC",
            type="Attribute"
        )
    )
    identifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="IDENTIFIER",
            type="Attribute",
            required=True
        )
    )
    last_change: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LAST-CHANGE",
            type="Attribute",
            required=True
        )
    )
    long_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LONG-NAME",
            type="Attribute"
        )
    )

    @dataclass
    class AlternativeId:
        """
        :ivar alternative_id:
        """
        alternative_id: Optional[AlternativeId] = field(
            default=None,
            metadata=dict(
                name="ALTERNATIVE-ID",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
            )
        )

    @dataclass
    class Values:
        """
        :ivar attribute_value_boolean:
        :ivar attribute_value_date:
        :ivar attribute_value_enumeration:
        :ivar attribute_value_integer:
        :ivar attribute_value_real:
        :ivar attribute_value_string:
        :ivar attribute_value_xhtml:
        """
        attribute_value_boolean: List[AttributeValueBoolean] = field(
            default_factory=list,
            metadata=dict(
                name="ATTRIBUTE-VALUE-BOOLEAN",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        attribute_value_date: List[AttributeValueDate] = field(
            default_factory=list,
            metadata=dict(
                name="ATTRIBUTE-VALUE-DATE",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        attribute_value_enumeration: List[AttributeValueEnumeration] = field(
            default_factory=list,
            metadata=dict(
                name="ATTRIBUTE-VALUE-ENUMERATION",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        attribute_value_integer: List[AttributeValueInteger] = field(
            default_factory=list,
            metadata=dict(
                name="ATTRIBUTE-VALUE-INTEGER",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        attribute_value_real: List[AttributeValueReal] = field(
            default_factory=list,
            metadata=dict(
                name="ATTRIBUTE-VALUE-REAL",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        attribute_value_string: List[AttributeValueString] = field(
            default_factory=list,
            metadata=dict(
                name="ATTRIBUTE-VALUE-STRING",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        attribute_value_xhtml: List[AttributeValueXhtml] = field(
            default_factory=list,
            metadata=dict(
                name="ATTRIBUTE-VALUE-XHTML",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )

    @dataclass
    class Type:
        """
        :ivar spec_object_type_ref:
        """
        spec_object_type_ref: Optional[str] = field(
            default=None,
            metadata=dict(
                name="SPEC-OBJECT-TYPE-REF",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
            )
        )


@dataclass
class SpecRelation:
    """
    :ivar alternative_id:
    :ivar values:
    :ivar source:
    :ivar target:
    :ivar type:
    :ivar desc:
    :ivar identifier:
    :ivar last_change:
    :ivar long_name:
    """
    class Meta:
        name = "SPEC-RELATION"

    alternative_id: Optional["SpecRelation.AlternativeId"] = field(
        default=None,
        metadata=dict(
            name="ALTERNATIVE-ID",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
        )
    )
    values: Optional["SpecRelation.Values"] = field(
        default=None,
        metadata=dict(
            name="VALUES",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
        )
    )
    source: Optional["SpecRelation.Source"] = field(
        default=None,
        metadata=dict(
            name="SOURCE",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            required=True
        )
    )
    target: Optional["SpecRelation.Target"] = field(
        default=None,
        metadata=dict(
            name="TARGET",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            required=True
        )
    )
    type: Optional["SpecRelation.Type"] = field(
        default=None,
        metadata=dict(
            name="TYPE",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            required=True
        )
    )
    desc: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DESC",
            type="Attribute"
        )
    )
    identifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="IDENTIFIER",
            type="Attribute",
            required=True
        )
    )
    last_change: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LAST-CHANGE",
            type="Attribute",
            required=True
        )
    )
    long_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LONG-NAME",
            type="Attribute"
        )
    )

    @dataclass
    class AlternativeId:
        """
        :ivar alternative_id:
        """
        alternative_id: Optional[AlternativeId] = field(
            default=None,
            metadata=dict(
                name="ALTERNATIVE-ID",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
            )
        )

    @dataclass
    class Values:
        """
        :ivar attribute_value_boolean:
        :ivar attribute_value_date:
        :ivar attribute_value_enumeration:
        :ivar attribute_value_integer:
        :ivar attribute_value_real:
        :ivar attribute_value_string:
        :ivar attribute_value_xhtml:
        """
        attribute_value_boolean: List[AttributeValueBoolean] = field(
            default_factory=list,
            metadata=dict(
                name="ATTRIBUTE-VALUE-BOOLEAN",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        attribute_value_date: List[AttributeValueDate] = field(
            default_factory=list,
            metadata=dict(
                name="ATTRIBUTE-VALUE-DATE",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        attribute_value_enumeration: List[AttributeValueEnumeration] = field(
            default_factory=list,
            metadata=dict(
                name="ATTRIBUTE-VALUE-ENUMERATION",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        attribute_value_integer: List[AttributeValueInteger] = field(
            default_factory=list,
            metadata=dict(
                name="ATTRIBUTE-VALUE-INTEGER",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        attribute_value_real: List[AttributeValueReal] = field(
            default_factory=list,
            metadata=dict(
                name="ATTRIBUTE-VALUE-REAL",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        attribute_value_string: List[AttributeValueString] = field(
            default_factory=list,
            metadata=dict(
                name="ATTRIBUTE-VALUE-STRING",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        attribute_value_xhtml: List[AttributeValueXhtml] = field(
            default_factory=list,
            metadata=dict(
                name="ATTRIBUTE-VALUE-XHTML",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )

    @dataclass
    class Source:
        """
        :ivar spec_object_ref:
        """
        spec_object_ref: Optional[str] = field(
            default=None,
            metadata=dict(
                name="SPEC-OBJECT-REF",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
            )
        )

    @dataclass
    class Target:
        """
        :ivar spec_object_ref:
        """
        spec_object_ref: Optional[str] = field(
            default=None,
            metadata=dict(
                name="SPEC-OBJECT-REF",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
            )
        )

    @dataclass
    class Type:
        """
        :ivar spec_relation_type_ref:
        """
        spec_relation_type_ref: Optional[str] = field(
            default=None,
            metadata=dict(
                name="SPEC-RELATION-TYPE-REF",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
            )
        )


@dataclass
class Specification:
    """
    :ivar alternative_id:
    :ivar values:
    :ivar children:
    :ivar type:
    :ivar desc:
    :ivar identifier:
    :ivar last_change:
    :ivar long_name:
    """
    class Meta:
        name = "SPECIFICATION"

    alternative_id: Optional["Specification.AlternativeId"] = field(
        default=None,
        metadata=dict(
            name="ALTERNATIVE-ID",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
        )
    )
    values: Optional["Specification.Values"] = field(
        default=None,
        metadata=dict(
            name="VALUES",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
        )
    )
    children: Optional["Specification.Children"] = field(
        default=None,
        metadata=dict(
            name="CHILDREN",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
        )
    )
    type: Optional["Specification.Type"] = field(
        default=None,
        metadata=dict(
            name="TYPE",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
            required=True
        )
    )
    desc: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DESC",
            type="Attribute"
        )
    )
    identifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="IDENTIFIER",
            type="Attribute",
            required=True
        )
    )
    last_change: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LAST-CHANGE",
            type="Attribute",
            required=True
        )
    )
    long_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LONG-NAME",
            type="Attribute"
        )
    )

    @dataclass
    class AlternativeId:
        """
        :ivar alternative_id:
        """
        alternative_id: Optional[AlternativeId] = field(
            default=None,
            metadata=dict(
                name="ALTERNATIVE-ID",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
            )
        )

    @dataclass
    class Values:
        """
        :ivar attribute_value_boolean:
        :ivar attribute_value_date:
        :ivar attribute_value_enumeration:
        :ivar attribute_value_integer:
        :ivar attribute_value_real:
        :ivar attribute_value_string:
        :ivar attribute_value_xhtml:
        """
        attribute_value_boolean: List[AttributeValueBoolean] = field(
            default_factory=list,
            metadata=dict(
                name="ATTRIBUTE-VALUE-BOOLEAN",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        attribute_value_date: List[AttributeValueDate] = field(
            default_factory=list,
            metadata=dict(
                name="ATTRIBUTE-VALUE-DATE",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        attribute_value_enumeration: List[AttributeValueEnumeration] = field(
            default_factory=list,
            metadata=dict(
                name="ATTRIBUTE-VALUE-ENUMERATION",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        attribute_value_integer: List[AttributeValueInteger] = field(
            default_factory=list,
            metadata=dict(
                name="ATTRIBUTE-VALUE-INTEGER",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        attribute_value_real: List[AttributeValueReal] = field(
            default_factory=list,
            metadata=dict(
                name="ATTRIBUTE-VALUE-REAL",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        attribute_value_string: List[AttributeValueString] = field(
            default_factory=list,
            metadata=dict(
                name="ATTRIBUTE-VALUE-STRING",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        attribute_value_xhtml: List[AttributeValueXhtml] = field(
            default_factory=list,
            metadata=dict(
                name="ATTRIBUTE-VALUE-XHTML",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )

    @dataclass
    class Children:
        """
        :ivar spec_hierarchy:
        """
        spec_hierarchy: List[SpecHierarchy] = field(
            default_factory=list,
            metadata=dict(
                name="SPEC-HIERARCHY",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )

    @dataclass
    class Type:
        """
        :ivar specification_type_ref:
        """
        specification_type_ref: Optional[str] = field(
            default=None,
            metadata=dict(
                name="SPECIFICATION-TYPE-REF",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
            )
        )


@dataclass
class RelationGroupType:
    """
    :ivar alternative_id:
    :ivar spec_attributes:
    :ivar desc:
    :ivar identifier:
    :ivar last_change:
    :ivar long_name:
    """
    class Meta:
        name = "RELATION-GROUP-TYPE"

    alternative_id: Optional["RelationGroupType.AlternativeId"] = field(
        default=None,
        metadata=dict(
            name="ALTERNATIVE-ID",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
        )
    )
    spec_attributes: Optional["RelationGroupType.SpecAttributes"] = field(
        default=None,
        metadata=dict(
            name="SPEC-ATTRIBUTES",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
        )
    )
    desc: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DESC",
            type="Attribute"
        )
    )
    identifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="IDENTIFIER",
            type="Attribute",
            required=True
        )
    )
    last_change: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LAST-CHANGE",
            type="Attribute",
            required=True
        )
    )
    long_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LONG-NAME",
            type="Attribute"
        )
    )

    @dataclass
    class AlternativeId:
        """
        :ivar alternative_id:
        """
        alternative_id: Optional[AlternativeId] = field(
            default=None,
            metadata=dict(
                name="ALTERNATIVE-ID",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
            )
        )

    @dataclass
    class SpecAttributes:
        """
        :ivar attribute_definition_boolean:
        :ivar attribute_definition_date:
        :ivar attribute_definition_enumeration:
        :ivar attribute_definition_integer:
        :ivar attribute_definition_real:
        :ivar attribute_definition_string:
        :ivar attribute_definition_xhtml:
        """
        attribute_definition_boolean: List[AttributeDefinitionBoolean] = field(
            default_factory=list,
            metadata=dict(
                name="ATTRIBUTE-DEFINITION-BOOLEAN",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        attribute_definition_date: List[AttributeDefinitionDate] = field(
            default_factory=list,
            metadata=dict(
                name="ATTRIBUTE-DEFINITION-DATE",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        attribute_definition_enumeration: List[AttributeDefinitionEnumeration] = field(
            default_factory=list,
            metadata=dict(
                name="ATTRIBUTE-DEFINITION-ENUMERATION",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        attribute_definition_integer: List[AttributeDefinitionInteger] = field(
            default_factory=list,
            metadata=dict(
                name="ATTRIBUTE-DEFINITION-INTEGER",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        attribute_definition_real: List[AttributeDefinitionReal] = field(
            default_factory=list,
            metadata=dict(
                name="ATTRIBUTE-DEFINITION-REAL",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        attribute_definition_string: List[AttributeDefinitionString] = field(
            default_factory=list,
            metadata=dict(
                name="ATTRIBUTE-DEFINITION-STRING",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        attribute_definition_xhtml: List[AttributeDefinitionXhtml] = field(
            default_factory=list,
            metadata=dict(
                name="ATTRIBUTE-DEFINITION-XHTML",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )


@dataclass
class SpecObjectType:
    """
    :ivar alternative_id:
    :ivar spec_attributes:
    :ivar desc:
    :ivar identifier:
    :ivar last_change:
    :ivar long_name:
    """
    class Meta:
        name = "SPEC-OBJECT-TYPE"

    alternative_id: Optional["SpecObjectType.AlternativeId"] = field(
        default=None,
        metadata=dict(
            name="ALTERNATIVE-ID",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
        )
    )
    spec_attributes: Optional["SpecObjectType.SpecAttributes"] = field(
        default=None,
        metadata=dict(
            name="SPEC-ATTRIBUTES",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
        )
    )
    desc: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DESC",
            type="Attribute"
        )
    )
    identifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="IDENTIFIER",
            type="Attribute",
            required=True
        )
    )
    last_change: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LAST-CHANGE",
            type="Attribute",
            required=True
        )
    )
    long_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LONG-NAME",
            type="Attribute"
        )
    )

    @dataclass
    class AlternativeId:
        """
        :ivar alternative_id:
        """
        alternative_id: Optional[AlternativeId] = field(
            default=None,
            metadata=dict(
                name="ALTERNATIVE-ID",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
            )
        )

    @dataclass
    class SpecAttributes:
        """
        :ivar attribute_definition_boolean:
        :ivar attribute_definition_date:
        :ivar attribute_definition_enumeration:
        :ivar attribute_definition_integer:
        :ivar attribute_definition_real:
        :ivar attribute_definition_string:
        :ivar attribute_definition_xhtml:
        """
        attribute_definition_boolean: List[AttributeDefinitionBoolean] = field(
            default_factory=list,
            metadata=dict(
                name="ATTRIBUTE-DEFINITION-BOOLEAN",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        attribute_definition_date: List[AttributeDefinitionDate] = field(
            default_factory=list,
            metadata=dict(
                name="ATTRIBUTE-DEFINITION-DATE",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        attribute_definition_enumeration: List[AttributeDefinitionEnumeration] = field(
            default_factory=list,
            metadata=dict(
                name="ATTRIBUTE-DEFINITION-ENUMERATION",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        attribute_definition_integer: List[AttributeDefinitionInteger] = field(
            default_factory=list,
            metadata=dict(
                name="ATTRIBUTE-DEFINITION-INTEGER",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        attribute_definition_real: List[AttributeDefinitionReal] = field(
            default_factory=list,
            metadata=dict(
                name="ATTRIBUTE-DEFINITION-REAL",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        attribute_definition_string: List[AttributeDefinitionString] = field(
            default_factory=list,
            metadata=dict(
                name="ATTRIBUTE-DEFINITION-STRING",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        attribute_definition_xhtml: List[AttributeDefinitionXhtml] = field(
            default_factory=list,
            metadata=dict(
                name="ATTRIBUTE-DEFINITION-XHTML",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )


@dataclass
class SpecRelationType:
    """
    :ivar alternative_id:
    :ivar spec_attributes:
    :ivar desc:
    :ivar identifier:
    :ivar last_change:
    :ivar long_name:
    """
    class Meta:
        name = "SPEC-RELATION-TYPE"

    alternative_id: Optional["SpecRelationType.AlternativeId"] = field(
        default=None,
        metadata=dict(
            name="ALTERNATIVE-ID",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
        )
    )
    spec_attributes: Optional["SpecRelationType.SpecAttributes"] = field(
        default=None,
        metadata=dict(
            name="SPEC-ATTRIBUTES",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
        )
    )
    desc: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DESC",
            type="Attribute"
        )
    )
    identifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="IDENTIFIER",
            type="Attribute",
            required=True
        )
    )
    last_change: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LAST-CHANGE",
            type="Attribute",
            required=True
        )
    )
    long_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LONG-NAME",
            type="Attribute"
        )
    )

    @dataclass
    class AlternativeId:
        """
        :ivar alternative_id:
        """
        alternative_id: Optional[AlternativeId] = field(
            default=None,
            metadata=dict(
                name="ALTERNATIVE-ID",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
            )
        )

    @dataclass
    class SpecAttributes:
        """
        :ivar attribute_definition_boolean:
        :ivar attribute_definition_date:
        :ivar attribute_definition_enumeration:
        :ivar attribute_definition_integer:
        :ivar attribute_definition_real:
        :ivar attribute_definition_string:
        :ivar attribute_definition_xhtml:
        """
        attribute_definition_boolean: List[AttributeDefinitionBoolean] = field(
            default_factory=list,
            metadata=dict(
                name="ATTRIBUTE-DEFINITION-BOOLEAN",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        attribute_definition_date: List[AttributeDefinitionDate] = field(
            default_factory=list,
            metadata=dict(
                name="ATTRIBUTE-DEFINITION-DATE",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        attribute_definition_enumeration: List[AttributeDefinitionEnumeration] = field(
            default_factory=list,
            metadata=dict(
                name="ATTRIBUTE-DEFINITION-ENUMERATION",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        attribute_definition_integer: List[AttributeDefinitionInteger] = field(
            default_factory=list,
            metadata=dict(
                name="ATTRIBUTE-DEFINITION-INTEGER",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        attribute_definition_real: List[AttributeDefinitionReal] = field(
            default_factory=list,
            metadata=dict(
                name="ATTRIBUTE-DEFINITION-REAL",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        attribute_definition_string: List[AttributeDefinitionString] = field(
            default_factory=list,
            metadata=dict(
                name="ATTRIBUTE-DEFINITION-STRING",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        attribute_definition_xhtml: List[AttributeDefinitionXhtml] = field(
            default_factory=list,
            metadata=dict(
                name="ATTRIBUTE-DEFINITION-XHTML",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )


@dataclass
class SpecificationType:
    """
    :ivar alternative_id:
    :ivar spec_attributes:
    :ivar desc:
    :ivar identifier:
    :ivar last_change:
    :ivar long_name:
    """
    class Meta:
        name = "SPECIFICATION-TYPE"

    alternative_id: Optional["SpecificationType.AlternativeId"] = field(
        default=None,
        metadata=dict(
            name="ALTERNATIVE-ID",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
        )
    )
    spec_attributes: Optional["SpecificationType.SpecAttributes"] = field(
        default=None,
        metadata=dict(
            name="SPEC-ATTRIBUTES",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
        )
    )
    desc: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DESC",
            type="Attribute"
        )
    )
    identifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="IDENTIFIER",
            type="Attribute",
            required=True
        )
    )
    last_change: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LAST-CHANGE",
            type="Attribute",
            required=True
        )
    )
    long_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LONG-NAME",
            type="Attribute"
        )
    )

    @dataclass
    class AlternativeId:
        """
        :ivar alternative_id:
        """
        alternative_id: Optional[AlternativeId] = field(
            default=None,
            metadata=dict(
                name="ALTERNATIVE-ID",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
            )
        )

    @dataclass
    class SpecAttributes:
        """
        :ivar attribute_definition_boolean:
        :ivar attribute_definition_date:
        :ivar attribute_definition_enumeration:
        :ivar attribute_definition_integer:
        :ivar attribute_definition_real:
        :ivar attribute_definition_string:
        :ivar attribute_definition_xhtml:
        """
        attribute_definition_boolean: List[AttributeDefinitionBoolean] = field(
            default_factory=list,
            metadata=dict(
                name="ATTRIBUTE-DEFINITION-BOOLEAN",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        attribute_definition_date: List[AttributeDefinitionDate] = field(
            default_factory=list,
            metadata=dict(
                name="ATTRIBUTE-DEFINITION-DATE",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        attribute_definition_enumeration: List[AttributeDefinitionEnumeration] = field(
            default_factory=list,
            metadata=dict(
                name="ATTRIBUTE-DEFINITION-ENUMERATION",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        attribute_definition_integer: List[AttributeDefinitionInteger] = field(
            default_factory=list,
            metadata=dict(
                name="ATTRIBUTE-DEFINITION-INTEGER",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        attribute_definition_real: List[AttributeDefinitionReal] = field(
            default_factory=list,
            metadata=dict(
                name="ATTRIBUTE-DEFINITION-REAL",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        attribute_definition_string: List[AttributeDefinitionString] = field(
            default_factory=list,
            metadata=dict(
                name="ATTRIBUTE-DEFINITION-STRING",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        attribute_definition_xhtml: List[AttributeDefinitionXhtml] = field(
            default_factory=list,
            metadata=dict(
                name="ATTRIBUTE-DEFINITION-XHTML",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )


@dataclass
class ReqIfContent:
    """
    :ivar datatypes:
    :ivar spec_types:
    :ivar spec_objects:
    :ivar spec_relations:
    :ivar specifications:
    :ivar spec_relation_groups:
    """
    class Meta:
        name = "REQ-IF-CONTENT"

    datatypes: Optional["ReqIfContent.Datatypes"] = field(
        default=None,
        metadata=dict(
            name="DATATYPES",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
        )
    )
    spec_types: Optional["ReqIfContent.SpecTypes"] = field(
        default=None,
        metadata=dict(
            name="SPEC-TYPES",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
        )
    )
    spec_objects: Optional["ReqIfContent.SpecObjects"] = field(
        default=None,
        metadata=dict(
            name="SPEC-OBJECTS",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
        )
    )
    spec_relations: Optional["ReqIfContent.SpecRelations"] = field(
        default=None,
        metadata=dict(
            name="SPEC-RELATIONS",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
        )
    )
    specifications: Optional["ReqIfContent.Specifications"] = field(
        default=None,
        metadata=dict(
            name="SPECIFICATIONS",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
        )
    )
    spec_relation_groups: Optional["ReqIfContent.SpecRelationGroups"] = field(
        default=None,
        metadata=dict(
            name="SPEC-RELATION-GROUPS",
            type="Element",
            namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"
        )
    )

    @dataclass
    class Datatypes:
        """
        :ivar datatype_definition_boolean:
        :ivar datatype_definition_date:
        :ivar datatype_definition_enumeration:
        :ivar datatype_definition_integer:
        :ivar datatype_definition_real:
        :ivar datatype_definition_string:
        :ivar datatype_definition_xhtml:
        """
        datatype_definition_boolean: List[DatatypeDefinitionBoolean] = field(
            default_factory=list,
            metadata=dict(
                name="DATATYPE-DEFINITION-BOOLEAN",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        datatype_definition_date: List[DatatypeDefinitionDate] = field(
            default_factory=list,
            metadata=dict(
                name="DATATYPE-DEFINITION-DATE",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        datatype_definition_enumeration: List[DatatypeDefinitionEnumeration] = field(
            default_factory=list,
            metadata=dict(
                name="DATATYPE-DEFINITION-ENUMERATION",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        datatype_definition_integer: List[DatatypeDefinitionInteger] = field(
            default_factory=list,
            metadata=dict(
                name="DATATYPE-DEFINITION-INTEGER",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        datatype_definition_real: List[DatatypeDefinitionReal] = field(
            default_factory=list,
            metadata=dict(
                name="DATATYPE-DEFINITION-REAL",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        datatype_definition_string: List[DatatypeDefinitionString] = field(
            default_factory=list,
            metadata=dict(
                name="DATATYPE-DEFINITION-STRING",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        datatype_definition_xhtml: List[DatatypeDefinitionXhtml] = field(
            default_factory=list,
            metadata=dict(
                name="DATATYPE-DEFINITION-XHTML",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )

    @dataclass
    class SpecTypes:
        """
        :ivar relation_group_type:
        :ivar spec_object_type:
        :ivar spec_relation_type:
        :ivar specification_type:
        """
        relation_group_type: List[RelationGroupType] = field(
            default_factory=list,
            metadata=dict(
                name="RELATION-GROUP-TYPE",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        spec_object_type: List[SpecObjectType] = field(
            default_factory=list,
            metadata=dict(
                name="SPEC-OBJECT-TYPE",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        spec_relation_type: List[SpecRelationType] = field(
            default_factory=list,
            metadata=dict(
                name="SPEC-RELATION-TYPE",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        specification_type: List[SpecificationType] = field(
            default_factory=list,
            metadata=dict(
                name="SPECIFICATION-TYPE",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )

    @dataclass
    class SpecObjects:
        """
        :ivar spec_object:
        """
        spec_object: List[SpecObject] = field(
            default_factory=list,
            metadata=dict(
                name="SPEC-OBJECT",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )

    @dataclass
    class SpecRelations:
        """
        :ivar spec_relation:
        """
        spec_relation: List[SpecRelation] = field(
            default_factory=list,
            metadata=dict(
                name="SPEC-RELATION",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )

    @dataclass
    class Specifications:
        """
        :ivar specification:
        """
        specification: List[Specification] = field(
            default_factory=list,
            metadata=dict(
                name="SPECIFICATION",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )

    @dataclass
    class SpecRelationGroups:
        """
        :ivar relation_group:
        """
        relation_group: List[RelationGroup] = field(
            default_factory=list,
            metadata=dict(
                name="RELATION-GROUP",
                type="Element",
                namespace="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )


@dataclass
class ReqIf:
    """
    :ivar the_header:
    :ivar core_content:
    :ivar tool_extensions:
    :ivar lang:
    """
    class Meta:
        name = "REQ-IF"
        namespace = "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"

    the_header: Optional["ReqIf.TheHeader"] = field(
        default=None,
        metadata=dict(
            name="THE-HEADER",
            type="Element",
            required=True
        )
    )
    core_content: Optional["ReqIf.CoreContent"] = field(
        default=None,
        metadata=dict(
            name="CORE-CONTENT",
            type="Element",
            required=True
        )
    )
    tool_extensions: Optional["ReqIf.ToolExtensions"] = field(
        default=None,
        metadata=dict(
            name="TOOL-EXTENSIONS",
            type="Element"
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace",
            required=True
        )
    )

    @dataclass
    class TheHeader:
        """
        :ivar req_if_header:
        """
        req_if_header: Optional[ReqIfHeader] = field(
            default=None,
            metadata=dict(
                name="REQ-IF-HEADER",
                type="Element"
            )
        )

    @dataclass
    class CoreContent:
        """
        :ivar req_if_content:
        """
        req_if_content: Optional[ReqIfContent] = field(
            default=None,
            metadata=dict(
                name="REQ-IF-CONTENT",
                type="Element"
            )
        )

    @dataclass
    class ToolExtensions:
        """
        :ivar req_if_tool_extension:
        """
        req_if_tool_extension: List[ReqIfToolExtension] = field(
            default_factory=list,
            metadata=dict(
                name="REQ-IF-TOOL-EXTENSION",
                type="Element",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
