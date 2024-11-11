import mimetypes
import os

from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from .forms import ResponseSettingsForm
from .models import ResponseSettings, Image


def image(request, file_name):
    rs = ResponseSettings.objects.get(pk=1)
    if rs.mode == rs.Mode.ERROR:
        return HttpResponseNotFound()

    file = get_object_or_404(Image, name=file_name)
    _, extension = os.path.splitext(file.img.url)
    new_file_name = f'{file_name}{extension}'
    (mime_type, *_) = mimetypes.guess_type(file.img.url)

    try:
        with open(file.img.path, 'rb') as f:
            file_data = f.read()
            response = HttpResponse(file_data, content_type=mime_type)
            response['Content-Disposition'] = f'attachment; filename="{new_file_name}"'
    except IOError:
        response = HttpResponseNotFound()

    return response


class ResponseSettingsUpdateView(TemplateView):
    template_name = 'update_response_settings.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        rs = ResponseSettings.objects.get(pk=1)
        context['form'] = ResponseSettingsForm(instance=rs)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        rs = ResponseSettings.objects.get(pk=1)
        form = ResponseSettingsForm(request.POST, instance=rs)
        if form.is_valid():
            form.save()
        context['form'] = form
        return self.render_to_response(context)
