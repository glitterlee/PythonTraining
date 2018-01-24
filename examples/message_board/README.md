## SDS 2 (Django Message Board) Tutorial

1. Activate the virtual environment
    1. Change directories into the folder where you created the virtual environments from last week.
    2. Activate the python 3 virtual environment with django installed with the command
       `source <env_name>/bin/activate` if you are on linux and `<env_name\Scripts\activate` if you
       are one windows, replacing *<env_name>* with the environment name.
    
2. Clone the base repository
    1. In a directory you can keep track of (**sds_python** from last week)
       clone the git repository, `git clone https://github.com/osu-cass/PythonTraining.git`.
    2. Enter the PythonTraining directory using `cd PythonTraining/examples/message_board/`

3. Run the default code and make sure everything works as expected
    1. Run this command to setup your database for initial use: `python manage.py migrate`
    2. Run this command to create an admin user which we will use later. Don't forget the password!
       `python manage.py createsuperuser`
    3. Start the django app with `python manage.py runserver`
    4. View the page at `http://localhost:8000/`.

4. Create new page for editing a message.
    1. This begins with setting up a route in board/urls.py.
	    1. Add `path(r'edit/<int:msg_id>/', views.edit_msg, name='edit_msg'),` to
		   the `urlpatterns = [...]` list.
		2. This directs a route of the form `http://localhost:8000/edit/10/`
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
		1. Find the table where the messages are being added, specifically find the line
		   `<td>{{ m.text }}</td>` and right below it REPLACE the `<td/>` with
		   `<td><a class="button float-right" href="{% url 'edit_msg' m.id %}">Edit</a></td>`
	4. View page at http://localhost:8000/ and try out the edit button and the edit page!

5. Add user to message
	1. Stop the django server with CTRL+C, as we are now making changes which will break it
	2. Add required user foreign key field to Message
		1. Import the django built in User model by adding the below to the top to the **board/models.py** file
		   ```python
		   from django.contrib.auth.models import User
		   ```
		2. Add a new field to the Message in **board/models.py**
		   ```python
		   user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
		   ```
	3. Create a migration to update the database running `python manage.py makemigrations`
		1. Run migration with
		   `python manage.py migrate`
		2. Start django server with
		   `python manage.py runserver` It should start up with no issues
	4. Add user field to **board/forms.py/NewMessageForm**
		1. Import the django built in User model by adding the below to the top of the **board/forms.py** file.
		   ```python
		   from django.contrib.auth.models import User
		   ```
		2. Add this field to the class definition.
		   ```python
		   user = forms.ModelChoiceField(queryset=User.objects.all(), required=True)
		   ```
		3. Add the field to the form's Meta class by changing the fields variable to
		   ```python
		   fields = ("user", "text",)
		   ```
	5. Add user field to **board/templates/index.html**
		1. In the input section of the form, above `{{ msg_form.text }}`
			Add the following line `{{ msg_form.user }}`
	6. Restart django server and refresh page to see changes

6. Add two users for testing
	1. Log in to admin site at http://localhost:8000/admin
	2. Click on users, and then **add user** in the upper right
	3. Under username, enter "user1" and a password, click "Save and add another"
		Enter "user2" and a password, click "Save"
	4. Navigate back to http://localhost:8000, or click "VIEW SITE" in upper right corner of admin site
	5. Notice drop down with three users: admin, user1, user2

7. Add user column to index page
	1. Edit the file **board/templates/index.html**
	2. Above the Date column header `<th>Date</th>`,
		add `<th>User</th>`
	3. In the table body, above `<td>{{ m.pub_date }}</td>`
	   add `<td>{{ m.user }}</td>`
8. Add user field to edit page
	1. Edit the file **board/templates/edit.html**
	2. In the input section of the form, above `{{ msg_form.text }}`
		Add the following line `{{ msg_form.user }}`
	3. Restart django server and check out changes at http://localhost:8000/


#### Notes
* To wipe the database, run `python manage.py flush`
