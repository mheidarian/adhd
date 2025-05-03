from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Test, Question, Choice, Result, Answer
from .forms import AnswerForm

# Create your views here.

@login_required
def test_list(request):
    tests = Test.objects.all()
    return render(request, 'assessment/test_list.html', {'tests': tests})

@login_required
def test_detail(request, pk):
    test = get_object_or_404(Test, pk=pk)
    return render(request, 'assessment/test_detail.html', {'test': test})

@login_required
def take_test(request, pk):
    test = get_object_or_404(Test, pk=pk)
    questions = test.questions.all()
    
    if request.method == 'POST':
        # جمع‌آوری تمام پاسخ‌ها
        score = 0
        result = Result.objects.create(user=request.user, test=test, score=0)
        
        for question in questions:
            choice_id = request.POST.get(f'question_{question.id}')
            if choice_id:
                choice = Choice.objects.get(id=choice_id)
                score += choice.score
                Answer.objects.create(
                    result=result,
                    question=question,
                    choice=choice
                )
        
        # به‌روزرسانی امتیاز نهایی
        result.score = score
        result.save()
        
        # ارسال ایمیل نتیجه به مدیر
        result.send_result_email()
        
        return redirect('test_result', result_id=result.id)
    
    # ایجاد فرم‌ها برای تمام سوالات
    forms = []
    for question in questions:
        form = AnswerForm(question=question)
        forms.append({'form': form, 'question': question})
    
    return render(request, 'assessment/take_test.html', {
        'test': test, 
        'forms': forms,
        'total_questions': len(questions),
    })

@login_required
def test_result(request, result_id):
    result = get_object_or_404(Result, id=result_id, user=request.user)
    return render(request, 'assessment/test_result.html', {'result': result})

@login_required
def test_guide(request):
    return render(request, 'assessment/test_guide.html')
