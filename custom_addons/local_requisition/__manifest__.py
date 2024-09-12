{
    "name": "Stock Requisition",  # The name that will appear in the App list
    "version": "16.0.0",  # Version
    "category": "Inventory",  # Category
    "author": "Local Development",  # Author
    "application": True,  # This line says the module is an App, and not a module
    "depends": ["base",'mail','product','stock'],  # dependencies
    "data": [
      'security/ir.model.access.csv',
      'data/sequence.xml',
      'views/local_requisition_views.xml',
      'views/local_requisition_detail_views.xml',	
      'views/local_requisition_menus.xml',	
      'views/Stock.xml',	
      'views/stock_picking_local.xml',	
    ],
    "installable": True,
    'license': 'LGPL-3',
}