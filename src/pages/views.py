from django.shortcuts import render

from pages.models import TeamMember


def home(request):
    team_members = TeamMember.objects.all()  # Or filter if needed
    return render(request, "home.html", {
        "team_members": team_members
    })


#def team(request):
#    members = TeamMember.objects.all()
#    return render(request, 'team.html', {'members': members})
