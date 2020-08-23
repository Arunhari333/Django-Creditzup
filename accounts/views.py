from django.shortcuts import render, redirect, get_object_or_404
from accounts.forms import RegistrationForm, RegistrationForm2, EditprofileForm, \
    LeadForm, Cultform, Profform, Entreform, Gameform, NatForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from accounts.models import User, UserProfile, LeadPage, CultPage, ProfPage, EntrePage, GamePage, NatPage
from accounts.database import *


@login_required
def home(request):
    return render(request, 'accounts/home.html')


class national_initiatives(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/national_initiatives.html'

    def get(self, request):
        form = NatForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):

        form = NatForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('/account')


class sports_games(LoginRequiredMixin, TemplateView):

    template_name = 'accounts/sports_games.html'

    def get(self, request):
        form = Gameform()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = Gameform(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('/account')


class cultural_activities(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/cultural_activities.html'

    def get(self, request):
        form = Cultform()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = Cultform(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('/account')


class prof_self_initiatives(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/prof_self_initiatives.html'

    def get(self, request):
        form = Profform()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = Profform(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('/account')


class Entrepreneurship_innovation(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/Entrepreneurship_innovation.html'

    def get(self, request):
        form = Entreform()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = Entreform(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('/account')


class Leadership_management(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/Leadership_management.html'

    def get(self, request):
        form = LeadForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = LeadForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('/account')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            if User.objects.filter(email=form.cleaned_data.get('email')).exists():
                args = {'error': 'User already exists', 'erlink': '/account/register'}
                return render(request, 'accounts/regerror.html', args)
            else:
                form.save()
                return redirect('/account')
        else:
            args = {'error': 'Password not strong', 'erlink': '/account/register'}
            return render(request, 'accounts/regerror.html', args)
    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'accounts/reg_form.html', args)


class RegView(TemplateView):
    template_name = 'accounts/reg_form_2.html'

    def get(self, request):
        form = RegistrationForm2()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = RegistrationForm2(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('/account/profile/')


@login_required
def profile(request):
    O = RegView()
    if request.user.is_authenticated:
        if UserProfile.objects.filter(user=request.user).exists():
            details = UserProfile.objects.get(user=request.user)
            args = {'data': details, 'id': request.user.id}
            return render(request, 'accounts/profile.html', args)
        else:
            if request.method == 'POST':
                return O.post(request)
            else:
                return O.get(request)

    return redirect('/account')


@login_required
def view_natpage(request, id):
    natpage = get_object_or_404(NatPage, id=id)
    args = {'O': natpage, 'ref': n2}
    return render(request, 'accounts/nat_display.html', args)


@login_required
def view_gamepage(request, id):
    gamepage = get_object_or_404(GamePage, id=id)
    args = {'O': gamepage, 'ref': g2}
    return render(request, 'accounts/game_display.html', args)


@login_required
def view_cultpage(request, id):
    cultpage = get_object_or_404(CultPage, id=id)
    args = {'O': cultpage, 'ref': c2}
    return render(request, 'accounts/cult_display.html', args)


@login_required
def view_profpage(request, id):
    profpage = get_object_or_404(ProfPage, id=id)
    args = {'O': profpage, 'ref': p2}
    return render(request, 'accounts/prof_display.html', args)


@login_required
def view_entrepage(request, id):
    entrepage = get_object_or_404(EntrePage, id=id)
    args = {'O': entrepage, 'ref': e2}
    return render(request, 'accounts/entre_display.html', args)


@login_required
def view_leadpage(request, id):
    leadpage = get_object_or_404(LeadPage, id=id)
    args = {'O': leadpage, 'ref': l2}
    return render(request, 'accounts/lead_display.html', args)


@login_required
def edit_profile(request):
    userprofile1 = UserProfile.objects.get(user_id=request.user.id)
    userprofile = get_object_or_404(UserProfile, id=userprofile1.id)
    if request.method == 'POST':
        form = RegistrationForm2(request.POST, instance=userprofile)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('/account/profile/')
    else:
        form = RegistrationForm2(instance=userprofile)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)


@login_required
def edit_natpage(request, id):
    natpage = get_object_or_404(NatPage, id=id)
    if (natpage.user_id == request.user.id) and (not natpage.Approved):
        if request.method == 'POST':
            form = NatForm(request.POST, request.FILES, instance=natpage)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
                return redirect('/account/uploads/')
        else:
            form = NatForm(instance=natpage)
            args = {'form': form}
            return render(request, 'accounts/edit_natpage.html', args)
    else:
        return redirect('/account/')


@login_required
def edit_gamepage(request, id):
    gamepage = get_object_or_404(GamePage, id=id)
    if (gamepage.user_id == request.user.id) and (not gamepage.Approved):
        if request.method == 'POST':
            form = Gameform(request.POST, request.FILES, instance=gamepage)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
                return redirect('/account/uploads/')
        else:
            form = Gameform(instance=gamepage)
            args = {'form': form}
            return render(request, 'accounts/edit_gamepage.html', args)
    else:
        return redirect('/account/')


@login_required
def edit_cultpage(request, id):
    cultpage = get_object_or_404(CultPage, id=id)
    if (cultpage.user_id == request.user.id) and (not cultpage.Approved):
        if request.method == 'POST':
            form = Cultform(request.POST, request.FILES, instance=cultpage)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
                return redirect('/account/uploads/')
        else:
            form = Cultform(instance=cultpage)
            args = {'form': form}
            return render(request, 'accounts/edit_cultpage.html', args)
    else:
        return redirect('/account/')


@login_required
def edit_profpage(request, id):
    profpage = get_object_or_404(ProfPage, id=id)
    if (profpage.user_id == request.user.id) and (not profpage.Approved):
        if request.method == 'POST':
            form = Profform(request.POST, request.FILES, instance=profpage)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
                return redirect('/account/uploads/')
        else:
            form = Profform(instance=profpage)
            args = {'form': form}
            return render(request, 'accounts/edit_profpage.html', args)
    else:
        return redirect('/account/')


@login_required
def edit_entrepage(request, id):
    entrepage = get_object_or_404(EntrePage, id=id)
    if (entrepage.user_id == request.user.id) and (not entrepage.Approved):
        if request.method == 'POST':
            form = Entreform(request.POST, request.FILES, instance=entrepage)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
                return redirect('/account/uploads/')
        else:
            form = Entreform(instance=entrepage)
            args = {'form': form}
            return render(request, 'accounts/edit_entrepage.html', args)
    else:
        return redirect('/account/')


@login_required
def edit_leadpage(request, id):
    leadpage = get_object_or_404(LeadPage, id=id)
    if (leadpage.user_id == request.user.id) and (not leadpage.Approved):
        if request.method == 'POST':
            form = LeadForm(request.POST, request.FILES, instance=leadpage)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
                return redirect('/account/uploads/')
        else:
            form = LeadForm(instance=leadpage)
            args = {'form': form}
            return render(request, 'accounts/edit_leadpage.html', args)
    else:
        return redirect('/account/')


def delete_natpage(request, id):
    natpage = get_object_or_404(NatPage, id=id)
    U = UserProfile.objects.get(user=request.user)
    if int(natpage.TwoYears) == 1 and natpage.Approved:
        points = nat_point_calc(natpage.Category, natpage.SubCategory)
        U.TotalCredits -= points
        U.save()

    natpage.delete()

    return redirect('/account/uploads/')


def delete_gamepage(request, id):
    gamepage = get_object_or_404(GamePage, id=id)
    U = UserProfile.objects.get(user=request.user)
    points = game_point_calc(gamepage.Category, gamepage.Level)

    if int(gamepage.OneYear) == 1 and gamepage.Approved:
        U.TotalCredits -= points
        U.save()

    gamepage.delete()

    return redirect('/account/uploads/')


def delete_cultpage(request, id):
    cultpage = get_object_or_404(CultPage, id=id)
    U = UserProfile.objects.get(user=request.user)
    points = cult_point_calc(cultpage.Category, cultpage.Level, cultpage.Position)

    if int(cultpage.OneYear) == 1 and cultpage.Approved:
        U.TotalCredits -= points
        U.save()

    cultpage.delete()

    return redirect('/account/uploads/')


def delete_profpage(request, id):
    profpage = get_object_or_404(ProfPage, id=id)
    U = UserProfile.objects.get(user=request.user)
    if profpage.Approved:
        points = prof_point_calc(profpage.Category, profpage.Level)
        U.TotalCredits -= points
        U.save()

    profpage.delete()

    return redirect('/account/uploads/')


def delete_entrepage(request, id):
    entrepage = get_object_or_404(EntrePage, id=id)
    U = UserProfile.objects.get(user=request.user)
    if entrepage.Approved:
        points = entre_point_calc(entrepage.Category)
        U.TotalCredits -= points
        U.save()

    entrepage.delete()

    return redirect('/account/uploads/')


def delete_leadpage(request, id):
    leadpage = get_object_or_404(LeadPage, id=id)
    U = UserProfile.objects.get(user=request.user)
    if leadpage.Approved:
        points = lead_point_calc(leadpage.Category, leadpage.SubCategory)
        U.TotalCredits -= points
        U.save()

    leadpage.delete()

    return redirect('/account/uploads/')


@login_required
def uploads(request):
    user = request.user
    l1 = LeadPage.objects.filter(user=user)
    n1 = NatPage.objects.filter(user=user)
    c1 = CultPage.objects.filter(user=user)
    p1 = ProfPage.objects.filter(user=user)
    e1 = EntrePage.objects.filter(user=user)
    g1 = GamePage.objects.filter(user=user)
    args = {'lead': l1, 'nat': n1, 'cult': c1, 'prof': p1, 'entr': e1, 'game': g1,
            'l2': l2, 'n2': n2, 'c2': c2, 'p2': p2, 'e2': e2, 'g2': g2}
    return render(request, 'accounts/uploads.html', args)


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/account/profile')
        else:
            return redirect('/account/change-password')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)
