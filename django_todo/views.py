from django.shortcuts import render, redirect
from todo.models import ToDoList
from todo.forms import ToDoForm


def Home_Page(request):
    todo_form = ToDoForm(request.POST or None)
    todo_list = ToDoList.objects.all()

    context = {
        "todo_list": todo_list,
        "todo_form": todo_form
    }

    if todo_form.is_valid():
        title = todo_form.cleaned_data.get("title")
        description = todo_form.cleaned_data.get("description")

        ToDoList.objects.create(title=title, description=description)
        context["todo_form"] = ToDoForm()

    return render(request, "home.html", context)


def mark_as_completed(request, *args, **kwargs):
    item_id = kwargs.get("item_id")
    item: ToDoList = ToDoList.objects.get_by_id(item_id)

    if item is not None:
        item.completed = True
        item.save()

    return redirect("/")


def delete_item(request, *args, **kwargs):
    item_id = kwargs.get("item_id")
    item: ToDoList = ToDoList.objects.get_by_id(item_id)

    if item is not None:
        item.delete()

    return redirect("/")
