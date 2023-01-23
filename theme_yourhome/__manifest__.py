# -*- coding: utf-8 -*-
{
    'name': 'YourHome Theme',
    'description': 'YourHome website theme',
    'category': 'Theme/Creative',
    'sequence': 10,
    'author': 'Anees',
    'version': '1.0',
    'depends': ['website'],
    'data': [
        'views/header.xml',
        'views/footer.xml',
        'views/homepage.xml',
        'views/services_page.xml',
        'views/menues.xml',
        'views/snippets/propert-agents.xml',
        'views/snippets/new-properties.xml',
        'views/snippets/rent_mega_menu.xml',
        'views/snippets/explore-cities.xml',
        'views/snippets/snippets.xml',

        'security/ir.model.access.csv',
        'views/yh_cities.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            "theme_yourhome/static/src/scss/styles.scss",
            "theme_yourhome/static/src/scss/property-agents.scss",
            "theme_yourhome/static/src/js/explore-cities.js",
        ],
        'web._assets_primary_variables': [
            "theme_yourhome/static/src/scss/primary_variables.scss"
        ]
    },
    'images': [],
    'snippet_lists': {},
    'license': 'LGPL-3',
}
