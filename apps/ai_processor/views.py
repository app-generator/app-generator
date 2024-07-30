from django.shortcuts import render,redirect , get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests
import os
import anthropic
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json
from dotenv import load_dotenv
from .models import ChatThread, ChatMessage , AnonymousChatIP
from apps.common.models import Tag
from django.utils.text import slugify

load_dotenv()
# Create your views here.

# AI Globals
ANTHROPIC_API_KEY     = os.getenv('ANTHROPIC_API_KEY')
ANTHROPIC_TOKENS      = 200
ANTHROPIC_MODEL       = "claude-3-5-sonnet-20240620"
ANTHROPIC_TEMPERATURE = 0

def teach_me(request, tag=None):

    if tag and Tag.objects.filter(name=tag).exists():
        tag = tag.capitalize()
    else:     
        tag = 'eLearning'

    if request.user.is_authenticated:
        threads = ChatThread.objects.filter(user=request.user).order_by('-id') 
        
        context = {
            'threads': threads,
            'page_title': 'Ai Processor (Asistent AI) - ' + tag,
            'tag': tag,
        }
        return render(request, 'ai/teach_me.html', context)
    else:
        context = {
            'page_title': 'Ai Processor (Asistent AI) - ' + tag,
            'tag': tag,
        }
        return render(request, 'ai/teach_me.html', context)


def create_message(message_content, tag, lang):

    lang = 'English'

    if not message_content:
        raise ValueError("Message content must be non-empty")
    
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)


    system_message  = 'You are a Programming Senior who assists the users in learning programming. Assume they are beginners.'
    
    if tag:
        system_message += f"You are an Programming Senior. The responses Respond only with short paragraph in English regarding {tag}." 

    message = client.messages.create(
        model=ANTHROPIC_MODEL,
        max_tokens=ANTHROPIC_TOKENS,
        temperature=ANTHROPIC_TEMPERATURE,
        system=system_message,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": message_content
                    }
                ]
            }
        ]
    )
    generated_text = message.content[-1].text
    return generated_text 

@csrf_exempt
def ask_question(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        question = data.get('question')
        thread_id = data.get('thread_id')
        tag = data.get('tag_name')
        lang = data.get('language')

        user = request.user if request.user.is_authenticated else None
        ip_address = request.META.get('REMOTE_ADDR') 

        try:
            if not request.user.is_authenticated:
                ip_limit, created = AnonymousChatIP.objects.get_or_create(ip_address=ip_address)
                if ip_limit.questions_asked >= 10:
                    return JsonResponse({'error': 'The maximum number of questions has been reached (10) - You must activate a PRO account'}, status=406)

            if not question:
                return JsonResponse({'error': 'The question must be well formulated'}, status=400)

            if thread_id:
                thread = get_object_or_404(ChatThread, id=thread_id)

            else:
                thread = ChatThread.objects.create(user=user, title=question)

            response_text = create_message(question, tag , lang)
            message= ChatMessage.objects.create(thread=thread, user=user, message=question, response=response_text)
            if message:
                message.slug = f"{slugify(message.message)}-{message.pk}"
                message.save()
                
            tag_obj = Tag.objects.filter(name=tag).first()
            if tag_obj:
                message.tags.add(tag_obj)

            if not request.user.is_authenticated:
                ip_limit.questions_asked += 1
                ip_limit.save()

            return JsonResponse({'response': response_text, 'thread_id': thread.id})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

@login_required
def thread_messages(request, thread_id):
    thread = get_object_or_404(ChatThread, id=thread_id, user=request.user)
    messages = thread.messages.all().order_by('timestamp')
    return JsonResponse({'messages': [{'user': msg.user.username, 'message': msg.message, 'response': msg.response, 'timestamp': msg.timestamp} for msg in messages]})


@login_required
def question_list(request,tag=None):
    messages = ChatMessage.objects.all().order_by('-timestamp')
    if tag:
        tag_obj = get_object_or_404(Tag, name=tag)
        messages = messages.filter(tags=tag_obj)

    context = {
        'messages': messages
    }

    return render(request, 'ai/question_list.html', context)
