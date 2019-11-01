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
            instance.user2 = request.user
            instance.save()

            TwoYears = form.cleaned_data['TwoYears']
            Category = form.cleaned_data['Category']
            SubCategory = form.cleaned_data['SubCategory']
            DocType = form.cleaned_data['DocType']
            form = NatForm()

            if int(TwoYears) * 1 == 1:
                U = UserProfile.objects.get(user=request.user)
                x = 10 * int(Category) + int(SubCategory)
                U.TotalCredits += n[x]
                U.save()

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
            instance.user6 = request.user
            instance.save()

            OneYear = form.cleaned_data['OneYear']
            Category = form.cleaned_data['Category']
            Level = form.cleaned_data['Level']
            Position = form.cleaned_data['Position']
            DocType = form.cleaned_data['DocType']
            form = Gameform()

            h = 0
            if int(Position) == 1:
                if int(Level) in [1, 2, 3]:
                    h += 10
                elif int(Level) in [4, 5]:
                    h += 20
            elif int(Position) == 2:
                if int(Level) in [1, 2, 3]:
                    h += 8
                elif int(Level) in [4, 5]:
                    h += 16
            elif int(Position) == 3:
                if int(Level) in [1, 2, 3]:
                    h += 5
                elif int(Level) in [4, 5]:
                    h += 12

            if int(OneYear) * 1 == 1:
                U = UserProfile.objects.get(user=request.user)
                x = 10 * int(Category) + int(Level)
                U.TotalCredits += (s[x] + h)
                U.save()

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
            instance.user3 = request.user
            instance.save()

            OneYear = form.cleaned_data['OneYear']
            Category = form.cleaned_data['Category']
            Level = form.cleaned_data['Level']
            Position = form.cleaned_data['Position']
            DocType = form.cleaned_data['DocType']
            form = Cultform()

            h = 0
            if int(Position) == 1:
                if int(Level) in [1, 2, 3]:
                    h += 10
                elif int(Level) in [4, 5]:
                    h += 20
            elif int(Position) == 2:
                if int(Level) in [1, 2, 3]:
                    h += 8
                elif int(Level) in [4, 5]:
                    h += 16
            elif int(Position) == 3:
                if int(Level) in [1, 2, 3]:
                    h += 5
                elif int(Level) in [4, 5]:
                    h += 12

            if int(OneYear) * 1 == 1:
                U = UserProfile.objects.get(user=request.user)
                x = 10 * int(Category) + int(Level)
                U.TotalCredits += (c[x] + h)
                U.save()

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
            instance.user4 = request.user
            instance.save()

            Category = form.cleaned_data['Category']
            Level = form.cleaned_data['Level']
            DocType = form.cleaned_data['DocType']
            form = Profform()

            U = UserProfile.objects.get(user=request.user)
            if int(Category) == 1 or int(Category) == 3:
                x = 10 * int(Category) + int(Level)
            elif Category != 0:
                x = 10 * int(Category)
            U.TotalCredits += p[x]
            U.save()

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
            instance.user5 = request.user
            instance.save()

            Category = form.cleaned_data['Category']
            DocType = form.cleaned_data['DocType']
            form = Entreform()

            U = UserProfile.objects.get(user=request.user)
            x = int(Category)
            U.TotalCredits += e[x]
            U.save()

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
            instance.user1 = request.user
            instance.save()

            Category = form.cleaned_data['Category']
            SubCategory = form.cleaned_data['SubCategory']
            DocType = form.cleaned_data['DocType']
            form = LeadForm()

            U = UserProfile.objects.get(user=request.user)
            x = 10 * int(Category) + int(SubCategory)
            U.TotalCredits += l[x]
            U.save()

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

            FirstName = form.cleaned_data['FirstName']
            LastName = form.cleaned_data['LastName']
            Class = form.cleaned_data['Class']
            Semester = form.cleaned_data['Semester']
            form = RegistrationForm2()
            #return redirect('/account/profile/')
            args = {'form': form, 'FirstName': FirstName, 'LastName': LastName, 'Class': Class, 'Semester': Semester}
            return render(request, self.template_name, args)

    # def put(self, request, id=None):
    #     userprofile = get_object_or_404(UserProfile, id=id)
    #     form = RegistrationForm2(request.POST, instance=userprofile)
    #     if form.is_valid():
    #         instance = form.save(commit=False)
    #         instance.user = request.user
    #         instance.save()
    #
    #         return redirect('/account/profile/')

