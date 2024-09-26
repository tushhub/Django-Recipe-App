from django.shortcuts import render, redirect,get_object_or_404
from .models import Recipes

def Recipe_view(request):
    if request.method == "POST":
        data = request.POST
        recipe_img = request.FILES.get('recipe_img')
        recipe_name = data.get("recipe_name")
        recipe_dec = data.get("recipe_dec")
        
        recipe_count = Recipes.objects.count()
        
        
        Recipes.objects.create(
            recipe_img=recipe_img,
            recipe_name=recipe_name,
            recipe_dec=recipe_dec,
        )
        
        return redirect('/veggiesApp/')
    
    
    queryset = Recipes.objects.all()
    context = {'recipes': queryset}
    
    return render(request, 'recipe.html', context)

def show_view(request):

    recipes = Recipes.objects.all()
    
    if request.GET.get('search'):
        recipes=recipes.filter(recipe_name__icontains=request.GET.get('search'))
    return render(request, 'show.html', {'recipes': recipes})
 

def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipes, id=recipe_id)
    recipe.delete()
    return redirect(request,'/veggiesApp/show/') 


def update_recipe(request, recipe_id):
    queryset = Recipes.objects.get(id=recipe_id)
    
    if request.method == "POST":
        data = request.POST
        recipe_name = data.get("recipe_name")
        recipe_img = request.FILES.get("recipe_img")
        recipe_dec = data.get("recipe_dec")

        # Ensure the recipe name is not None or empty
        if recipe_name:
            queryset.recipe_name = recipe_name
        else:
            # Handle the error for missing recipe name
            return render(request, 'update_recipe.html', {'error': 'Recipe name is required', 'recipes': queryset})

        queryset.recipe_dec = recipe_dec
        
        if recipe_img:  # Only update the image if a new one is provided
            queryset.recipe_img = recipe_img

        queryset.save()
        return redirect('/veggiesApp/show/')
    
    context = {'recipes': queryset}
    return render(request, 'update_recipe.html', context)
