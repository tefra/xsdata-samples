from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class DisplayFormatString:
    """This is a display format specifier for the display of values  e.g. in documents or in measurement and calibration systems.
    The display format specifier is a subset of the ANSI C printf specifiers with the following
    form:
    % [flags] [width] [.prec] type character
    For more details refer to "ASAM-HarmonizedDataObjects-V1.1.pdf" chapter 13.3.2 DISPLAY OF DATA.
    Due to the numerical nature of value settings, only the following type characters are allowed:
    * d:  Signed decimal integer
    * i:  Signed decimal integer
    * o:  Unsigned octal integer
    * u:  Unsigned decimal integer
    * x:  Unsigned hexadecimal integer, using "abcdef"
    * X:  Unsigned hexadecimal integer, using "ABCDEF"
    * e:  Signed value having the form [-]d.dddd e [sign]ddd where d is a single decimal digit, dddd is one or more decimal digits, ddd is exactly three decimal digits, and sign is + or -
    * E:  Identical to the e format except that E rather than e introduces the exponent
    * f:  Signed value having the form [-]dddd.dddd, where dddd is one or more decimal digits; the number of digits before the decimal point depends on the magnitude of the number, and the number of digits after the decimal point depends on the requested precision
    * g:  Signed value printed in f or e format, whichever is more compact for the given value and precision; trailing zeros are truncated, and the decimal point appears only if one or more digits follow it
    * G:  Identical to the g format, except that E, rather than e, introduces the exponent (where appropriate)

    :ivar value:
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
        name = "DISPLAY-FORMAT-STRING"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"%[ \-+#]?[0-9]*(\.[0-9]+)?[diouxXfeEgGcs]",
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
