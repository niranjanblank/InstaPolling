from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect,reverse, HttpResponse
from .forms import QuestionForm,OptionFormModel
from .models import Question, Option
from django.forms import inlineformset_factory
from datetime import datetime
from django.core.paginator import Paginator

# Create your views here.
def calculate_time_difference(questions):
    for i in questions:
        current_time=datetime.utcnow()
        if abs(current_time.hour-i.date_published.hour) == 1:
            if current_time.minute>i.date_published.minute:
                i.expired=True
        elif abs(current_time.hour-i.date_published.hour)>1:
            i.expired = True
        i.save()
def home(request):
    questions = Question.objects.all().order_by('-date_published')
    calculate_time_difference(questions)
    #Paginator#
    paginator = Paginator(questions,4)
    page = request.GET.get('page')
    questions_list= paginator.get_page(page)
    ##########
    return render(request,'Polls/home.html',{'questions':questions_list})


def index(request):
    return render(request,'Polls/index.html')

def create_question(request):

    if request.method=='POST':
        question_form = QuestionForm(request.POST)
        if question_form.is_valid():
            question=question_form.save()
            return redirect('create-option',poll_id=question.id)

    question_form=QuestionForm()
    return render(request,'Polls/question_form.html',{'form':question_form})

def create_option(request,poll_id):
    # prev_url_data = str(request.META.get('HTTP_REFERER'))
    # same_url_data='http://127.0.0.1:8000/addPoll/'+str(poll_id)
    # if not ((prev_url_data == 'http://127.0.0.1:8000/addPoll/') or (prev_url_data == same_url_data)):
    #     return HttpResponse(status=404)
    question= Question.objects.get(id=poll_id)
    # OptionFormset = inlineformset_factory(Question, Option, fields=('option_title',),can_delete=False,extra=1)
    OptionFormset = inlineformset_factory(Question, Option,form = OptionFormModel,can_delete=False,extra=1)
    if request.method == 'POST':
        formset= OptionFormset(request.POST,instance=question)
        if formset.is_valid():
            formset.save()
        return redirect('create-option', poll_id=question.id)
    formset= OptionFormset(instance=question)
    return render(request,'Polls/option_form.html',{'form':formset,'question':question})

def vote_page(request,poll_id):
    question = Question.objects.get(id=poll_id)
    questions=[question]
    calculate_time_difference(questions)
    if question.expired:
        return redirect('results',poll_id=question.id)
    return render(request,'Polls/voting_page.html',{'question':question})

def vote_function(request,poll_id):
    question=get_object_or_404(Question,pk=poll_id)
    questions = [question]
    calculate_time_difference(questions)
    if not question.expired:
        selected_option = question.option_set.get(pk=request.POST['pollOption'])
        selected_option.votes += 1
        selected_option.save()
    return HttpResponseRedirect(reverse('results',args=(question.id,)))

def results(request,poll_id):
    question = get_object_or_404(Question, pk=poll_id)
    questions = [question]
    calculate_time_difference(questions)
    return render(request, 'Polls/results.html', {'question': question})
