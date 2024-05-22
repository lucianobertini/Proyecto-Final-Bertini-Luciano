from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Message
from .forms import MessageForm

@login_required
def inbox(request):
    messages = Message.objects.filter(recipient=request.user)
    return render(request, 'messaging/inbox.html', {'messages': messages})

@login_required
def sent_messages(request):
    messages = Message.objects.filter(sender=request.user)
    return render(request, 'messaging/sent_messages.html', {'messages': messages})

@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return redirect('inbox')
    else:
        form = MessageForm()
    return render(request, 'messaging/send_message.html', {'form': form})

@login_required
def reply_message(request, message_id):
    return redirect('inbox')

@login_required
def delete_message(request, message_id):
    return redirect('inbox')


@login_required
def delete_message(request, message_id):
    message = get_object_or_404(Message, pk=message_id)
    try:
        message.delete()
    except Exception as e:
        print("Error al eliminar el mensaje:", e)
    return redirect('inbox')