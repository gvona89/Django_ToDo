from django.urls import include, path                    
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# similiar to express's app.use('/todoitem/', someRouter)
router.register(r'todoitem', views.TodoItemViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]
