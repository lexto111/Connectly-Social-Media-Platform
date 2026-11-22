from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from .models import Post, Profile, Comment, Like, Follow, Notification
from .forms import ProfileUpdateForm


def home(request):
    posts = Post.objects.select_related('user').prefetch_related(
        'likes',
        'comments',
        'comments__user'
    )

    liked_post_ids = []

    if request.user.is_authenticated:
        liked_post_ids = Like.objects.filter(
            user=request.user
        ).values_list('post_id', flat=True)

    return render(request, 'home.html', {
        'posts': posts,
        'liked_post_ids': liked_post_ids,
    })


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def profile(request, username):
    profile_user = get_object_or_404(User, username=username)

    user_posts = Post.objects.filter(user=profile_user)

    is_following = Follow.objects.filter(
        follower=request.user,
        following=profile_user
    ).exists()

    return render(request, 'profile.html', {
        'profile_user': profile_user,
        'profile': profile_user.profile,
        'posts': user_posts,
        'is_following': is_following,
        'followers_count': profile_user.followers.count(),
        'following_count': profile_user.following.count(),
    })

@login_required
@require_POST
def toggle_follow(request, username):
    profile_user = get_object_or_404(User, username=username)

    if request.user != profile_user:

        follow = Follow.objects.filter(
            follower=request.user,
            following=profile_user
        )

        if follow.exists():
            follow.delete()

        else:
            Follow.objects.create(
                follower=request.user,
                following=profile_user
            )

            Notification.objects.create(
                recipient=profile_user,
                sender=request.user,
                notification_type='follow',
                message=f'{request.user.username} started following you.'
            )
    return redirect('profile', username=username)

@login_required
def followers_list(request, username):
    profile_user = get_object_or_404(User, username=username)

    followers = Follow.objects.filter(
        following=profile_user
    ).select_related('follower')

    return render(request, 'followers.html', {
        'profile_user': profile_user,
        'connections': followers,
        'connection_type': 'Followers',
    })

@login_required
def following_list(request, username):
    profile_user = get_object_or_404(User, username=username)

    following = Follow.objects.filter(
        follower=profile_user
    ).select_related('following')

    return render(request, 'followers.html', {
        'profile_user': profile_user,
        'connections': following,
        'connection_type': 'Following',
    })

@login_required
def create_post(request):
    if request.method == 'POST':
        caption = request.POST.get('caption')
        image = request.FILES.get('image')

        if caption:
            Post.objects.create(
                user=request.user,
                caption=caption,
                image=image
            )
            return redirect('home')

    return render(request, 'create_post.html')

@login_required
@require_POST
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    like, created = Like.objects.get_or_create(
        post=post,
        user=request.user
    )

    if not created:
        like.delete()

    return redirect('home')

@login_required
@require_POST
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    text = request.POST.get('text', '').strip()

    if text:
        Comment.objects.create(
            post=post,
            user=request.user,
            text=text
        )

    return redirect('home')

@login_required
def edit_profile(request):
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile', username=request.user.username)

    else:
        form = ProfileUpdateForm(instance=profile)

    return render(request, 'edit_profile.html', {
        'form': form
    })
@login_required
def explore(request):
    query = request.GET.get('q', '')

    users = User.objects.exclude(
        id=request.user.id
    )

    if query:
        users = users.filter(
            username__icontains=query
        )

    return render(request, 'explore.html', {
        'users': users,
        'query': query,
    })