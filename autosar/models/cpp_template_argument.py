from dataclasses import dataclass, field
from typing import Optional
from autosar.models.allocator_subtypes_enum import AllocatorSubtypesEnum
from autosar.models.boolean import Boolean
from autosar.models.category_string import CategoryString
from autosar.models.cpp_implementation_data_type_subtypes_enum import CppImplementationDataTypeSubtypesEnum
from autosar.models.ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class CppTemplateArgument:
    """
    This meta-class has the ability to define properties for template
    arguments.

    :ivar allocator_ref: This reference identifies the applicable
        allocator.
    :ivar category: This attribute shall be used to contribute further
        clarification regarding the semantics of the enclosing
        CppTemplateArgument.
    :ivar inplace: This attribute specifies whether the shortName of the
        referenced templateType is used in the code generation and the
        type declaration is defined outside of the enclosing
        CppImplementationDataType (true) or whether the type definition
        is embedded inside of the enclosing CppImplementationDataType
        and the shortName is ignored (false).
    :ivar template_type_ref: This reference identifies the data type of
        the specific template argument required for the language
        binding.
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
        name = "CPP-TEMPLATE-ARGUMENT"

    allocator_ref: Optional["CppTemplateArgument.AllocatorRef"] = field(
        default=None,
        metadata={
            "name": "ALLOCATOR-REF",
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
    inplace: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "INPLACE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    template_type_ref: Optional["CppTemplateArgument.TemplateTypeRef"] = field(
        default=None,
        metadata={
            "name": "TEMPLATE-TYPE-REF",
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

    @dataclass
    class AllocatorRef(Ref):
        dest: Optional[AllocatorSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class TemplateTypeRef(Ref):
        dest: Optional[CppImplementationDataTypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
