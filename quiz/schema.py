from ast import Delete
from dataclasses import field
from pyexpat import model
# from unicodedata import category
import graphene
from graphene_django import DjangoObjectType
from graphene_django import DjangoListField
from .models import Quizzes , Category , Question ,Answer

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id","name")

class QuizzesType(DjangoObjectType):
     class Meta:
        model = Quizzes
        fields = ("id","title","catrgory","quiz")

class QuestionType(DjangoObjectType):
     class Meta:
        model = Question
        fields = ("title","quiz")

class AnswerType(DjangoObjectType):
     class Meta:
        model = Answer
        fields = ("question","answer_text")

class Query(graphene.ObjectType):
        all_category = DjangoListField(CategoryType)
        category_byid = graphene.Field(CategoryType, id=graphene.Int())
        category_byname = graphene.Field(CategoryType, name=graphene.String())
        def resolve_all_category(root,info):
                return Category.objects.all()   
        def resolve_category_byid(root,info,id):
                return Category.objects.get(id=id)  
        def resolve_category_byname(root,info,name):
                return Category.objects.get(name=name)  

        # -----------all()----------------
        # all_question = DjangoListField(QuestionType)
        # def resolve_all_question(root,info):
        #         return Question.objects.all()

        #--------------Fiter()-------------
        # all_question = DjangoListField(QuestionType)
        # def resolve_all_question(root,info):
        #         return Question.objects.filter(id=2)

        #--------------Sting Or Message-------
        # quiz = graphene.String()
        # def resolve_quiz(root,info):
        #         return f"This is the first question"

        #-------------with Parameter (id from Frontend)-----
        # all_quizzes = graphene.Field(QuizzesType, id=graphene.Int())
        # def resolve_all_quizzes(root, info, id):
        #         return Quizzes.objects.get(pk=id)
        #------------multipul models data gets-------------
        # all_quizzes = DjangoListField(QuizzesType)
        # all_Category = DjangoListField(CategoryType)
        # all_question = DjangoListField(QuestionType)
        # def resolve_all_question(root,info):
        #         return Question.objects.all()
        #  # def resolve_all_Category(root,info):
        #         return Category.objects.all()

              #--------------One to Many----------------
        # all_question = graphene.Field(QuestionType, id=graphene.Int())
        # all_answers = graphene.List(AnswerType, id=graphene.Int())
        # def resolve_all_question(root, info, id):
        #         return Question.objects.get(pk=id)

        # def resolve_all_answers(root, info, id):
        #         return Answer.objects.filter(question=id)                              #all Ans
        #         return Answer.objects.filter(question=id,is_right=True)                #correct Ans

#---------create new by Mutation-----------------
class CreateCategoryMutation(graphene.Mutation):
        class Arguments:
                name = graphene.String(required=True)
                
        category = graphene.Field(CategoryType)
        @classmethod
        def mutate(cls ,root ,info, name):
                category =Category(name=name)
                category.save()
                return CreateCategoryMutation(category = category)
## class Mutation(graphene.ObjectType):
#         update_categiry = CategoryMutation.Field()

#----------update data by Mutation----------------
class UpdateCategoryMutation(graphene.Mutation):
        class Arguments:
                id = graphene.ID()
                name = graphene.String(required=True)
        category = graphene.Field(CategoryType)
        @classmethod
        def mutate(cls, root, info, name, id):
                category = Category.objects.get(id=id)
                category.name = name
                category.save()
                return UpdateCategoryMutation(category = category)
# class Mutation(graphene.ObjectType):
#         update_categiry = CategoryMutation.Field()
#--------Delete data by Mutation-------------------
class DeleteCategoryMutation(graphene.Mutation):
        class Arguments:
                id = graphene.ID()
                # name = graphene.String(required=True)
        category = graphene.Field(CategoryType)
        @classmethod
        def mutate(cls, root, info, id):
                category = Category.objects.get(id=id)
                category.delete()
                return DeleteCategoryMutation(category = category)

class Mutation(graphene.ObjectType):
        update_category = UpdateCategoryMutation.Field()
        Create_category = CreateCategoryMutation.Field()
        Delete_category = DeleteCategoryMutation.Field()

schema =graphene.Schema(query =Query, mutation=Mutation)
