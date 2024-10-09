from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from pcell import views

urlpatterns = [
                  path('', views.index, name="index"),
                  path('admin_login', views.admin_login, name="admin_login"),
                  path('admin_home', views.admin_home, name='admin_home'),
                  path('recruiter_login', views.recruiter_login, name="recruiter_login"),
                  path('recruiter_signup', views.recruiter_signup, name="recruiter_signup"),
                  path('recruiter_home', views.recruiter_home, name="recruiter_home"),
                  path('user_login', views.user_login, name="user_login"),
                  path('user_signup', views.user_signup, name="user_signup"),
                  path('user_home', views.user_home, name="user_home"),
                  path('Logout', views.Logout, name="Logout"),
                  path('view_users', views.view_users, name="view_users"),
                  path('add_job', views.add_job, name="add_job"),
                  path('edit_job/<int:pid>', views.edit_job, name="edit_job"),
                  path('change_companylogo/<int:pid>', views.change_companylogo, name="change_companylogo"),
                  path('delete_job/<int:pid>', views.delete_job, name="delete_job"),
                  path('job_list',views.job_list, name="job_list"),
                  path('delete_user/<int:pid>', views.delete_user, name="delete_user"),
                  path('delete_recruiter/<int:pid>', views.delete_recruiter, name="delete_recruiter"),
                  path('view_recruiters', views.view_recruiters, name="view_recruiters"),
                  path('recruiter_pending', views.recruiter_pending, name="recruiter_pending"),
                  path('recruiter_accept', views.recruiter_accept, name="recruiter_accept"),
                  path('recruiter_reject', views.recruiter_reject, name="recruiter_reject"),
                  path('change_status/<int:pid>', views.change_status, name="change_status"),
                  path('change_passworduser', views.change_passworduser, name="change_passworduser"),
                  path('change_passwordadmin', views.change_passwordadmin, name="change_passwordadmin"),
                  path('change_passwordrecruiter', views.change_passwordrecruiter, name="change_passwordrecruiter"),
                  path('latest_jobs', views.latest_jobs, name="latest_jobs"),
                  path('user_joblist', views.user_joblist, name="user_joblist"),
                  path('job_detail/<int:pid>', views.job_detail, name="job_detail"),
                  path('applyforjob/<int:pid>', views.applyforjob, name="applyforjob"),
                  path('applied_candidatelist',views.applied_candidatelist,name="applied_candidatelist"),
                  path('contact',views.contact,name="contact"),
                  path('admin_job', views.admin_job, name="admin_job"),
                  path('admin_job_detail/<int:pid>', views.admin_job_detail, name="admin_job_detail"),
                  path('ticket_list',views.ticket_list,name="ticket_list"),
                  path('recruiter_ticket',views.recruiter_ticket,name="recruiter_ticket"),
                  path('student_ticket',views.student_ticket,name="student_ticket"),
                  path('feedback_list', views.feedback_list, name="feedback_list"),
                  path('recruiter_feedback', views.recruiter_feedback, name="recruiter_feedback"),
                  path('student_feedback', views.student_feedback, name="student_feedback"),
                  path('makepayment',views.makepayment),
                  path('paymentsuccess',views.paymentsuccess),
                  path('test_email', views.test_email, name='test_email'),

 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)