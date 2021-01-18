from django.contrib.auth.mixins import AccessMixin


class SchemaAccessMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user == self.get_object().user_id:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
