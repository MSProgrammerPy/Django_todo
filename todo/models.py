from django.db import models


# Create your models here.


class ToDoListManager(models.Manager):
    def get_by_id(self, item_id):
        qs = self.get_queryset().filter(pk=item_id)

        if qs.exists() and qs.count() == 1:
            return qs.first()
        else:
            return None


class ToDoList(models.Model):
    title = models.CharField(max_length=40, verbose_name="title")
    description = models.TextField(max_length=400, verbose_name="description")
    completed = models.BooleanField(default=False, verbose_name="completed")
    date = models.DateTimeField(auto_now_add=True, verbose_name="date")

    objects = ToDoListManager()

    class Meta:
        verbose_name_plural = "ToDo List"
        verbose_name = "ToDo"

    def __str__(self):
        return self.title