O = RegView()

@login_required
def profile(request):
    form = RegistrationForm(request.POST)
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
            # return render(request, 'accounts/reg_form_2.html', {'form': form})
    else:
         pass

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
    U = UserProfile.objects.get(user=request.user)
    y = 10 * int(natpage.Category) + int(natpage.SubCategory)
    if int(natpage.TwoYears) * 1 == 1:
        U.TotalCredits -= n[y]

    if request.method == 'POST':
        form = NatForm(request.POST, instance=natpage)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()

            TwoYears = form.cleaned_data['TwoYears']
            Category = form.cleaned_data['Category']
            SubCategory = form.cleaned_data['SubCategory']

            if int(TwoYears) * 1 == 1:
                x = 10 * int(Category) + int(SubCategory)
                U.TotalCredits += n[x]
                U.save()

            return redirect('/account/uploads/')
    else:
        form = NatForm(instance=natpage)
        args = {'form': form}
        return render(request, 'accounts/edit_natpage.html', args)

@login_required
def edit_gamepage(request, id):
    gamepage = get_object_or_404(GamePage, id=id)
    U = UserProfile.objects.get(user=request.user)
    y = 10 * int(gamepage.Category) + int(gamepage.Level)

    h1 = 0
    if int(gamepage.Position) == 1:
        if int(gamepage.Level) in [1, 2, 3]:
            h1 += 10
        elif int(gamepage.Level) in [4, 5]:
            h1 += 20
    elif int(gamepage.Position) == 2:
        if int(gamepage.Level) in [1, 2, 3]:
            h1 += 8
        elif int(gamepage.Level) in [4, 5]:
            h1 += 16
    elif int(gamepage.Position) == 3:
        if int(gamepage.Level) in [1, 2, 3]:
            h1 += 5
        elif int(gamepage.Level) in [4, 5]:
            h1 += 12

    if int(gamepage.OneYear) * 1 == 1:
        U.TotalCredits -= (s[y] + h1)

    if request.method == 'POST':
        form = Gameform(request.POST, instance=gamepage)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()

            OneYear = form.cleaned_data['OneYear']
            Category = form.cleaned_data['Category']
            Level = form.cleaned_data['Level']
            Position = form.cleaned_data['Position']

            h = 0
            if int(Position) == 1:
                if int(Level) in [1, 2, 3]:
                    h += 10
                elif int(Level) in [4, 5]:
                    h += 20
            elif int(Position) == 2:
                if int(Level) in [1, 2, 3]:
                    h += 8
                elif int(Level) in [4, 5]:
                    h += 16
            elif int(Position) == 3:
                if int(Level) in [1, 2, 3]:
                    h += 5
                elif int(Level) in [4, 5]:
                    h += 12

            if int(OneYear) * 1 == 1:
                x = 10 * int(Category) + int(Level)
                U.TotalCredits += (s[x] + h)
                print(s[x] + h)
                print(U.TotalCredits)
                U.save()

            return redirect('/account/uploads/')
    else:
        form = Gameform(instance=gamepage)
        args = {'form': form}
        return render(request, 'accounts/edit_gamepage.html', args)

