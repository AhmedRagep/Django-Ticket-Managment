from django.shortcuts import get_object_or_404, redirect, render
import datetime
from django.contrib import messages
from .models import Tiecket
from .forms import CreateTicketForm, UpdateTicketForm
from users.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def ticket_detail(request,pk):
    ticket = get_object_or_404(Tiecket, id=pk)
    # هاتلي اليوزر اللي باسم صاحب التكت
    t = User.objects.get(username=ticket.created_by)
    # هاتلي كل التكت اللي عملها اليوزر
    tickets_per_user = t.created_by.all()
    return render(request, 'ticket_detail.html', {'ticket':ticket,'tickets_per_user':tickets_per_user})


@login_required
def create_ticket(request):
    if request.method == 'POST':
        form = CreateTicketForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.created_by = request.user
            # التكت الجديد ياخذ قيمه انه جديد
            var.ticket_status = 'Pending'
            var.save()
            messages.info(request, 'Your Ticket Has Been Successfully Created')
            return redirect('dashboard')
        else:
            messages.warning(request, 'You Have Error Please Check Form')    
            return redirect('create_ticket')
    else:
        form = CreateTicketForm()
        return render(request,'create_ticket.html',{'form':form})
    



@login_required
def update_ticket(request,pk):
    ticket = get_object_or_404(Tiecket, id=pk)
    if not ticket.resolved:
      if request.method == 'POST':
          form = UpdateTicketForm(request.POST, instance=ticket)
          if form.is_valid():
              form.save()
              messages.info(request, 'Your Ticket Has Been Updated Successfully')
              return redirect('dashboard')
          else:
              messages.warning(request, 'You Have Error Please Check Form')    
              # return redirect('create_ticket')
      else:
          form = UpdateTicketForm(instance=ticket)
          return render(request,'update_ticket.html',{'form':form})
    else:
        messages.warning(request, 'You Canot make any changes')    
        return redirect('dashboard')

@login_required
def all_tickets(request):
    # عرض التكت الخاصة باليوزر الحالي
    tickets = Tiecket.objects.filter(created_by=request.user).order_by('-date_created')
    return render(request, 'all_tickets.html', {'tickets':tickets})

@login_required
def ticket_queue(request):
    # عرض التكت الجديدة او الغير مستخدمه
    tickets = Tiecket.objects.filter(ticket_status='Pending')
    return render(request, 'ticket_queue.html', {'tickets':tickets})

@login_required
def accept_ticket(request,pk):
    # هات التكت المحدد
    ticket = get_object_or_404(Tiecket, id=pk)
    # خلي فيه اليوزر الحالي
    ticket.assigned_to = request.user
    # اجعله نشط
    ticket.ticket_status = 'Active'
    # وقت النشاط دلوقتي
    ticket.accepted_date = datetime.datetime.now()
    ticket.save()
    messages.info(request,'Ticket Hsd been Accepted')
    return redirect('workspace')

@login_required
def closed_ticket(request,pk):
    # هات التكت المحدد
    ticket = get_object_or_404(Tiecket, id=pk)
    # قيمه مغلقه
    ticket.resolved = True
    # تم اخذه
    ticket.ticket_status = 'Completed'
    # التاريخ دلوقتي
    ticket.accepted_date = datetime.datetime.now()
    ticket.save()
    messages.info(request,'Ticket Hsd been Closed')
    return redirect('ticket_queue')


@login_required
def workspace(request):
    # هاتلي التكت اللي باليوزر الحالي ولسه مفتوحه
    tickets = Tiecket.objects.filter(assigned_to=request.user, resolved=False)
    return render(request,'workspace.html', {'tickets':tickets})


@login_required
def all_closed_tickets(request):
    # هاتلي التكت اللي باليوزر الحالي ومغلقه
    tickets = Tiecket.objects.filter(assigned_to=request.user, resolved=True)
    return render(request,'all_closed_tickets.html', {'tickets':tickets})