from django.db.models.signals import post_delete
from django.dispatch import receiver

from .models import Task


@receiver(post_delete, sender=Task)
def delete_task(sender, instance, using, **kwargs):
    if instance.id is None:
        return
    print("task delete")
    print(kwargs)
    print(instance)
    print(sender)
    executor = instance.executor
    executor.ended_tasks += 1
    executor.save()
    instance.delete()
    return True
