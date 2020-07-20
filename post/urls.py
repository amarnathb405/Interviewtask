from django.urls import path,include
from rest_framework.routers import DefaultRouter
from post import views


router= DefaultRouter()

router.register(r'post', views.ArticleViewset)
router.register(r'review', views.ArticleReviewViewset)

urlpatterns = [
    path('',include(router.urls)),
    path('api/login', views.login)


]

