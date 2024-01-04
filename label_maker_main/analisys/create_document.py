from io import BytesIO

from django.http import HttpResponse
from django.shortcuts import render
from pypdf import PdfMerger

from label_maker_main.models import Label
from django_xhtml2pdf.utils import pdf_decorator


@pdf_decorator(pdfname='labels.pdf')
def create_document_code_(request, label_chunk):
    context = {'label': label_chunk, 'height': "100px", "width": "250px"}
    return render(request, 'label_maker_main/template_.html', context)


def create_document_code(request):
    all_labels = list(Label.objects.all())
    chunk_size = 30
    chunks = [all_labels[i:i + chunk_size] for i in range(0, len(all_labels), chunk_size)]

    pdfs = []
    for label_chunk in chunks:
        pdf_response = create_document_code_(request, label_chunk)
        pdfs.append(pdf_response)

    # Merge all PDFs into one
    output = BytesIO()
    pdf_merger = PdfMerger()
    for pdf in pdfs:
        pdf_merger.append(BytesIO(pdf.content))
    pdf_merger.write(output)

    # Create an HttpResponse with the merged PDF content
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="merged_labels.pdf"'
    response.write(output.getvalue())

    return response

