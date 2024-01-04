from django.shortcuts import render, redirect
from django.views.generic import View
from label_maker_main.analisys.create_document import create_document_code
from label_maker_main.analisys.get_values import get_values
from label_maker_main.forms import uploadForm
from label_maker_main.models import Label


class Home(View):
    def get(self, request):
        context = {'upload_form': uploadForm}
        return render(request, 'label_maker_main/home.html', context)

    def post(self, request):
        form = uploadForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['upload_file']  # Replace 'file_field_name' with the actual name of your file field
            list_items: list = get_values(excel_file)

            # create labels in database
            for i in list_items:
                Label.objects.get_or_create(name=i)

            # take labels and put them in template
            return create_document_code(request)
        return redirect('label_maker:home')
