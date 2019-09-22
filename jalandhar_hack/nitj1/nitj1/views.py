from django.views.defaults import page_not_found

def handler_404(request, exception):
    return page_not_found(request, exception, template_name="errors/404.html")