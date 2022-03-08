from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from datetime import date, timedelta
from django.utils import timezone
from .models import Coaster

# Home Page
def home(request):
  today = date.today()
  days = timedelta(90)
  future_date = today + days
  print(today)
  print(future_date)
  # upcoming = Coaster.objects.filter(date_opened__isnull=False).filter(date_opened__range=[today, future_date]).order_by('date_opened__month', 'date_opened__day')[:10]
  upcoming = Coaster.objects.filter(date_opened__isnull=False, date_opened__month__gte=today.month, date_opened__day__gte=today.day).order_by('date_opened__month', 'date_opened__day')[:10]
  print(Coaster.objects.filter(title__isnull=True).count())
  return render(request, 'coasters/home.html', { 'upcoming': upcoming })

# Coasters Index
def coasters(request):
  page = request.GET.get('page', '1')
  page_int = int(page)
  print(page)
  coasters = Coaster.objects.order_by('title')
  paginator = Paginator(coasters, 20)
  num_pages = paginator.num_pages

  if num_pages <= 11 or page_int <= 6:  # case 1 and 2
    pages = [x for x in range(1, min(num_pages + 1, 12))]
  elif page_int > num_pages - 6:  # case 4
    pages = [x for x in range(num_pages - 10, num_pages + 1)]
  else:  # case 3
    pages = [x for x in range(page_int - 5, page_int + 6)]

  return render(request, 'coasters/coasters.html', { 'coasters': paginator.get_page(page), 'pages': pages })

# Coaster Detail
def coaster(request, id):
  coaster = get_object_or_404(Coaster, id=id)
  return render(request, 'coasters/coaster.html', {'coaster': coaster})

# CSV Upload
def csv_upload(request):
  if request.method == 'POST':
    print(request.FILES)
    return  render(request, 'coasters/csv-upload.html', { 'upload_succeeded': True})
  print(request.method)
  return render(request, 'coasters/csv-upload.html', {})
