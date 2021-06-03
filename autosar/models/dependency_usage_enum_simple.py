from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DependencyUsageEnumSimple(Enum):
    """
    :cvar BUILD: The object referred by the dependency is required
        during the build process.
    :cvar CODEGENERATION: The object referred by the dependency is
        required during code generation
    :cvar COMPILE: The object referred by the dependency is required
        during compilation.
    :cvar EXECUTE: The object referred by the dependency is required at
        execution time.
    :cvar LINK: The object referred by the dependency is required during
        linking.
    """
    BUILD = "BUILD"
    CODEGENERATION = "CODEGENERATION"
    COMPILE = "COMPILE"
    EXECUTE = "EXECUTE"
    LINK = "LINK"
