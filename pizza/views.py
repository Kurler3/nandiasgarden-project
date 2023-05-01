from django.shortcuts import render
from .forms import PizzaForm

# Create your views here.

def home(request):
    return render(request, 'pizza/home.html')

def order(request):
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST) # Fill a new form with the data
        
        # Check if the form is valid
        if filled_form.is_valid():
            
            clean_data = filled_form.cleaned_data

            print(clean_data)

            # Create a note to send back to client
            note = 'Thanks for ordering! Your %s %s and %s pizza is on its way!' %(clean_data['size'], clean_data['topping1'], clean_data['topping2'])

            new_form = PizzaForm()
                
            return render(
                request, 
                'pizza/order.html', 
                {
                    'pizza_form': new_form, 
                    'note': note
                })          
    else:
        form = PizzaForm() 
        return render(request, 'pizza/order.html', {'pizza_form': form})
