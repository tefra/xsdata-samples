from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.clearbox_element_ref_type import ClearboxElementRefType
from ipxact.models.constraint_set_ref import ConstraintSetRef
from ipxact.models.description import Description
from ipxact.models.display_name import DisplayName
from ipxact.models.file_builder_type import FileBuilderType
from ipxact.models.file_set_ref import FileSetRef
from ipxact.models.language_type import LanguageType
from ipxact.models.module_parameter_type import ModuleParameterType
from ipxact.models.parameters import Parameters
from ipxact.models.short_description import ShortDescription
from ipxact.models.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class ComponentInstantiationType:
    """
    Component instantiation type.

    :ivar name: Unique name
    :ivar display_name:
    :ivar short_description:
    :ivar description:
    :ivar is_virtual: When true, indicates that this component should
        not be netlisted.
    :ivar language: The hardware description language used such as
        "verilog" or "vhdl". If the attribute "strict" is "true", this
        value must match the language being generated for the design.
    :ivar library_name: A string specifying the library name in which
        the model should be compiled. If the libraryName element is not
        present then its value defaults to “work”.
    :ivar package_name: A string describing the VHDL package containing
        the interface of the model. If the packageName element is not
        present then its value defaults to the component VLNV name
        concatenated with postfix “_cmp_pkg” which stands for component
        package.
    :ivar module_name: A string describing the Verilog, SystemVerilog,
        or SystemC module name or the VHDL entity name. If the
        moduleName is not present then its value defaults to the
        component VLNV name
    :ivar architecture_name: A string describing the VHDL architecture
        name. If the architectureName element is not present then its
        value defaults to “rtl”.
    :ivar configuration_name: A string describing the Verilog,
        SystemVerilog, or VHDL configuration name. If the
        configurationName element is not present then its value defaults
        to the design configuration VLNV name of the design
        configuration associated with the active hierarchical view or,
        if there is no active hierarchical view, to the component VLNV
        name concatenated with postfix “_rtl_cfg”.
    :ivar module_parameters: Model parameter name value pairs container
    :ivar default_file_builder: Default command and flags used to build
        derived files from the sourceName files in the referenced file
        sets.
    :ivar file_set_ref:
    :ivar constraint_set_ref:
    :ivar clearbox_element_refs: Container for clear box element
        references.
    :ivar parameters:
    :ivar vendor_extensions:
    :ivar id:
    """

    class Meta:
        name = "componentInstantiationType"

    name: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "required": True,
        },
    )
    display_name: None | DisplayName = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    short_description: None | ShortDescription = field(
        default=None,
        metadata={
            "name": "shortDescription",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    description: None | Description = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    is_virtual: None | bool = field(
        default=None,
        metadata={
            "name": "isVirtual",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    language: None | LanguageType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    library_name: None | str = field(
        default=None,
        metadata={
            "name": "libraryName",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    package_name: None | str = field(
        default=None,
        metadata={
            "name": "packageName",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    module_name: None | str = field(
        default=None,
        metadata={
            "name": "moduleName",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    architecture_name: None | str = field(
        default=None,
        metadata={
            "name": "architectureName",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    configuration_name: None | str = field(
        default=None,
        metadata={
            "name": "configurationName",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    module_parameters: None | ComponentInstantiationType.ModuleParameters = (
        field(
            default=None,
            metadata={
                "name": "moduleParameters",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            },
        )
    )
    default_file_builder: list[FileBuilderType] = field(
        default_factory=list,
        metadata={
            "name": "defaultFileBuilder",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    file_set_ref: list[FileSetRef] = field(
        default_factory=list,
        metadata={
            "name": "fileSetRef",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    constraint_set_ref: list[ConstraintSetRef] = field(
        default_factory=list,
        metadata={
            "name": "constraintSetRef",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    clearbox_element_refs: (
        None | ComponentInstantiationType.ClearboxElementRefs
    ) = field(
        default=None,
        metadata={
            "name": "clearboxElementRefs",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    parameters: None | Parameters = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    vendor_extensions: None | VendorExtensions = field(
        default=None,
        metadata={
            "name": "vendorExtensions",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )

    @dataclass
    class ModuleParameters:
        """
        :ivar module_parameter: A module parameter name value pair. The
            name is given in an attribute. The value is the element
            value. The dataType (applicable to high level modeling) is
            given in the dataType attribute. For hardware based models,
            the name should be identical to the RTL (VHDL generic or
            Verilog parameter). The usageType attribute indicates how
            the model parameter is to be used.
        """

        module_parameter: list[ModuleParameterType] = field(
            default_factory=list,
            metadata={
                "name": "moduleParameter",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                "min_occurs": 1,
            },
        )

    @dataclass
    class ClearboxElementRefs:
        """
        :ivar clearbox_element_ref: Reference to a clear box element
            which is visible within this view.
        """

        clearbox_element_ref: list[ClearboxElementRefType] = field(
            default_factory=list,
            metadata={
                "name": "clearboxElementRef",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            },
        )
