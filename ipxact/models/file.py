from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.dependency import Dependency
from ipxact.models.file_type import FileType
from ipxact.models.ipxact_uri import IpxactUri
from ipxact.models.name_value_pair_type import NameValuePairType
from ipxact.models.string_expression import StringExpression
from ipxact.models.unsigned_bit_expression import UnsignedBitExpression
from ipxact.models.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class File:
    """
    IP-XACT reference to a file or directory.

    :ivar name: Path to the file or directory. If this path is a
        relative path, then it is relative to the containing XML file.
    :ivar file_type:
    :ivar is_structural: Indicates that the current file is purely
        structural.
    :ivar is_include_file: Indicate that the file is include file.
    :ivar logical_name: Logical name for this file or directory e.g.
        VHDL library name.
    :ivar exported_name: Defines exported names that can be accessed
        externally, e.g. exported function names from a C source file.
    :ivar build_command: Command and flags used to build derived files
        from the sourceName files. If this element is present, the
        command and/or flags used to to build the file will override or
        augment any default builders at a higher level.
    :ivar dependency:
    :ivar define: Specifies define symbols that are used in the source
        file.  The ipxact:name element gives the name to be defined and
        the text content of the ipxact:value element holds the value.
        This element supports full configurability.
    :ivar image_type: Relates the current file to a certain executable
        image type in the design.
    :ivar description: String for describing this file to users
    :ivar vendor_extensions:
    :ivar file_id: Unique ID for this file, referenced in
        fileSet/function/fileRef
    :ivar other_attributes:
    :ivar id:
    """

    class Meta:
        name = "file"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    name: IpxactUri | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    file_type: list[FileType] = field(
        default_factory=list,
        metadata={
            "name": "fileType",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    is_structural: bool | None = field(
        default=None,
        metadata={
            "name": "isStructural",
            "type": "Element",
        },
    )
    is_include_file: File.IsIncludeFile | None = field(
        default=None,
        metadata={
            "name": "isIncludeFile",
            "type": "Element",
        },
    )
    logical_name: File.LogicalName | None = field(
        default=None,
        metadata={
            "name": "logicalName",
            "type": "Element",
        },
    )
    exported_name: list[File.ExportedName] = field(
        default_factory=list,
        metadata={
            "name": "exportedName",
            "type": "Element",
        },
    )
    build_command: File.BuildCommand | None = field(
        default=None,
        metadata={
            "name": "buildCommand",
            "type": "Element",
        },
    )
    dependency: list[Dependency] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    define: list[NameValuePairType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    image_type: list[File.ImageType] = field(
        default_factory=list,
        metadata={
            "name": "imageType",
            "type": "Element",
        },
    )
    description: str | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    vendor_extensions: VendorExtensions | None = field(
        default=None,
        metadata={
            "name": "vendorExtensions",
            "type": "Element",
        },
    )
    file_id: str | None = field(
        default=None,
        metadata={
            "name": "fileId",
            "type": "Attribute",
        },
    )
    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )
    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )

    @dataclass
    class IsIncludeFile:
        """
        :ivar value:
        :ivar external_declarations: the File contains some declarations
            that are needed in top file
        """

        value: bool | None = field(
            default=None,
            metadata={
                "required": True,
            },
        )
        external_declarations: bool = field(
            default=False,
            metadata={
                "name": "externalDeclarations",
                "type": "Attribute",
            },
        )

    @dataclass
    class LogicalName:
        """
        :ivar value:
        :ivar default: The logical name shall only be used as a default
            and another process may override this name.
        """

        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        default: bool = field(
            default=False,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class ExportedName:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        id: str | None = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.w3.org/XML/1998/namespace",
            },
        )

    @dataclass
    class BuildCommand:
        """
        :ivar command: Command used to build this file.
        :ivar flags: Flags given to the build command when building this
            file. If the optional attribute "append" is "true", this
            string will be appended to any existing flags, otherwise
            these flags will replace any existing default flags.
        :ivar replace_default_flags: If true, the value of the sibling
            element "flags" should replace any default flags specified
            at a more global level. If this is true and the sibling
            element "flags" is empty or missing, this has the effect of
            clearing any default flags.
        :ivar target_name: Pathname to the file that is derived (built)
            from the source file.
        """

        command: StringExpression | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        flags: File.BuildCommand.Flags | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        replace_default_flags: UnsignedBitExpression | None = field(
            default=None,
            metadata={
                "name": "replaceDefaultFlags",
                "type": "Element",
            },
        )
        target_name: IpxactUri | None = field(
            default=None,
            metadata={
                "name": "targetName",
                "type": "Element",
            },
        )

        @dataclass
        class Flags(StringExpression):
            """
            :ivar append: "true" indicates that the flags shall be
                appended to any existing flags, "false"indicates these
                flags will replace any existing default flags.
            """

            append: bool | None = field(
                default=None,
                metadata={
                    "type": "Attribute",
                },
            )

    @dataclass
    class ImageType:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        id: str | None = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.w3.org/XML/1998/namespace",
            },
        )
