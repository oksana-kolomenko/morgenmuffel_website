from django.shortcuts import render

from menu.models import Category
from pages.models import TeamMember


def home(request):
    team_members = TeamMember.objects.all()
    menu_categories = Category.objects.prefetch_related(
        'subcategories__menu_items'
    ).all()

    # Filter out categories and subcategories without items
    filtered_categories = []
    for category in menu_categories:
        # Keep subcategories that have at least one menu item
        subcategories_with_items = [sub for sub in category.subcategories.all() if sub.menu_items.exists()]
        if subcategories_with_items:
            # Assign filtered subcategories back to category
            category.subcategories_filtered = subcategories_with_items
            filtered_categories.append(category)

    return render(request, "home.html", {
        "team_members": team_members,
        "menu_categories": filtered_categories
    })


#def team(request):
#    members = TeamMember.objects.all()
#    return render(request, 'team.html', {'members': members})
