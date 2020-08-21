from django.shortcuts import render, redirect, get_object_or_404
from accounts.forms import RegistrationForm2
from django.views.generic import TemplateView
from staff.models import StaffProfile
from accounts.models import User, UserProfile, LeadPage, CultPage, ProfPage, EntrePage, GamePage, NatPage
from accounts.database import *
from django.contrib.admin.views.decorators import staff_member_required
import json
from django.http import JsonResponse


class AdminRegView(TemplateView):
    template_name = 'staff/reg_form.html'

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


@staff_member_required
def home(request):
    O1 = AdminRegView()
    if request.user.is_authenticated:
        if StaffProfile.objects.filter(user=request.user).exists():
            details = StaffProfile.objects.get(user=request.user)
            students = UserProfile.objects.filter(Class=details.Class, Semester=details.Semester)
            args = {'data': details, 'id': request.user.id, 'students': students}
            return render(request, 'staff/home.html', args)
        else:
            if request.method == 'POST':
                return O1.post(request)
            else:
                return O1.get(request)
    else:
         pass


@staff_member_required
def uploads(request, id):
    user = get_object_or_404(User, id=id)
    l1 = LeadPage.objects.filter(user=user)
    n1 = NatPage.objects.filter(user=user)
    c1 = CultPage.objects.filter(user=user)
    p1 = ProfPage.objects.filter(user=user)
    e1 = EntrePage.objects.filter(user=user)
    g1 = GamePage.objects.filter(user=user)
    args = {'lead': l1, 'nat': n1, 'cult': c1, 'prof': p1, 'entr': e1, 'game': g1,
            'l2': l2, 'n2': n2, 'c2': c2, 'p2': p2, 'e2': e2, 'g2': g2, 'user_profile_id': id}
    return render(request, 'staff/uploads.html', args)


@staff_member_required
def view_natpage(request, uid, id):
    natpage = get_object_or_404(NatPage, id=id)
    args = {'O': natpage, 'ref': n2, 'user_profile_id': uid}
    return render(request, 'staff/nat_display.html', args)


@staff_member_required
def view_gamepage(request, uid, id):
    gamepage = get_object_or_404(GamePage, id=id)
    args = {'O': gamepage, 'ref': g2, 'user_profile_id': uid}
    return render(request, 'staff/game_display.html', args)


@staff_member_required
def view_cultpage(request, uid, id):
    cultpage = get_object_or_404(CultPage, id=id)
    args = {'O': cultpage, 'ref': c2, 'user_profile_id': uid}
    return render(request, 'staff/cult_display.html', args)


@staff_member_required
def view_profpage(request, uid, id):
    profpage = get_object_or_404(ProfPage, id=id)
    args = {'O': profpage, 'ref': p2, 'user_profile_id': uid}
    return render(request, 'staff/prof_display.html', args)


@staff_member_required
def view_entrepage(request, uid, id):
    entrepage = get_object_or_404(EntrePage, id=id)
    args = {'O': entrepage, 'ref': e2, 'user_profile_id': uid}
    return render(request, 'staff/entre_display.html', args)


@staff_member_required
def view_leadpage(request, uid, id):
    leadpage = get_object_or_404(LeadPage, id=id)
    args = {'O': leadpage, 'ref': l2, 'user_profile_id': uid}
    return render(request, 'staff/lead_display.html', args)


@staff_member_required
def approve_natpage(request, uid, id):
    natpage = get_object_or_404(NatPage, id=id)
    natpage.Approved = not natpage.Approved
    natpage.save()

    TwoYears = natpage.TwoYears
    Category = natpage.Category
    SubCategory = natpage.SubCategory

    if int(TwoYears) * 1 == 1:
        U = UserProfile.objects.get(user_id=uid)
        x = 10 * int(Category) + int(SubCategory)
        if natpage.Approved:
            U.TotalCredits += n[x]
        else:
            U.TotalCredits -= n[x]
        U.save()

    return redirect('/staff/student-details/{}'.format(uid))


@staff_member_required
def approve_gamepage(request, uid, id):
    gamepage = get_object_or_404(GamePage, id=id)
    gamepage.Approved = not gamepage.Approved
    gamepage.save()

    OneYear = gamepage.OneYear
    Category = gamepage.Category
    Level = gamepage.Level
    Position = gamepage.Position

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
        U = UserProfile.objects.get(user_id=uid)
        x = 10 * int(Category) + int(Level)
        if gamepage.Approved:
            U.TotalCredits += (s[x] + h)
        else:
            U.TotalCredits -= (s[x] + h)
        U.save()

    return redirect('/staff/student-details/{}'.format(uid))


