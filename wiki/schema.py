from graphene import relay, ObjectType
from graphene.contrib.django.filter import DjangoFilterConnectionField
from graphene.contrib.django.types import DjangoNode
from .models import Article, Content, Category


class ArticleNode(DjangoNode):
    class Meta:
        model = Article
        filter_fields = {
            'id': ['exact'],
        }
        filter_order_by = ['-current_content__updated_at', 'title']


class ContentNode(DjangoNode):
    class Meta:
        model = Content
        filter_fields = {
            'id': ['exact'],
        }
        filter_order_by = ['parent_article__title']


class CategoryNode(DjangoNode):
    class Meta:
        model = Category
        filter_fields = {
            'id': ['exact'],
        }
        filter_order_by = ['title']


class Query(ObjectType):
    article = relay.NodeField(ArticleNode)
    all_articles = DjangoFilterConnectionField(ArticleNode)

    content = relay.NodeField(ContentNode)
    all_content = DjangoFilterConnectionField(ContentNode)

    category = relay.NodeField(CategoryNode)
    all_categories = DjangoFilterConnectionField(CategoryNode)

    class Meta:
        abstract = True
