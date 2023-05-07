from dataclasses import dataclass, field
from typing import Dict, List, Optional, Union
from crossref.models.org.w3.pkg_1998.math.math_ml.malignmark import Malignmark
from crossref.models.org.w3.pkg_1998.math.math_ml.mglyph import Mglyph
from crossref.models.org.w3.pkg_1998.math.math_ml.mo_accent import MoAccent
from crossref.models.org.w3.pkg_1998.math.math_ml.mo_dir import MoDir
from crossref.models.org.w3.pkg_1998.math.math_ml.mo_fence import MoFence
from crossref.models.org.w3.pkg_1998.math.math_ml.mo_fontstyle import MoFontstyle
from crossref.models.org.w3.pkg_1998.math.math_ml.mo_fontweight import MoFontweight
from crossref.models.org.w3.pkg_1998.math.math_ml.mo_form import MoForm
from crossref.models.org.w3.pkg_1998.math.math_ml.mo_indentalign import MoIndentalign
from crossref.models.org.w3.pkg_1998.math.math_ml.mo_indentalignfirst import MoIndentalignfirst
from crossref.models.org.w3.pkg_1998.math.math_ml.mo_indentalignlast import MoIndentalignlast
from crossref.models.org.w3.pkg_1998.math.math_ml.mo_largeop import MoLargeop
from crossref.models.org.w3.pkg_1998.math.math_ml.mo_linebreak import MoLinebreak
from crossref.models.org.w3.pkg_1998.math.math_ml.mo_linebreakstyle import MoLinebreakstyle
from crossref.models.org.w3.pkg_1998.math.math_ml.mo_mathvariant import MoMathvariant
from crossref.models.org.w3.pkg_1998.math.math_ml.mo_movablelimits import MoMovablelimits
from crossref.models.org.w3.pkg_1998.math.math_ml.mo_separator import MoSeparator
from crossref.models.org.w3.pkg_1998.math.math_ml.mo_stretchy import MoStretchy
from crossref.models.org.w3.pkg_1998.math.math_ml.mo_symmetric import MoSymmetric
from crossref.models.org.w3.pkg_1998.math.math_ml.mo_value import MoValue

__NAMESPACE__ = "http://www.w3.org/1998/Math/MathML"


@dataclass
class Mo:
    class Meta:
        name = "mo"
        namespace = "http://www.w3.org/1998/Math/MathML"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    xref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: List[str] = field(
        default_factory=list,
        metadata={
            "name": "class",
            "type": "Attribute",
            "tokens": True,
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    other: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )
    mathcolor: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((#[0-9a-fA-F]{3}([0-9a-fA-F]{3})?)|[aA][qQ][uU][aA]|[bB][lL][aA][cC][kK]|[bB][lL][uU][eE]|[fF][uU][cC][hH][sS][iI][aA]|[gG][rR][aA][yY]|[gG][rR][eE][eE][nN]|[lL][iI][mM][eE]|[mM][aA][rR][oO][oO][nN]|[nN][aA][vV][yY]|[oO][lL][iI][vV][eE]|[pP][uU][rR][pP][lL][eE]|[rR][eE][dD]|[sS][iI][lL][vV][eE][rR]|[tT][eE][aA][lL]|[wW][hH][iI][tT][eE]|[yY][eE][lL][lL][oO][wW])\s*",
        }
    )
    mathbackground: Optional[Union[str, MoValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((#[0-9a-fA-F]{3}([0-9a-fA-F]{3})?)|[aA][qQ][uU][aA]|[bB][lL][aA][cC][kK]|[bB][lL][uU][eE]|[fF][uU][cC][hH][sS][iI][aA]|[gG][rR][aA][yY]|[gG][rR][eE][eE][nN]|[lL][iI][mM][eE]|[mM][aA][rR][oO][oO][nN]|[nN][aA][vV][yY]|[oO][lL][iI][vV][eE]|[pP][uU][rR][pP][lL][eE]|[rR][eE][dD]|[sS][iI][lL][vV][eE][rR]|[tT][eE][aA][lL]|[wW][hH][iI][tT][eE]|[yY][eE][lL][lL][oO][wW])\s*",
        }
    )
    mathvariant: Optional[MoMathvariant] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    mathsize: Optional[Union[str, MoValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        }
    )
    dir: Optional[MoDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    fontfamily: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    fontweight: Optional[MoFontweight] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    fontstyle: Optional[MoFontstyle] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    fontsize: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        }
    )
    color: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((#[0-9a-fA-F]{3}([0-9a-fA-F]{3})?)|[aA][qQ][uU][aA]|[bB][lL][aA][cC][kK]|[bB][lL][uU][eE]|[fF][uU][cC][hH][sS][iI][aA]|[gG][rR][aA][yY]|[gG][rR][eE][eE][nN]|[lL][iI][mM][eE]|[mM][aA][rR][oO][oO][nN]|[nN][aA][vV][yY]|[oO][lL][iI][vV][eE]|[pP][uU][rR][pP][lL][eE]|[rR][eE][dD]|[sS][iI][lL][vV][eE][rR]|[tT][eE][aA][lL]|[wW][hH][iI][tT][eE]|[yY][eE][lL][lL][oO][wW])\s*",
        }
    )
    background: Optional[Union[str, MoValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((#[0-9a-fA-F]{3}([0-9a-fA-F]{3})?)|[aA][qQ][uU][aA]|[bB][lL][aA][cC][kK]|[bB][lL][uU][eE]|[fF][uU][cC][hH][sS][iI][aA]|[gG][rR][aA][yY]|[gG][rR][eE][eE][nN]|[lL][iI][mM][eE]|[mM][aA][rR][oO][oO][nN]|[nN][aA][vV][yY]|[oO][lL][iI][vV][eE]|[pP][uU][rR][pP][lL][eE]|[rR][eE][dD]|[sS][iI][lL][vV][eE][rR]|[tT][eE][aA][lL]|[wW][hH][iI][tT][eE]|[yY][eE][lL][lL][oO][wW])\s*",
        }
    )
    form: Optional[MoForm] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    fence: Optional[MoFence] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    separator: Optional[MoSeparator] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lspace: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        }
    )
    rspace: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        }
    )
    stretchy: Optional[MoStretchy] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    symmetric: Optional[MoSymmetric] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    maxsize: Optional[Union[str, MoValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        }
    )
    minsize: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        }
    )
    largeop: Optional[MoLargeop] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    movablelimits: Optional[MoMovablelimits] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    accent: Optional[MoAccent] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    linebreak: Optional[MoLinebreak] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lineleading: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        }
    )
    linebreakstyle: Optional[MoLinebreakstyle] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    linebreakmultchar: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    indentalign: Optional[MoIndentalign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    indentshift: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        }
    )
    indenttarget: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    indentalignfirst: Optional[MoIndentalignfirst] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    indentshiftfirst: Optional[Union[str, MoValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        }
    )
    indentalignlast: Optional[MoIndentalignlast] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    indentshiftlast: Optional[Union[str, MoValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "mglyph",
                    "type": Mglyph,
                },
                {
                    "name": "malignmark",
                    "type": Malignmark,
                },
            ),
        }
    )
