from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from . import views

# 创建路由器并注册 ViewSet
router = DefaultRouter()
router.register('Post', views.BlogImages)

# 定义 URL 路径
urlpatterns = [
    # 基本页面的 URL
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('js_test/', views.js_test, name='js_test'),
    
    # REST API 路径
    path('api_root/', include(router.urls)),  # 注册的 ViewSet 路径
    path('api_root/api-token-auth/', obtain_auth_token),  # Token 认证路径
    path('api-auth/', include('rest_framework.urls')),  # REST Framework 自带的登录/登出
]
