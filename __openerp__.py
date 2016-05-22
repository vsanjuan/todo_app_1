#*-* coding: utf-8 -*-
{
	'name' : 'To-Do Application',
	'description': 'Mananage your persoal Tasks with this module',
	'author': 'Daniel Reis',
	'depends': ['mail'],
	'data': [
		'todo_view.xml',
		'security/ir.model.access.csv',
		'security/todo_access_rules.xml',
		],
	'application': True,

}
