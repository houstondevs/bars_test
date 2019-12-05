from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from .forms import RecruitForm, SithChoiceForm
from .models import Question, Recruit, Answer, Sith


def main(request):
    return render(request, 'main_page.html')


def recruit_information(request):
    if request.method == "POST":
        form = RecruitForm(data=request.POST)
        if form.is_valid():
            recruit = form.save()
            request.session['id_of_recruit'] = recruit.id
            return redirect(to='quiz')
    else:
        form = RecruitForm()
    return render(request, 'recruit.html', context={'form': form})


def quiz(request):
    questions = Question.objects.all()
    recruit = Recruit.objects.get(pk=request.session['id_of_recruit'])
    if request.method == 'POST':
        for question in questions:
            answer = Answer.objects.create(recruit=recruit, question=question, answer=request.POST.get(question.unique_code))
            answer.save()
        del request.session['id_of_recruit']
        return redirect(to='main_page')
    return render(request, 'quiz.html', context={'questions': questions, 'recruit': recruit})


def sith(request):
    if request.method == 'POST':
        form = SithChoiceForm(data=request.POST)
        if form.is_valid():
            request.session['id_of_sith'] = form.data.get('sith')
            return redirect(to='recruits_without_hand')
    else:
        form = SithChoiceForm()
        return render(request, 'sith.html', context={'form': form})


def recruits_withous_hand(request):
    recruits = Recruit.objects.filter(shadow=False)
    return render(request, 'recruits_withoud_hand.html', context={'recruits': recruits})


def accept_recruit(request):
    sith = Sith.objects.get(pk=request.session['id_of_sith'])
    if sith.recruit.count() < 3:
        recruit = Recruit.objects.get(pk=request.session['id_of_recruit'])
        recruit.master = sith
        recruit.shadow = True
        recruit.save()
        email = EmailMessage(subject="Вас выбрали!", body=f'{sith.name} избрал вас! Теперь вы рука тени!', to=[recruit.email])
        email.send()
    del request.session['id_of_sith']
    del request.session['id_of_recruit']
    return redirect(to='main_page')


def recruit_page(request, pk):
    recruit = Recruit.objects.get(pk=pk)
    request.session['id_of_recruit'] = recruit.pk
    answers = Answer.objects.filter(recruit=recruit)
    return render(request, 'recruit_page.html', context={'recruit':recruit, 'answers': answers})


def sith_shodow_count(request):
    siths = Sith.objects.all()
    return render(request, 'sith_shadow_count.html', context={"siths":siths})