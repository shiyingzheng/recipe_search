from django.shortcuts import get_object_or_404, render, redirect
from app.models import UserProfile
from django.contrib.auth.models import User
from app.forms import UserForm, UserProfileForm
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

@login_required
def userprofile_update(request):
    profile_obj = request.user.profile
    if request.POST:
        profile_form = UserProfileForm(data=request.POST, instance=profile_obj)
        profile_form.actual_user = request.user

        if profile_form.is_valid():
            profile_form.save()
            return render(request, 'users/update_success.html')
    else:
        profile_form = UserProfileForm(instance=profile_obj)

    return render(request, 'users/update.html',
        {'profile_form': profile_form})




#            user = request.user
#            user_form = UserForm(data=request.POST, instance = user)
#            user_post = user_form.save()

#            user_post.set_password(user_post.password)
#            user_post.save()

#            if 'picture' in request.FILES:
#                profile_post.picture = request.FILES['picture']
#            profile_post.save()

#            valid = True

#        else:
#            print(user_form.errors, profile_form.errors)

#    userprofile = request.user.profile
#    profile_form = UserProfileForm(data=request.POST, instance = userprofile)
#    profile_post = profile_form.save()

#    user = request.user
#    user_form = UserForm(data=request.POST, instance = user)
    #user_post = user_form.save()

#    return render(request, 'users/update.html',
#        {'user_form': user_form,'profile_form': profile_form, 'valid': valid})

        #'user_form': user_form,
