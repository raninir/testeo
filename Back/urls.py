from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from . import views 
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView
from django.contrib.auth import views as auth_views

urlpatterns=[
    url(r'^$',views.index),
    url(r'^index/$',views.index,name="inicio"),
    url(r'^Ingresar/$',views.ingresar,name="login"),
    url(r'^salir/$',views.salir,name="logout"),
    url(r'^Usuarios/$',views.gestionarUsuarios,name="gestionarUsuarios"),
    url(r'^Mascota/$',views.gestionarMascota,name="gestionarMascotas"),
    url(r'^MascotaLista',views.lista,name="lista"),
    url(r'^Registro',views.registro,name="registrarse"),

    url(r'^oauth/', include('social_django.urls', namespace='social')),

    
    #url(r'^Mascota/$',views.MascotaCreate.as_view(),name="MascotaNueva"),
    #url(r'^Editar/(?P<pk>\d+)/$',views.MascotaUpdate.as_view(),name="editarMascota"),
    #url(r'^Eliminar/(?P<pk>\d+)/$',views.MascotaDelete.as_view(),name="eliminarMascota"),
    #url(r'^Formulario/$',views.Formulario,name="Fomulario"),   
    #url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),

    #RECUPERAR CONTRASEÑA 

    url(r'^password_reset', PasswordResetView.as_view(), 
        {'template_name':'password_reset_form.html',
        'email_template_name': 'password_reset_email.html'}, 
        name='password_reset'), 
    url(r'^password_reset_done', PasswordResetDoneView.as_view(), 
        {'template_name': 'password_reset_done.html'}, 
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', PasswordResetConfirmView.as_view(), 
        {'template_name': 'password_reset_confirm.html'},
        name='password_reset_confirm'
        ),
    url(r'^reset/done', PasswordResetCompleteView.as_view(), {'template_name': 'password_reset_complete.html'},
        name='password_reset_complete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   

