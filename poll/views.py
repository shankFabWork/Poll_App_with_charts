from django.shortcuts import render,redirect
from .models import Question,CheckBox
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import QuestionUpdateForm ,QuestionCreateForm,CheckBoxForm
from django.contrib import messages
from .models import RandomImage
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,'poll/home.html')

@login_required
def update_question(request,id):
    user=User.objects.filter(username=request.user).first()
    data=Question.objects.get(id=id)
    if request.method == 'POST':
        form = QuestionUpdateForm(request.POST,instance=data)
        if form.is_valid():
            messages.success(request,'Question Updated Successfully')
            form.save()
            return redirect('questions_show')

    else: 
        form = QuestionUpdateForm(instance=data)


    context={'data':data,'form':form}
    return render(request,'poll/update_question.html',context)

@login_required
def delete_question(request,id):
    data=Question.objects.get(id=id,user=request.user)
    data.delete()
    return redirect('questions_show')


@login_required
def search_question(request):
    title=request.GET.get('search')
    print(title)
    arr=[]
    if title != None:
        arr=Question.objects.filter(ques_text__icontains=title,user=request.user)
    context={'arr':arr}
    print(arr)        
    return render(request,"poll/search_question.html",context)


@login_required
def global_question(request):
    if request.user.is_superuser:
        arr=User.objects.all()
        context={'arr':arr}
    else:
        data='You are not a super user'
        context={'data':data}

    return render(request,"poll/global_question.html",context)

@login_required
def each_question(request,id):
    if request.method == 'GET':
        question=Question.objects.get(pk=id)
        context={'question':question}
        return render(request,'poll/each_question.html',context)
    else:
        question=Question.objects.get(pk=id)
        print(request.POST)


        if request.POST['option_no'] == 'option1':
            question.choice1_vote=question.choice1_vote+1

        elif request.POST['option_no'] == 'option2':
            question.choice2_vote=question.choice2_vote+1

        elif request.POST['option_no'] == 'option3':
            question.choice3_vote=question.choice3_vote+1

        elif request.POST['option_no'] == 'option4':
            question.choice4_vote=question.choice4_vote+1
        else:
            return render(request,'poll/error_404.html')

        question.save()
        messages.success(request,"Your Vote Saved Sucessfully")
        context={'question':question}
        return render(request,'poll/each_question.html',context)

@login_required
def create_question(request):
    print(request.POST)
    if request.method == 'POST':
        form = QuestionCreateForm(request.POST)
        if form.is_valid():
            # messages.success(request,'Question created Sucessfully')
            ques_obj=Question(
                ques_text=request.POST['ques_text'],
                choice1_text=request.POST['choice1_text'],
                choice2_text=request.POST['choice2_text'],
                choice3_text=request.POST['choice3_text'],
                choice4_text=request.POST['choice4_text'],
                user=request.user)
            ques_obj.save()
            return redirect('questions_show') 
            # return redirect('create_question') 
    else:
        form = QuestionCreateForm()
        context={'form':form}
        return render(request,'poll/create_question.html',context)

@login_required
def questions_show(request):
    if request.method == 'POST':
        return redirect('questions_show')
    else:
        import random
        ques_arr=Question.objects.filter(user=request.user)
        img_arr=RandomImage.objects.all()
        context={'arr':ques_arr}

        return render(request,'poll/questions_show.html',context)

@login_required
def votes_show(request):
    ques_obj=Question.objects.filter(user=request.user)
    context={'arr':ques_obj}
    return render(request,'poll/votes_show.html',context)

@login_required
def global_question_show(request):
    if request.method == 'POST':
        return redirect('global_votes_show')
    else:
        import random
        ques_arr=Question.objects.filter()
        img_arr=RandomImage.objects.all()
        context={'arr':ques_arr}

        return render(request,'poll/global_question_show.html',context)

def global_votes_show(request):
    ques_obj=Question.objects.filter()
    context={
                'arr':ques_obj,
            }
    return render(request,'poll/global_votes_show.html',context)

