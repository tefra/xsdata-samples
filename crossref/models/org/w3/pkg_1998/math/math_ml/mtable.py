from dataclasses import dataclass, field
from typing import Optional, Union

from crossref.models.org.w3.pkg_1998.math.math_ml.columnalignstyle import (
    Columnalignstyle,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.linestyle import Linestyle
from crossref.models.org.w3.pkg_1998.math.math_ml.mlabeledtr import Mlabeledtr
from crossref.models.org.w3.pkg_1998.math.math_ml.mtable_displaystyle import (
    MtableDisplaystyle,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.mtable_equalcolumns import (
    MtableEqualcolumns,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.mtable_equalrows import (
    MtableEqualrows,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.mtable_side import MtableSide
from crossref.models.org.w3.pkg_1998.math.math_ml.mtable_value import (
    MtableValue,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.mtr import Mtr
from crossref.models.org.w3.pkg_1998.math.math_ml.verticalalign import (
    Verticalalign,
)

__NAMESPACE__ = "http://www.w3.org/1998/Math/MathML"


@dataclass
class Mtable:
    class Meta:
        name = "mtable"
        namespace = "http://www.w3.org/1998/Math/MathML"

    mtr: list[Mtr] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    mlabeledtr: list[Mlabeledtr] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    xref: object | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: list[str] = field(
        default_factory=list,
        metadata={
            "name": "class",
            "type": "Attribute",
            "tokens": True,
        },
    )
    style: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    href: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    other: object | None = field(
        default=None,
        metadata={
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
    mathcolor: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((#[0-9a-fA-F]{3}([0-9a-fA-F]{3})?)|[aA][qQ][uU][aA]|[bB][lL][aA][cC][kK]|[bB][lL][uU][eE]|[fF][uU][cC][hH][sS][iI][aA]|[gG][rR][aA][yY]|[gG][rR][eE][eE][nN]|[lL][iI][mM][eE]|[mM][aA][rR][oO][oO][nN]|[nN][aA][vV][yY]|[oO][lL][iI][vV][eE]|[pP][uU][rR][pP][lL][eE]|[rR][eE][dD]|[sS][iI][lL][vV][eE][rR]|[tT][eE][aA][lL]|[wW][hH][iI][tT][eE]|[yY][eE][lL][lL][oO][wW])\s*",
        },
    )
    mathbackground: str | MtableValue | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((#[0-9a-fA-F]{3}([0-9a-fA-F]{3})?)|[aA][qQ][uU][aA]|[bB][lL][aA][cC][kK]|[bB][lL][uU][eE]|[fF][uU][cC][hH][sS][iI][aA]|[gG][rR][aA][yY]|[gG][rR][eE][eE][nN]|[lL][iI][mM][eE]|[mM][aA][rR][oO][oO][nN]|[nN][aA][vV][yY]|[oO][lL][iI][vV][eE]|[pP][uU][rR][pP][lL][eE]|[rR][eE][dD]|[sS][iI][lL][vV][eE][rR]|[tT][eE][aA][lL]|[wW][hH][iI][tT][eE]|[yY][eE][lL][lL][oO][wW])\s*",
        },
    )
    align: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*(top|bottom|center|baseline|axis)(\s+-?[0-9]+)?\s*",
        },
    )
    rowalign: list[Verticalalign] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    columnalign: list[Columnalignstyle] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    groupalign: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"(\s*\{\s*(left|center|right|decimalpoint)(\s+(left|center|right|decimalpoint))*\})*\s*",
        },
    )
    alignmentscope: list[MtableValue] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    columnwidth: list[MtableValue] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    width: str | MtableValue | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    rowspacing: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "min_length": 1,
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
            "tokens": True,
        },
    )
    columnspacing: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "min_length": 1,
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
            "tokens": True,
        },
    )
    rowlines: list[Linestyle] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    columnlines: list[Linestyle] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    frame: Linestyle | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    framespacing: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "length": 2,
            "tokens": True,
        },
    )
    equalrows: MtableEqualrows | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    equalcolumns: MtableEqualcolumns | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    displaystyle: MtableDisplaystyle | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    side: MtableSide | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    minlabelspacing: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
