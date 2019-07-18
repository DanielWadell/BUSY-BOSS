from django_elasticsearch_dsl import DocType, Index
from busyapp.models import Post

posts = Index('posts')

@posts.doc_type
class PostDocument(DocType):
    class Meta:
        model = Post

        fields = [
            'title',
            'image',
            'text',
            'slug',
            'create_date',
            'published_date',
        ]