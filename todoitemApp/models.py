from django.db import models

# below is like the following in express:
#
#   TodoItemSchema = mongoose.Schema({ description : String, done : Boolean })
#
# (like "class TodoItem extends ..." in Js)
#         python class inheritance
#              |
#              V
class TodoItem(models.Model):
    # add the different fields of our model
    # see https://docs.djangoproject.com/en/2.2/ref/models/fields/ for the 
    # different kinds of fields you can use
    description = models.CharField(max_length=30)
    done        = models.BooleanField()
