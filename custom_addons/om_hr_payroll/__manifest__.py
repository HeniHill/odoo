{
    'name': 'Odoo 17 HR Payroll',
    'category': 'Generic Modules/Human Resources',
    'version': '17.0.1.0.4',
    'sequence': 1,
    'author': 'Odoo Mates, Odoo SA',
    'summary': 'Payroll For Odoo 17 Community Edition',
    'live_test_url': 'https://www.youtube.com/watch?v=0kaHMTtn7oY',
    'description': "Odoo 17 Payroll, Payroll Odoo 17, Odoo Community Payroll",
    'website': 'https://www.odoomates.tech',
    'license': 'LGPL-3',
    'depends': [
        'mail',
        'hr_contract',
        'hr_holidays',
    ],
    'data': [
        'security/hr_payroll_security.xml',
        'security/ir.model.access.csv',
        'data/hr_payroll_sequence.xml',
        'data/hr_payroll_category.xml',
        'data/hr_payroll_data.xml',
        'wizard/hr_payroll_payslips_by_employees_views.xml',
        'views/hr_contract_type_views.xml',
        'views/hr_contract_views.xml',
        'views/hr_salary_rule_views.xml',
        'views/hr_payslip_views.xml',
        'views/hr_employee_views.xml',
        'views/hr_payroll_report.xml',
        'wizard/hr_payroll_contribution_register_report_views.xml',
        'views/res_config_settings_views.xml',
        'views/report_contribution_register_templates.xml',
        'views/report_payslip_templates.xml',
        'views/report_payslip_details_templates.xml',
        'views/hr_contract_history_views.xml',
        'views/hr_leave_type_view.xml',
        'data/mail_template.xml',
    ],
    'images': ['static/description/banner.png'],
    'application': True,
    'module_type': 'official' 
}
