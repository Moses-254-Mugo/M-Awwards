from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Project, Comments

# Create your tests here.
class CommentsTestCase(TestCase):
    def setUp(self):
        self.comment=Comments(text="Good", project_id=self.www.id, user = self.moringa)

    def test_instance(self):
        self.assertTrue(isinstance(self.comment.Comments))
    
    def test_save_comments(self):
        self.comment.sava_comment()
        coments = Comments.objects.all()
        self.assertEqual(len(coments),1)
    
    def test_delete_comment(self):
        self.comment.save_comments()
        self.comment.delete_comments()
        comment_list = Comments.objects.all()
        self.assertTrue(len(comment_list)==0)

class ProjectTestCase(TestCase):
    def setUp(self):
        self.newPost = Project(title = 'Pitchapp', image='pitch.jpg', description = 'good site', link ='http://pitchapp.com', user= 'moringa')


    def test_save_image(self):
        self.picture.savar_image()
        images = Project.objects.all()
        self.assertEqual(len(images),1)
    
    def test_delete_imge(self):
        self.images.sava_image()
        self.images.delete_image()
        image_list = Project.objects.all()
        self.assertTrue(len(image_list)==0)
