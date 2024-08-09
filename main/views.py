from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required
def main(request):
  user = request.user
  context = {'user':user}
  return render(request, "main.html", context)

def logout_view(request):
    logout(request)
    return redirect('/')
  