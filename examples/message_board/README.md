SDS 2 (Django Message Board) Tutorial

## Add git clone here

## Add show basic functiality here `python manage.py migrate` and `python manage.py createsuperuser` (`python manage.py runserver`)

1. Create new page for editing a message.
    1. This begins with setting up a route in board/urls.py.
	    1. Add `path(r'edit/<int:msg_id>/', views.edit_msg, name='edit_msg'),` to
		   the `urlpatterns = [...]` list.
		2. This directs a route of the form **"http://localhost:8000/edit/10/"**
		   which will send the user to a edit page for the message with id 10.
	2. Create view method (the C, Controller, in the MVC format) in board/views.py,
	   called `edit_msg` as specified in the url route "`views.edit_msg`".
	    1. The function will be `def edit_msg(request, msg_id)`.  This takes the
		   request object and the msg_id, from the url, as the parameters.
		2. The total function definition is:
		```python
		def edit_msg(request, msg_id):
			message = Message.objects.filter(id=msg_id).first()

			if message is None:
				return HttpResponseForbidden("This message doesn't exist.")
			else:
				msg_form = NewMessageForm(request.POST or None, instance=message)

				if msg_form.is_valid():
					msg_form.save()
					return redirect(reverse('index'))
				
			return render(request, 'edit.html', {
				'msg_form': msg_form,
				'message': message,
			})
		```
		3. Create the **board/template/edit.html** template.
		```html
		{% extends 'base.html' %}

		{% block content %}

		<div class='text-center'>
			<br/>
			<h4>Edit Message</h4>
			<br/>
		</div>

		<form class="form-group" id="message-post" method="POST" action="{% url 'edit_msg' message.id %}">

			{% csrf_token %}

			<div class="row">
				<div class="col-md-12" align="center">
					<p id="errors" class="text-center">
						{{ msg_form.text.errors.as_text }}
					</p>
				</div>
			</div>

			<div class="row">
				<div class="input-group">
					{{ msg_form.text }}
					<input type="submit" value="Submit">
				</div>
			</div>

		</form>
			
		{% endblock %}
		```
	3. Create edit button for each message in **board/template/index.html**
		1. Find the table where the messages are being added, sepcifally find the line
		   `<td>{{ m.text }}</td>` and add right below it
		   `<td><a class="button float-right" href="{% url 'edit_msg' m.id %}">Edit</a></td>`
	4. Show off functionality

2. Add user to message
	1. Add required user foreign key field to Message
		1. Add a new field to the Message in **board/models.py**
		```python
		user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
		```
	2. Create a migration to update the database using
		`python manage.py makemigrations`
		1. Stop django server with CTRL+C, run migration with
		`python manage.py migrate`
		2. Start django server with
		`python manage.py runserver`
	3. Add user field to **board/models.py/NewMessageForm**
		1. Add this field to the class definition
		`user = forms.ModelChoiceField(queryset=User.objects.all(), required=True)`
		2. Add the field to the form's Meta class by changing the fields variable to:
		`fields = ("user", "text",)`
	4. Add user field to **board/templates/index.html**
		1. In the input section of the form, above `{{ msg_form.text }}`
			Add the following line `{{ msg_form.user }}`
	5. Restart django server and refresh page to see changes

3. Add two users for testing
	1. Log in to admin site at `http://localhost:8000/admin`
	2. Click on users, and then **add user** in the upper right
	3. Under username, enter "user1" and a password, click "save and add another"
		Enter "user2" and a password, click "save"
	4. Navigate back to `http://localhost:8000`, or click "view site" in upper right corner of admin site
	5. Notice drop down with three users: admin, user1, user2

4. Add user column to index page
	1. Edit the file **board/templates/index.html**
	2. Above the Date column header (`<th>Date</th>`),
		add the following `<th>User</th>`
	3. In the table body, above `<td>{{ m.pub_date }}</td>`
	add `<td>{{ m.user }}</td>`
5. Add user field to edit page
	1. Edit the file **board/templates/edit.html**
	2. In the input section of the form, above `{{ msg_form.text }}`
		Add the following line `{{ msg_form.user }}`
