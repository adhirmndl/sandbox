Todos.TodosController = Ember.ArrayController.extend({
	actions: {
		createTodo: function(){
			// Get the todo title
			var title = this.get('newTitle');
			if (!title.trim()) { return; }

			// Create the new Todo
			var todo = this.store.createRecord('todo', {
				title: title,
				isCompleted: false
			});

			// Clear the new todo text field
			this.set('newTitle', '');

			todo.save();
		}
	}
});