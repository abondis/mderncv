"""
Pandoc filter using panflute to create a cv using moderncv LaTeX package
from markdown.
"""

import panflute as pf

"""

"""
def prepare(doc):
    pass

def action(elem, doc):
    if isinstance(elem, pf.BulletList) and doc.format == 'latex':
        div = pf.Div()
        for item in elem.content.list:
            plain = item.content.list[0]
            key = plain.content.pop(0)
            cv_line_tex = "\cvitem{%s}{%s}{}" % (
                pf.stringify(key), pf.stringify(plain))
            raw_inline = pf.RawInline(cv_line_tex, format='latex')
            div.content.extend([pf.Plain(raw_inline)])
        return div


def finalize(doc):
    pass


def main(doc=None):
    return pf.run_filter(action,
                         prepare=prepare,
                         finalize=finalize,
                         doc=doc)


if __name__ == '__main__':
    main()
