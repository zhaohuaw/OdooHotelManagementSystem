# -*- encoding: utf-8 -*-
#############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2012-Today Serpent Consulting Services Pvt. Ltd.
#    (<http://www.serpentcs.com>)
#    Copyright (C) 2004 OpenERP SA (<http://www.openerp.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
#############################################################################

{
    "name": "Hotel POS Restaurant Management",
    "version": "0.10",
    "author": "Serpent Consulting Services Pvt. Ltd., OpenERP SA",
    "category": "Generic Modules/Hotel Restaurant Management",
    "description": """
    Module for Hotel/Restaurant management. You can manage:
     """,
    "website": "http://www.serpentcs.com",
    "depends": ["pos_restaurant"],
    "demo": ["views/hotel_pos_data.xml"],
    "data": ["security/ir.model.access.csv",
             "views/pos_restaurent_view.xml"],
    "auto_install": False,
    "installable": True
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
