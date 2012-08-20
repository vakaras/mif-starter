#!/usr/bin/python3
{
    # main.tex options
    'document_class': 'documentation',
    'document_class_args': '12pt, a4paper',
    'use_annotation': False,
    'use_bibliography': True,
    # style.sty options
    'font': 'Palemonas',
    'page_geometry': 'top=2.0cm, bottom=2.0cm, left=3.0cm, right=1.5cm',
    # other options
    'template_files': [
        'main.tex',
        'chapters.tex',
        'documentation.cls',
        ],
    'concat_files': {
        'style.sty': [
            #'style/old.sty',
            'style/font.sty',
            'style/page.sty',
            'style/paragraph.sty',
            # TODO 'style/table.sty',
            'style/enumeration.sty',
            ],
        },
    }
