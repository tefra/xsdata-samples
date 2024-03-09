from dataclasses import dataclass, field
from typing import Dict, List, Optional, Union

from crossref.models.org.w3.pkg_1998.math.math_ml.msline_value import (
    MslineValue,
)

__NAMESPACE__ = "http://www.w3.org/1998/Math/MathML"


@dataclass
class Msline:
    class Meta:
        name = "msline"
        namespace = "http://www.w3.org/1998/Math/MathML"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    xref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: List[str] = field(
        default_factory=list,
        metadata={
            "name": "class",
            "type": "Attribute",
            "tokens": True,
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    other: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )
    mathcolor: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((#[0-9a-fA-F]{3}([0-9a-fA-F]{3})?)|[aA][qQ][uU][aA]|[bB][lL][aA][cC][kK]|[bB][lL][uU][eE]|[fF][uU][cC][hH][sS][iI][aA]|[gG][rR][aA][yY]|[gG][rR][eE][eE][nN]|[lL][iI][mM][eE]|[mM][aA][rR][oO][oO][nN]|[nN][aA][vV][yY]|[oO][lL][iI][vV][eE]|[pP][uU][rR][pP][lL][eE]|[rR][eE][dD]|[sS][iI][lL][vV][eE][rR]|[tT][eE][aA][lL]|[wW][hH][iI][tT][eE]|[yY][eE][lL][lL][oO][wW])\s*",
        },
    )
    mathbackground: Optional[Union[str, MslineValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((#[0-9a-fA-F]{3}([0-9a-fA-F]{3})?)|[aA][qQ][uU][aA]|[bB][lL][aA][cC][kK]|[bB][lL][uU][eE]|[fF][uU][cC][hH][sS][iI][aA]|[gG][rR][aA][yY]|[gG][rR][eE][eE][nN]|[lL][iI][mM][eE]|[mM][aA][rR][oO][oO][nN]|[nN][aA][vV][yY]|[oO][lL][iI][vV][eE]|[pP][uU][rR][pP][lL][eE]|[rR][eE][dD]|[sS][iI][lL][vV][eE][rR]|[tT][eE][aA][lL]|[wW][hH][iI][tT][eE]|[yY][eE][lL][lL][oO][wW])\s*",
        },
    )
    position: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    length: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    leftoverhang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    rightoverhang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    mslinethickness: Optional[Union[str, MslineValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
