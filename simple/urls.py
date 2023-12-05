from django.contrib import admin
from django.urls import path, re_path, include
from fobi.contrib.apps.drf_integration.urls import fobi_router
from core.views import CareerPageView, index, JobzoneView, CareerView


urlpatterns = [
    path('', index, name='index'),
    path("admin/", admin.site.urls),
    # View URLs
    re_path(r'^fobi/', include('fobi.urls.class_based.view')),

    # Edit URLs
    re_path(r'^fobi/', include('fobi.urls.class_based.edit')),
    # DB Store plugin URLs
    re_path(r'^fobi/plugins/form-handlers/db-store/',
            include('fobi.contrib.plugins.form_handlers.db_store.urls')),

    re_path(r'^fobi/plugins/form-wizard-handlers/db-store/',
            include('fobi.contrib.plugins.form_handlers.db_store.urls.'
                    'form_wizard_handlers')),
    re_path(r'^api/', include(fobi_router.urls)),
    path('career/', CareerPageView.as_view(), name='career'),
    path('api/jobzone/', JobzoneView.as_view(), name='jobzone'),
    path('api/career/', CareerView.as_view(), name='career2'),

]
