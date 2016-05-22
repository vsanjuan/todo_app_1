#*-* coding: utf-8 -*-
from openerp import models, fields
class TodoTask(models.Model):
	_name = 'todo.taks'
	name = fields.Char('Description', required=True)
	is_done = fields.Boolean('Done?')
	active = fields.Boolean('Active?', default=True)

	