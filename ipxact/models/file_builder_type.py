from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.file_type import FileType
from ipxact.models.string_expression import StringExpression
from ipxact.models.unsigned_bit_expression import UnsignedBitExpression

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class FileBuilderType:
    """
    :ivar file_type:
    :ivar command: Default command used to build files of the specified
        fileType.
    :ivar flags: Flags given to the build command when building files of
        this type.
    :ivar replace_default_flags: If true, replace any default flags
        value with the value in the sibling flags element. Otherwise,
        append the contents of the sibling flags element to any default
        flags value. If the value is true and the "flags" element is
        empty or missing, this will have the result of clearing any
        default flags value.
    :ivar id:
    """

    class Meta:
        name = "fileBuilderType"

    file_type: Optional[FileType] = field(
        default=None,
        metadata={
            "name": "fileType",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "required": True,
        },
    )
    command: Optional[StringExpression] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    flags: Optional[StringExpression] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    replace_default_flags: Optional[UnsignedBitExpression] = field(
        default=None,
        metadata={
            "name": "replaceDefaultFlags",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
