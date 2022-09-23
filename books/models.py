# # from tkinter import Scale
from django.db import models
# from django.utils.translation import grttrxt_lazy as _

# # --------1st Video---------------
# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.TextField()

    def __str__(self):
        return self.title
# # ------------end----------------------

# class Category(models.model):
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name

# class Quizzes(models.model):
#     title = models.CharField(max_length=255, default=_("New Quiz"))
#     catagory = models.ForeignKey(Category,default=1,on_dalete=models.DO_NOTHING)
#     date_created = models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return self.title

# class Question(models.model):
#     SCALE =(
#         (0,_('Fundamental')),
#         (1,_('Beginner')),
#         (2,_('Intermediate')),
#         (3,_('Advanced')),
#         (4,_('Expert')),
#     )
#     TYPE =(
#         (0,('Multiple Choice'))
#     )
#     Quiz = models.ForeignKey(Quizzes, related_name='question' , on_delete=models.DO_NOTHING)
#     technique = models.IntegerField(choices=Type, default=0,verbose_name=_("Type of Question"))
#     title = models.CharField(max_length=255, verbose_name=_("Title"))
#     difficulty = models.IntegerField(choices=SCALE,default=0,verbose_name=_("Difficulty"))
#     date_created = models.DateTimeField(auto_now_add=True ,verbose_name=_("Date Created"))
#     id_active = models.BooleanField(default=False ,verbose_name=_("Active Status"))
#     def __str__(self):
#         return self.title

# class Answer(models.model):
#     question = models.ForeignKey(Question, related_name='answer',on_delete=models.DO_NOTHING)
#     answer_text = models.CharField(max_length=255 ,verbose_name=_("Answer Text"))
#     is_right = models.BooleanField(default=False)
#     def __str__(self):
#         return self.answer_text
 
