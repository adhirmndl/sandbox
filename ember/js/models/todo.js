Todos.Todo = DS.Model.extend({
	title: DS.attr('string'),
	isCompleted: DS.attr('boolean')
});

Todos.Todo.FIXTURES = [
	{
		id: 1,
		title: 'Learn Stuff',
		isCompleted: true
	},
	{
		id: 2,
		title: 'whoa, this works',
		isCompleted: false
	},
	{
		id: 3,
		title: 'Profit!',
		isCompleted: false
	}
];