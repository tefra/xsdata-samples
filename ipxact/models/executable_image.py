from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.description import Description
from ipxact.models.display_name import DisplayName
from ipxact.models.file_set_ref import FileSetRef
from ipxact.models.file_type import FileType
from ipxact.models.linker_command_file import LinkerCommandFile
from ipxact.models.parameters import Parameters
from ipxact.models.short_description import ShortDescription
from ipxact.models.string_expression import StringExpression
from ipxact.models.unsigned_bit_expression import UnsignedBitExpression
from ipxact.models.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class ExecutableImage:
    """
    Specifies an executable software image to be loaded into a processors
    address space.

    The format of the image is not specified. It could, for example, be an
    ELF loadfile, or it could be raw binary or ascii hex data for loading
    directly into a memory model instance.

    :ivar name: Unique name
    :ivar display_name:
    :ivar short_description:
    :ivar description:
    :ivar parameters: Additional information about the load module, e.g.
        stack base addresses, table addresses, etc.
    :ivar language_tools: Default commands and flags for software
        language tools needed to build the executable image.
    :ivar file_set_ref_group: Contains a group of file set references
        that indicates the set of file sets complying with the tool set
        of the current executable image.
    :ivar vendor_extensions:
    :ivar image_id: Unique ID for the executableImage, referenced in
        fileSet/function/fileRef
    :ivar image_type: Open element to describe the type of image. The
        contents is model and/or generator specific.
    :ivar id:
    """

    class Meta:
        name = "executableImage"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    name: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    display_name: DisplayName | None = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
        },
    )
    short_description: ShortDescription | None = field(
        default=None,
        metadata={
            "name": "shortDescription",
            "type": "Element",
        },
    )
    description: Description | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    parameters: Parameters | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    language_tools: ExecutableImage.LanguageTools | None = field(
        default=None,
        metadata={
            "name": "languageTools",
            "type": "Element",
        },
    )
    file_set_ref_group: ExecutableImage.FileSetRefGroup | None = field(
        default=None,
        metadata={
            "name": "fileSetRefGroup",
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
    image_id: str | None = field(
        default=None,
        metadata={
            "name": "imageId",
            "type": "Attribute",
            "required": True,
        },
    )
    image_type: str | None = field(
        default=None,
        metadata={
            "name": "imageType",
            "type": "Attribute",
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
    class LanguageTools:
        """
        :ivar file_builder: A generic placeholder for any file builder
            like compilers and assemblers.  It contains the file types
            to which the command should be applied, and the flags to be
            used with that command.
        :ivar linker:
        :ivar linker_flags:
        :ivar linker_command_file:
        """

        file_builder: list[ExecutableImage.LanguageTools.FileBuilder] = (
            field(
                default_factory=list,
                metadata={
                    "name": "fileBuilder",
                    "type": "Element",
                },
            )
        )
        linker: StringExpression | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        linker_flags: StringExpression | None = field(
            default=None,
            metadata={
                "name": "linkerFlags",
                "type": "Element",
            },
        )
        linker_command_file: list[LinkerCommandFile] = field(
            default_factory=list,
            metadata={
                "name": "linkerCommandFile",
                "type": "Element",
                "max_occurs": 2,
                "sequence": 1,
            },
        )

        @dataclass
        class FileBuilder:
            """
            :ivar file_type:
            :ivar command: Default command used to build files of the
                specified fileType.
            :ivar flags: Flags given to the build command when building
                files of this type.
            :ivar replace_default_flags: If true, replace any default
                flags value with the value in the sibling flags element.
                Otherwise, append the contents of the sibling flags
                element to any default flags value. If the value is true
                and the "flags" element is empty or missing, this will
                have the result of clearing any default flags value.
            :ivar vendor_extensions:
            :ivar id:
            """

            file_type: FileType | None = field(
                default=None,
                metadata={
                    "name": "fileType",
                    "type": "Element",
                    "required": True,
                },
            )
            command: StringExpression | None = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                },
            )
            flags: StringExpression | None = field(
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
            vendor_extensions: VendorExtensions | None = field(
                default=None,
                metadata={
                    "name": "vendorExtensions",
                    "type": "Element",
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
    class FileSetRefGroup:
        file_set_ref: list[FileSetRef] = field(
            default_factory=list,
            metadata={
                "name": "fileSetRef",
                "type": "Element",
                "min_occurs": 1,
            },
        )