@staff_member_required
def approve_cultpage(request, uid, id):
    cultpage = get_object_or_404(CultPage, id=id)
    cultpage.Approved = not cultpage.Approved
    cultpage.save()

    OneYear = cultpage.OneYear
    Category = cultpage.Category
    Level = cultpage.Level
    Position = cultpage.Position

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
        U = UserProfile.objects.get(user_id=uid)
        x = 10 * int(Category) + int(Level)
        if cultpage.Approved:
            U.TotalCredits += (c[x] + h)
        else:
            U.TotalCredits -= (c[x] + h)
        U.save()

    return redirect('/staff/student-details/{}'.format(uid))


@staff_member_required
def approve_profpage(request, uid, id):
    profpage = get_object_or_404(ProfPage, id=id)
    profpage.Approved = not profpage.Approved
    profpage.save()

    Category = profpage.Category
    Level = profpage.Level

    U = UserProfile.objects.get(user_id=uid)
    x = 0
    if int(Category) == 1 or int(Category) == 3:
        x = 10 * int(Category) + int(Level)
    elif Category != 0:
        x = 10 * int(Category)
    if profpage.Approved:
        U.TotalCredits += p[x]
    else:
        U.TotalCredits -= p[x]
    U.save()

    return redirect('/staff/student-details/{}'.format(uid))


@staff_member_required
def approve_entrepage(request, uid, id):
    entrepage = get_object_or_404(EntrePage, id=id)
    entrepage.Approved = not entrepage.Approved
    entrepage.save()

    Category = entrepage.Category

    U = UserProfile.objects.get(user_id=uid)
    x = int(Category)
    if entrepage.Approved:
        U.TotalCredits += e[x]
    else:
        U.TotalCredits -= e[x]
    U.save()

    return redirect('/staff/student-details/{}'.format(uid))


@staff_member_required
def approve_leadpage(request, uid, id):
    leadpage = get_object_or_404(LeadPage, id=id)
    leadpage.Approved = not leadpage.Approved
    leadpage.save()

    Category = leadpage.Category
    SubCategory = leadpage.SubCategory

    U = UserProfile.objects.get(user_id=uid)
    x = 10 * int(Category) + int(SubCategory)
    if leadpage.Approved:
        U.TotalCredits += l[x]
    else:
        U.TotalCredits -= l[x]
    U.save()

    return redirect('/staff/student-details/{}'.format(uid))


@staff_member_required
def search(request):
    if request.method == 'POST':
        type = int(request.POST.get('type'))
        category = request.POST.get('category')
        subcategory = request.POST.get('subcategory')
        mini = request.POST.get('min')
        maxi = request.POST.get('max')
        if type == 1:
            result = NatPage.objects.all()
        elif type == 2:
            result = GamePage.objects.all()
        elif type == 3:
            result = CultPage.objects.all()
        elif type == 4:
            result = LeadPage.objects.all()
        elif type == 5:
            result = ProfPage.objects.all()
        else:
            result = EntrePage.objects.all()
        if category:
            result = result.filter(Category=int(category))
        if subcategory:
            if type == 4 or type == 6:
                result = result.filter(SubCategory=int(subcategory))
            else:
                result = result.filter(Level=int(subcategory))
        if mini:
            result = result.filter(user__userprofile__TotalCredits__gte=int(mini))
        if maxi:
            result = result.filter(user__userprofile__TotalCredits__lte=int(maxi))
        u = set()
        users = []
        for res in result:
            if res.user not in u:
                u.add(res.user)
                users.append(res.user.userprofile)
        count = len(users)
        users.sort(key=lambda x: x.FirstName)
        args = {'students': users, 'count': count}
        return render(request, 'staff/search_results.html', args)
    return render(request, 'staff/search.html')


# @staff_member_required
# def search_results_ajax(request):
#     try:
#         data = json.loads(request.body)
#     except:
#         return redirect('/')
#     type = int(data['type'])
#     category = data['category']
#     subcategory = data['subcategory']
#     min = data['min']
#     max = data['max']
#     print(type, category, subcategory, min, max)
#     if type == 1:
#         result = NatPage.objects.all()
#     elif type == 2:
#         result = GamePage.objects.all()
#     elif type == 3:
#         result = CultPage.objects.all()
#     elif type == 4:
#         result = LeadPage.objects.all()
#     elif type == 5:
#         result = ProfPage.objects.all()
#     else:
#         result = EntrePage.objects.all()
#     if category:
#         result = result.filter(Category=int(category))
#     if subcategory:
#         if type == 4 or type == 6:
#             result = result.filter(SubCategory=int(subcategory))
#         else:
#             result = result.filter(Level=int(subcategory))
#     if min:
#         result = result.filter(user__userprofile__TotalCredits__gte=int(min))
#     if max:
#         result = result.filter(user__userprofile__TotalCredits__lte=int(max))
#     u = set()
#     users = []
#     for res in result:
#         if res.user not in u:
#             u.add(res.user)
#             userprofile = res.user.userprofile
#             users.append({'user_id': userprofile.user_id, 'FirstName': userprofile.FirstName,
#                           'LastName': userprofile.LastName})
#     return JsonResponse({'result': list(result.values()), 'users': users})
