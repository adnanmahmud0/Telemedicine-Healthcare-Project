from .chatbot import get_chatbot_response
from django.shortcuts import render, redirect
from .forms import MessageForm

messages = []


def chat_view(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            sender = 'Bot'
            user = "Me"
            content = form.cleaned_data['content']
            bot_response = get_chatbot_response(content)
            me = {'sender': user, 'content': content}
            message = {'sender': sender, 'content': bot_response}
            # reply = JsonResponse({'bot_response': bot_response})
            messages.append(me)
            messages.append(message)

            return redirect('chat')
    else:
        form = MessageForm()

    return render(request, 'chat.html', {'form': form, 'messages': messages})


from .models import Ambulance


def ambulance(request):
    ambulances = Ambulance.objects.all()
    return render(request, 'ambulance.html', {'all':ambulances})
