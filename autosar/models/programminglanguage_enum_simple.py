from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class ProgramminglanguageEnumSimple(Enum):
    """
    :cvar C: C language
    :cvar CPP: C++ language
    :cvar JAVA: Java language
    """

    C = "C"
    CPP = "CPP"
    JAVA = "JAVA"
