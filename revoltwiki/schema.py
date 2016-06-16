import graphene
from wiki.schema import Query as WikiQuery


class Query(WikiQuery):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

schema = graphene.Schema(name='Wiki Schema')
schema.query = Query
