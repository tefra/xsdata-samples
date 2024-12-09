from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.data_type_type import DataTypeType
from ipxact.models.dependency import Dependency
from ipxact.models.description import Description
from ipxact.models.display_name import DisplayName
from ipxact.models.file import File
from ipxact.models.file_builder_type import FileBuilderType
from ipxact.models.file_type import FileType
from ipxact.models.ipxact_uri import IpxactUri
from ipxact.models.name_value_pair_type import NameValuePairType
from ipxact.models.return_type_type import ReturnTypeType
from ipxact.models.short_description import ShortDescription
from ipxact.models.unsigned_bit_expression import UnsignedBitExpression
from ipxact.models.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class FileSetType:
    """
    :ivar name: Unique name
    :ivar display_name:
    :ivar short_description:
    :ivar description:
    :ivar group: Identifies this filleSet as belonging to a particular
        group or having a particular purpose. Examples might be
        "diagnostics", "boot", "application", "interrupt",
        "deviceDriver", etc.
    :ivar file:
    :ivar default_file_builder: Default command and flags used to build
        derived files from the sourceName files in this file set.
    :ivar dependency:
    :ivar function: Generator information if this file set describes a
        function. For example, this file set may describe diagnostics
        for which the DE can generate a diagnostics driver.
    :ivar vendor_extensions:
    :ivar id:
    """

    class Meta:
        name = "fileSetType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "required": True,
        },
    )
    display_name: Optional[DisplayName] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    short_description: Optional[ShortDescription] = field(
        default=None,
        metadata={
            "name": "shortDescription",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    description: Optional[Description] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    group: list["FileSetType.Group"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    file: list[File] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    default_file_builder: list[FileBuilderType] = field(
        default_factory=list,
        metadata={
            "name": "defaultFileBuilder",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    dependency: list[Dependency] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    function: list["FileSetType.Function"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    vendor_extensions: Optional[VendorExtensions] = field(
        default=None,
        metadata={
            "name": "vendorExtensions",
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

    @dataclass
    class Group:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.w3.org/XML/1998/namespace",
            },
        )

    @dataclass
    class Function:
        """
        :ivar entry_point: Optional name for the function.
        :ivar file_ref: A reference to the file that contains the entry
            point function.
        :ivar return_type: Function return type. Possible values are
            void and int.
        :ivar argument: Arguments passed in when the function is called.
            Arguments are passed in order. This is an extension of the
            name-value pair which includes the data type in the
            ipxact:dataType attribute.  The argument name is in the
            ipxact:name element and its value is in the ipxact:value
            element.
        :ivar disabled: Specifies if the SW function is enabled. If not
            present the function is always enabled.
        :ivar source_file: Location information for the source file of
            this function.
        :ivar replicate: If true directs the generator to compile a
            separate object module for each instance of the component in
            the design. If false (default) the function will be called
            with different arguments for each instance.
        :ivar id:
        """

        entry_point: Optional[str] = field(
            default=None,
            metadata={
                "name": "entryPoint",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            },
        )
        file_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "fileRef",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                "required": True,
            },
        )
        return_type: Optional[ReturnTypeType] = field(
            default=None,
            metadata={
                "name": "returnType",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            },
        )
        argument: list["FileSetType.Function.Argument"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            },
        )
        disabled: Optional[UnsignedBitExpression] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            },
        )
        source_file: list["FileSetType.Function.SourceFile"] = field(
            default_factory=list,
            metadata={
                "name": "sourceFile",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            },
        )
        replicate: bool = field(
            default=False,
            metadata={
                "type": "Attribute",
            },
        )
        id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.w3.org/XML/1998/namespace",
            },
        )

        @dataclass
        class Argument(NameValuePairType):
            """
            :ivar data_type: The data type of the argument as pertains
                to the language. Example: "int", "double", "char *".
            """

            data_type: Optional[DataTypeType] = field(
                default=None,
                metadata={
                    "name": "dataType",
                    "type": "Attribute",
                    "required": True,
                },
            )

        @dataclass
        class SourceFile:
            """
            :ivar source_name: Source file for the boot load.  Relative
                names are searched for in the project directory and the
                source of the component directory.
            :ivar file_type:
            :ivar id:
            """

            source_name: Optional[IpxactUri] = field(
                default=None,
                metadata={
                    "name": "sourceName",
                    "type": "Element",
                    "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                    "required": True,
                },
            )
            file_type: Optional[FileType] = field(
                default=None,
                metadata={
                    "name": "fileType",
                    "type": "Element",
                    "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                    "required": True,
                },
            )
            id: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.w3.org/XML/1998/namespace",
                },
            )