@login_required
def edit_cultpage(request, id):
    cultpage = get_object_or_404(CultPage, id=id)
    U = UserProfile.objects.get(user=request.user)
    y = 10 * int(cultpage.Category) + int(cultpage.Level)

    h1 = 0
    if int(cultpage.Position) == 1:
        if int(cultpage.Level) in [1, 2, 3]:
            h1 += 10
        elif int(cultpage.Level) in [4, 5]:
            h1 += 20
    elif int(cultpage.Position) == 2:
        if int(cultpage.Level) in [1, 2, 3]:
            h1 += 8
        elif int(cultpage.Level) in [4, 5]:
            h1 += 16
    elif int(cultpage.Position) == 3:
        if int(cultpage.Level) in [1, 2, 3]:
            h1 += 5
        elif int(cultpage.Level) in [4, 5]:
            h1 += 12

    if int(cultpage.OneYear) * 1 == 1:
        U.TotalCredits -= (c[y] + h1)

    if request.method == 'POST':
        form = Cultform(request.POST, instance=cultpage)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()

            OneYear = form.cleaned_data['OneYear']
            Category = form.cleaned_data['Category']
            Level = form.cleaned_data['Level']
            Position = form.cleaned_data['Position']

            h = 0
            if int(Position) == 1:
                if int(Level) in [1, 2, 3]:
                    h += 10
                elif int(Level) in [4, 5]:
                    h += 20
            elif int(Position) == 2:
                if int(Level) in [1, 2, 3]:
                    h += 8
                elif int(Level) in [4, 5]:
                    h += 16
            elif int(Position) == 3:
                if int(Level) in [1, 2, 3]:
                    h += 5
                elif int(Level) in [4, 5]:
                    h += 12

            if int(OneYear) * 1 == 1:
                x = 10 * int(Category) + int(Level)
                U.TotalCredits += (c[x] + h)
                U.save()

            return redirect('/account/uploads/')
    else:
        form = Cultform(instance=cultpage)
        args = {'form': form}
        return render(request, 'accounts/edit_cultpage.html', args)

@login_required
def edit_profpage(request, id):
    profpage = get_object_or_404(ProfPage, id=id)
    U = UserProfile.objects.get(user=request.user)
    if int(profpage.Category) == 1 or int(profpage.Category) == 3:
        y = 10 * int(profpage.Category) + int(profpage.Level)
    elif profpage.Category != 0:
        y = 10 * int(profpage.Category)

    if request.method == 'POST':
        form = Profform(request.POST, instance=profpage)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()

            Category = form.cleaned_data['Category']
            Level = form.cleaned_data['Level']

            U.TotalCredits -= p[y]
            if int(Category) == 1 or int(Category) == 3:
                x = 10 * int(Category) + int(Level)
            elif Category != 0:
                x = 10 * int(Category)
            U.TotalCredits += p[x]
            U.save()

            return redirect('/account/uploads/')
    else:
        form = Profform(instance=profpage)
        args = {'form': form}
        return render(request, 'accounts/edit_profpage.html', args)

@login_required
def edit_entrepage(request, id):
    entrepage = get_object_or_404(EntrePage, id=id)
    U = UserProfile.objects.get(user=request.user)
    y = int(entrepage.Category)
    print(y)

    if request.method == 'POST':
        form = Entreform(request.POST, instance=entrepage)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()

            Category = form.cleaned_data['Category']

            U.TotalCredits -= e[y]
            x = int(Category)
            U.TotalCredits += e[x]
            U.save()

            return redirect('/account/uploads/')
    else:
        form = Entreform(instance=entrepage)
        args = {'form': form}
        return render(request, 'accounts/edit_entrepage.html', args)

@login_required
def edit_leadpage(request, id):
    leadpage = get_object_or_404(LeadPage, id=id)
    U = UserProfile.objects.get(user=request.user)
    y = 10 * int(leadpage.Category) + int(leadpage.SubCategory)

    if request.method == 'POST':
        form = LeadForm(request.POST, instance=leadpage)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()

            Category = form.cleaned_data['Category']
            SubCategory = form.cleaned_data['SubCategory']

            U.TotalCredits -= l[y]
            x = 10 * int(Category) + int(SubCategory)
            U.TotalCredits += l[x]
            U.save()

            return redirect('/account/uploads/')
    else:
        form = LeadForm(instance=leadpage)
        args = {'form': form}
        return render(request, 'accounts/edit_leadpage.html', args)

@login_required
def uploads(request):
    l1 = LeadPage.objects.filter(user1=request.user)
    n1 = NatPage.objects.filter(user2=request.user)
    c1 = CultPage.objects.filter(user3=request.user)
    p1 = ProfPage.objects.filter(user4=request.user)
    e1 = EntrePage.objects.filter(user5=request.user)
    g1 = GamePage.objects.filter(user6=request.user)
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
