from django.contrib import messages


class Action:
    short_description = None
    func = None
    field = None

    def get_queryset(self, queryset):
        return queryset

    def action(self):
        try:
            qs = self.get_queryset(self.queryset)
            if self.field is None:
                items = qs
            else:
                items = list(qs.values_list(self.field, flat=True))
            return self.__class__.func(items)  # pylint: disable=not-callable
        except Exception as e:
            messages.error(self.request, f"Error: {e}")

    def __init__(self, modeladmin=None, request=None, queryset=None):
        self.modeladmin = modeladmin
        self.request = request
        self.queryset = queryset

    def __call__(
        self, modeladmin, request, queryset
    ):  # pylint: disable=unused-argument
        return self.__class__(modeladmin, request, queryset).action()

    def __getattribute__(self, name):
        if name == "__name__":
            return self.__class__.__name__
        return super().__getattribute__(name)
