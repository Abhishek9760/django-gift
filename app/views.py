from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView

from .models import Message
from .forms import MessageForm


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('home')
    template_name = 'app/create_view.html'


#
# class MessageDeleteView(DeleteView):
#     model = Message
#     success_url = reverse_lazy('home')
#     template_name = 'app/delete_view.html'
