{
    'name': "Real Estate",
    'summary': "Management of Real Estate",
    'version': '1.0',
    'depends': ['base'],
    'author': "jeanpetit",
    'category': 'Category',
    'description': 
        """
        Description text
        """,
    # data files always loaded at installation
    'data': [
        'views/estate_property_views.xml',
        'security/ir.model.access.csv',
        'security/groupe.xml',
        'report/estate_property_report.xml',
        'report/estate_property_templates.xml',
    ],
    # data files containing optionally loaded demonstration data
    # 'demo': [
    #     'demo/demo_data.xml',
    # ],
    'application': True ,
    'installable': True ,
    'auto_install': False,
    'sequence': 1,
}