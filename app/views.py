from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    """Display the list of tasks stored in cookies."""
    # Get the task list from cookies (as a string), if it exists
    task_list = request.COOKIES.get('tasks')
    if task_list:
        tasks = task_list.split(',')  # Convert string back to a list
    else:
        tasks = []

    return render(request, 'app/index.html', {'tasks': tasks})

def add_task(request):
    """Add a new task to the cookies."""
    if request.method == 'POST':
        new_task = request.POST.get('task')
        task_list = request.COOKIES.get('tasks')
        
        if task_list:
            tasks = task_list.split(',')
        else:
            tasks = []

        if new_task:
            tasks.append(new_task)  # Add the new task to the list

        # Create a response and set a persistent cookie
        response = redirect('index')
        response.set_cookie('tasks', ','.join(tasks), max_age=7 * 24 * 60 * 60)  # Store for 7 days
        return response