from accounts.models import CustomUser

def profile_picture(request):
    # Add the user's profile picture to the context if the user is authenticated
    if request.user.is_authenticated:
        profile_image = request.user.image if hasattr(request.user, 'image') else None
        print('profile_image==== context=',profile_image)
        return {'profile_image': profile_image}
    return {}
