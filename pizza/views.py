from django.shortcuts import render
from .forms import PizzaForm, MultiplePizzaForm
from django.forms import formset_factory
from .models import Pizza

# Create your views here.

def home(request):
    return render(request, 'pizza/home.html')

def order(request):
    multiple_form = MultiplePizzaForm()
    
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST) # Fill a new form with the data
        
        # Check if the form is valid
        if filled_form.is_valid():
            
            created_pizza = filled_form.save() # Save the pizza in db
            
            
            
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
                    'note': note,
                    'multiple_form': multiple_form,
                    'created_pizza_pk': created_pizza
                })          
    else:
        form = PizzaForm() 
        return render(
            request, 
            'pizza/order.html', 
            {
                'pizza_form': form,
                'multiple_form': multiple_form
            }
        )


def edit_order(request, pk):
    
    pizza = Pizza.objects.get(pk=pk)
    
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST, instance=pizza)
        
        if filled_form.is_valid():
            filled_form.save()
            
            note = 'Order has been updated.';
            
            return render(
                request,
                'pizza/edit_order.html',
                {
                    'pizza_form': filled_form,
                    'pizza': 'pizza',
                    'note': note,
                }
            )
    else:
        form = PizzaForm(instance=pizza)
        return render(
            request, 
            'pizza/edit_order.html', 
            {'pizza_form': form, 'pizza': pizza}
        )
    
    

def pizzas(request):
    number_of_pizzas = 2
    filled_multiple_pizza_form = MultiplePizzaForm(request.GET)
    
    if filled_multiple_pizza_form.is_valid():
        number_of_pizzas = filled_multiple_pizza_form.cleaned_data['number']
    
    PizzaFormSet = formset_factory(PizzaForm, extra=number_of_pizzas)
    
    formset = PizzaFormSet()
    
    if request.method == 'POST':
        filled_formset = PizzaFormSet(request.POST)
        
        if filled_formset.is_valid():
            
            # Save pizzas
            
            
            for form in filled_formset:
                print(form.cleaned_data['topping1'])
            
            note = 'Pizzas have been ordered!'
            
        else:
            note = 'Order was not created, please try again.'
            
        return render(
            request, 
            'pizza/pizzas.html', 
            {
                'note': note, 
                'formset': formset
            }
        )
    # Get request
    else:
        return render(
            request,
            'pizza/pizzas.html',
            {'formset': formset}
        )