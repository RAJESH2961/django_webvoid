from django.shortcuts import render,redirect
from django.core.mail import send_mail

# Create your views here.
def home(req):
    return render(req,'index.html')
# def contact(req):
#     return render(req,'contact.html')



def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        send_mail(
            subject,
            f'Name: {name}\nEmail: {email}\nMessage: {message}',
            email,  # Sender's email address
            ['grajesh2906@gmail.com'],  # Recipient's email address
            fail_silently=False,
        )
        return redirect('successpage')  # Redirect to a success page
    else:
        return render(request, 'contact.html')

def successpage(req):
    return render(req,'successpage.html')


        # Rest of your code goes here
   
    #     ''' 
    #     send_mail('subject',
    #               'message',
    #               'grajesh2906@gmail.com',
    #               ('email','grajesh2961@gmail.com'),
    #               fail_silently=False)
    #     #return  HttpResponse("Email Sent")
    #     return render(request,'user_details.html') 
    #     '''
    
    #     send_mail(
    #         'Hey,There',  # subject
    #         'Im a Rajesh Gangadharam A Passionate Computer science student at Xyz Univercity',  # body
    #         'grajesh2906@gmail.com',  # sender Email Address
    #         ['grajesh2907@gmail.com', 'grajesh2961@gmail.com'],  # It will add CC to all members
    #         fail_silently=False
    #     )
    
    # #return HttpResponse("Email sent Successfully")
    # alert_message="Email sent successfully"
    # return render(request, 'index.html',{'alert_message':alert_message})

    # def iframe_page(request):
    # # Render the webpage content (replace this with your own logic)
    
    #     return render(request,'contact.html')
def iframe(req):
    return redirect(req,'contact.html')