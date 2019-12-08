from django.shortcuts import render
from firstapp.forms import ProductForm
from .models import Product
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from matplotlib import pyplot as plt


from django.http import HttpResponse
from matplotlib import pylab
from pylab import *
import PIL, io

# Create your views here.
def index(request):

	if request.method == 'POST':
		# product_data = ProductForm(data=request.POST)
		product_data = ProductForm(request.POST, request.FILES)
		if product_data.is_valid():
			# product_data.save(commit=False)
			# if request.FILES['img']:
			# 	myfile = request.FILES['img']
			# 	fs = FileSystemStorage()
			# 	filename = fs.save(myfile.name, myfile)
			# 	product_data.img = fs.url(filename)
			product_data.save()
	else:
		product_data = ProductForm();
	
	return render(request,'firstapp/index.html',{'product':product_data })


def products(request):
	products = Product.objects.raw('SELECT * FROM firstapp_product')
	plot_x = [22, 23, 24, 25, 26, 27, 28]
	plot_y = [1223, 2633, 6765, 3553, 8765, 7654, 9876]
	# plt.plot(plot_x,plot_y)
	# response = plt.show()

	# Construct the graph
  # t = arange(0.0, 2.0, 0.01)
  # s = sin(2*pi*t)
	plt.plot(plot_x, plot_y)

	xlabel('time (s)')
	ylabel('voltage (mV)')
	title('About as simple as it gets, folks')
	grid(True)

  # Store image in a string buffer
	buffer = io.BytesIO()
	canvas = pylab.get_current_fig_manager().canvas
	canvas.draw()
	pilImage = PIL.Image.frombytes("RGB", canvas.get_width_height(), canvas.tostring_rgb())
	pilImage.save(buffer, "PNG")
	pylab.close()

	# response = HttpResponse(buffer.getvalue(), content_type="image/png")

  # Send buffer in a http response the the browser with the mime type image/png set
	# return render(request,'firstapp/products.html',{'response':response })
	return HttpResponse(buffer.getvalue(), content_type="image/png")

def validate_name(request):
	name = request.GET.get('name',None)
	data = {
		'is_taken': Product.objects.filter(name=name).exists()
	}
	return JsonResponse(data)