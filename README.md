# Django Admin Action
`admin.py:`
```python
from django.contrib.admin import ModelAdmin

from django_admin_action import Action

from project_logic import archive_items, create_report, task_notify


# Queryset is passed to create_report
class CreateReportAction(Action):
    short_description = 'Create report
    func = create_report


# List of ids passed to task_notify
class NotifyAction(Action):
    short_description = 'Notify
    func = task_notify.delay
    field = 'id


class ArchiveAction(Action):
    short_description = 'Archive items
    func = archive_items
    
    # You can modify queryset
    def get_queryset(self, queryset):
        return queryset.filter(is_archived=False)


class ItemAdmin(ModelAdmin):
    # ...

    actions = [
        ArchiveAction(),
        CreateReportAction(),
        NotifyAction(),
    ]
```
