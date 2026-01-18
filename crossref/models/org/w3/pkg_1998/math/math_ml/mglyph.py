from __future__ import annotations

from dataclasses import dataclass, field

from crossref.models.org.w3.pkg_1998.math.math_ml.mglyph_fontstyle import (
    MglyphFontstyle,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.mglyph_fontweight import (
    MglyphFontweight,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.mglyph_mathvariant import (
    MglyphMathvariant,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.mglyph_value import (
    MglyphValue,
)

__NAMESPACE__ = "http://www.w3.org/1998/Math/MathML"


@dataclass(kw_only=True)
class Mglyph:
    class Meta:
        name = "mglyph"
        namespace = "http://www.w3.org/1998/Math/MathML"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    xref: None | object = field(
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
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    href: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    other: None | object = field(
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
    mathcolor: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((#[0-9a-fA-F]{3}([0-9a-fA-F]{3})?)|[aA][qQ][uU][aA]|[bB][lL][aA][cC][kK]|[bB][lL][uU][eE]|[fF][uU][cC][hH][sS][iI][aA]|[gG][rR][aA][yY]|[gG][rR][eE][eE][nN]|[lL][iI][mM][eE]|[mM][aA][rR][oO][oO][nN]|[nN][aA][vV][yY]|[oO][lL][iI][vV][eE]|[pP][uU][rR][pP][lL][eE]|[rR][eE][dD]|[sS][iI][lL][vV][eE][rR]|[tT][eE][aA][lL]|[wW][hH][iI][tT][eE]|[yY][eE][lL][lL][oO][wW])\s*",
        },
    )
    mathbackground: None | str | MglyphValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((#[0-9a-fA-F]{3}([0-9a-fA-F]{3})?)|[aA][qQ][uU][aA]|[bB][lL][aA][cC][kK]|[bB][lL][uU][eE]|[fF][uU][cC][hH][sS][iI][aA]|[gG][rR][aA][yY]|[gG][rR][eE][eE][nN]|[lL][iI][mM][eE]|[mM][aA][rR][oO][oO][nN]|[nN][aA][vV][yY]|[oO][lL][iI][vV][eE]|[pP][uU][rR][pP][lL][eE]|[rR][eE][dD]|[sS][iI][lL][vV][eE][rR]|[tT][eE][aA][lL]|[wW][hH][iI][tT][eE]|[yY][eE][lL][lL][oO][wW])\s*",
        },
    )
    src: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    width: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    height: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    valign: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    alt: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    index: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    mathvariant: None | MglyphMathvariant = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    mathsize: None | str | MglyphValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    fontfamily: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    fontweight: None | MglyphFontweight = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    fontstyle: None | MglyphFontstyle = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    fontsize: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    color: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((#[0-9a-fA-F]{3}([0-9a-fA-F]{3})?)|[aA][qQ][uU][aA]|[bB][lL][aA][cC][kK]|[bB][lL][uU][eE]|[fF][uU][cC][hH][sS][iI][aA]|[gG][rR][aA][yY]|[gG][rR][eE][eE][nN]|[lL][iI][mM][eE]|[mM][aA][rR][oO][oO][nN]|[nN][aA][vV][yY]|[oO][lL][iI][vV][eE]|[pP][uU][rR][pP][lL][eE]|[rR][eE][dD]|[sS][iI][lL][vV][eE][rR]|[tT][eE][aA][lL]|[wW][hH][iI][tT][eE]|[yY][eE][lL][lL][oO][wW])\s*",
        },
    )
    background: None | str | MglyphValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((#[0-9a-fA-F]{3}([0-9a-fA-F]{3})?)|[aA][qQ][uU][aA]|[bB][lL][aA][cC][kK]|[bB][lL][uU][eE]|[fF][uU][cC][hH][sS][iI][aA]|[gG][rR][aA][yY]|[gG][rR][eE][eE][nN]|[lL][iI][mM][eE]|[mM][aA][rR][oO][oO][nN]|[nN][aA][vV][yY]|[oO][lL][iI][vV][eE]|[pP][uU][rR][pP][lL][eE]|[rR][eE][dD]|[sS][iI][lL][vV][eE][rR]|[tT][eE][aA][lL]|[wW][hH][iI][tT][eE]|[yY][eE][lL][lL][oO][wW])\s*",
        },
    )
