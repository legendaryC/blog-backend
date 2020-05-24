import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from blog.models import Block,Article


# Create a GraphQL type for the block model
class BlockType(DjangoObjectType):
    class Meta:
        model = Block

# Create a GraphQL type for the article model
class ArticleType(DjangoObjectType):
    class Meta:
        model = Article

# Create a Query type
class Query(ObjectType):
    
    article= graphene.Field(ArticleType, id=graphene.Int())
    block= graphene.Field(BlockType, id=graphene.Int())
    articles=graphene.List(ArticleType)
    blocks=graphene.List(BlockType)

    def resolve_article(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Article.objects.get(pk=id)
        return None

    def resolve_block(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Block.objects.get(pk=id)
        return None

    def resolve_articles(self, info, **kwargs):
        return Article.objects.all()
        
    def resolve_blocks(self, info, **kwargs):
        return Block.objects.all()

schema = graphene.Schema(query=Query, mutation=None)
