from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class BindingTimeEnumSimple(Enum):
    """
    :cvar CODE_GENERATION_TIME: * Coding by hand, based on requirements
        document. * Tool based code generation, e.g. from a model. * The
        model may contain variants. * Only code for the selected
        variant(s) is actually generated.
    :cvar LINK_TIME: Configure what is included in object code, and what
        is omitted Based on which variant(s) are selected E.g. for
        modules that are delivered as object code (as opposed to those
        that are delivered as source code)
    :cvar PRE_COMPILE_TIME: This is typically the C-Preprocessor.
        Exclude parts of the code from the compilation process, e.g.,
        because they are not required for the selected variant, because
        they are incompatible with the selected variant, because they
        require resources that are not present in the selected variant.
        Object code is only generated for the selected variant(s). The
        code that is excluded at this stage code will not be available
        at later stages.
    :cvar SYSTEM_DESIGN_TIME: * Designing the VFB. * Software Component
        types (PortInterfaces). * SWC Prototypes and the Connections
        between SWCprototypes. * Designing the Topology * ECUs and
        interconnecting Networks * Designing the Communication Matrix
        and Data Mapping
    """
    CODE_GENERATION_TIME = "CODE-GENERATION-TIME"
    LINK_TIME = "LINK-TIME"
    PRE_COMPILE_TIME = "PRE-COMPILE-TIME"
    SYSTEM_DESIGN_TIME = "SYSTEM-DESIGN-TIME"
