{
    'name': 'Profesional',
    'version': '1.0.0',
    'category': 'Sales',
    'summary': 'Restricciones para ciertos usuarios de ventas',
    'depends': ['sale_management'],
    'data': [
        'security/profesional_security.xml',
        'views/sale_order_views.xml',
    ],
    'installable': True,
}
