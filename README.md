# mderncv

Write your cv in markdown! This [panflute]( http://scorreia.com/software/panflute/ ) filter helps [pandoc]( https://pandoc.org/ ) to convert a markdown file into a modern CV based on the [LaTeX package]( https://github.com/xdanaux/moderncv ) of the same name.

## Usage

### mderncv yaml header

The yaml-header in the markdown file allows to specify the settings, that will be part of the header in the resulting `.tex` file.

#### Moderncv document class and options

```yaml
title: Resumé title
lang: en-US
documentclass: moderncv
classoption: 11pt,a4paper,sans
panflute-filters: [mderncv]
panflute-path: 'source'
header-includes: |
  \usepackage[scale=0.8]{geometry}
  \recomputelengths
```

This yaml will be translated in the resulting `.tex` file like the following:

```latex
\documentclass[11pt,a4paper,sans]{moderncv}
\usepackage[scale=0.75]{geometry}
\usepackage[scale=0.8]{geometry}
\recomputelengths
\title{Resumé title} 
```

#### mderncv template and style (not yet implemented)

Style options are:

- 'casual' (default)
- 'classic'
- 'banking'
- 'oldstyle'
- 'fancy'

Color options are:

 - 'blue' (default)
 - 'black'
 - 'burgundy'
 - 'green'
 - 'grey'
 - 'orange'
 - 'purple'
 - 'red'

```yaml
mderncv:
    style: casual
    color: blue 
```

This yaml will be translated in the resulting `.tex` file like the following:

```latex
\moderncvstyle{casual}
\moderncvcolor{blue}
```

#### mderncv personal data block (not yet implemented)

The header yaml-Block allows you to define personal data, that will be inserted in the header of the first page, in the classic theme, or in the footer of every page, in the case of casual theme. Many of the values are optional. See the moderncv example files for details.

```yaml
mderncv:
    firstname: John
    familyname: Doe
    address: 
        - street and number
        - postcode city
        - country
    phone:
        mobile: +1 (234) 567890
        fixed: +2 (345) 678 901
        fax: +3 (456) 789 012
    email: john@doe.org
    homepage: www.johndoe.com
    social:
        linkedin: john.doe
        twitter: jdoe
        github: jdoe
    extrainfo: additional information
    photo:
        picture: picture
        height: 64pt
        frame: 0.4pt
    quote: Some quote
```

This yaml will be translated in the resulting `.tex` file like the following:

```latex
% personal data
\firstname{John}
\familyname{Doe}
\address{street and number}{postcode city}{country}
\phone[mobile]{+1~(234)~567~890}
\phone[fixed]{+2~(345)~678~901}
\phone[fax]{+3~(456)~789~012}
\email{john@doe.org}
\homepage{www.johndoe.com}
\social[linkedin]{john.doe}
\social[twitter]{jdoe}
\social[github]{jdoe}
\extrainfo{additional information}
\photo[64pt][0.4pt]{picture}
\quote{Some quote}
```

### cv entries

#### Entry with two fields - cvitem

A bulleted list item, starting with a bold font weight will be replaced with `\cvitem{}{}`:

```markdown
- **2017-2019**: Something something
```

```latex
\cvitem{2017-2019}{Something something}
```

### Entry with three fields - cvitemwithcomment (not yet implemented)

```markdown
- **Language** Skill level *Explanation*
```

```latex
\cvitemwithcomment{Language}{Skill level}{Explanation} 
```

### Entry with four fields - cvdoubleitem (not yet implemented)

```markdown
- **category 1** XXX, YYY, ZZZ \* **category 3** XXX, YYY, ZZZ
- **category 2** XXX, YYY, ZZZ \* **category 4** XXX, YYY, ZZZ
```

```latex
\cvdoubleitem{category 1}{XXX, YYY, ZZZ}{category 3}{XXX, YYY, ZZZ}
\cvdoubleitem{category 2}{XXX, YYY, ZZZ}{category 4}{XXX, YYY, ZZZ}
```

### Entry with six fields - cventry (not yet implemented)

```markdown
- **year-year** Job title \* Employer \* City \* \* General description no longer than 1--2 lines.
```

```latex
\cventry{year-year}{Job title}{Employer}{City}{}{General description no longer than 1--2 lines.}
```

### List item - cvlistitem (not yet implemented)

```markdown
- Item 1
- Item 2
- Item 3
```

```latex
\cvlistitem{Item 1}
\cvlistitem{Item 2}
\cvlistitem{Item 3}
```

### List item with two fields - cvlistdoubleitem (not yet implemented)

```markdown
- Item 1 \* Item 2
- Item 3 \* Item 4
```

```latex
\cvlistdoubleitem{Item 1}{Item 2}
\cvlistdoubleitem{Item 3}{Item 4}
```