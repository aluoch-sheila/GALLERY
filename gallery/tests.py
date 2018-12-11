
from django.test import TestCase
from .models import Posts,Location,Category
# Create your tests here.


class locationTest(TestCase):
    def setUp(self):
        self.new_location = Location(location="nairobi")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_location,Location))

    def test_data(self):
        self.assertTrue(self.new_location.location,"nairobi")

    def test_save(self):
        self.new_location.save()
        location = Location.objects.all()
        self.assertTrue(len(location)>0)
    
    def test_delete(self):
        location = Location.objects.filter(id=1)
        location.delete()
        locale = Location.objects.all()
        self.assertTrue(len(locale)==0)

    def test_update_location(self):
        self.new_location.save()
        self.update_location = Location.objects.filter(location='nairobi').update(location = 'Kenya')
        self.updated_location = Location.objects.get(location='Kenya')
        self.assertTrue(self.updated_location.location, 'Kenya')

    def test_get_location_by_id(self):
        self.new_location.save()
        locale = Location.objects.get(id=1)
        self.assertTrue(locale.location,'nairobi')


class CategoryTest(TestCase):
    def setUp(self):
        self.new_category = Category(name="test")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_category,Category))

    def test_data(self):
        self.assertTrue(self.new_category.name,"test")
        
    def test_save(self):
        self.new_category.save()
        categories = Category.objects.all()
        self.assertTrue(len(categories)>0)
    
    def test_delete(self):
        category = Category.objects.filter(id=1)
        category.delete()
        cat = Category.objects.all()
        self.assertTrue(len(cat)==0)
    
    def test_update_category(self):
        self.new_category.save()
        self.update_cat = Category.objects.filter(name='test').update(name = 'wedding')
        self.updated_cat = Category.objects.get(name='wedding')
        self.assertTrue(self.updated_cat.name,'wedding')

    def test_get_category_by_id(self):
        self.new_category.save()
        cat = Category.objects.get(id=1)
        self.assertTrue(cat.name,'test')


class postsTest(TestCase):
    def setUp(self):
        self.new_location = Location(location="nairobi")
        # self.new_category = Category(name="test")
        self.new_location.save()
        # self.new_category.save()
        self.new_post = Posts(name="sheila",description="like eating",location=self.new_location)
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_post,Posts))
    
    def test_data(self):
        self.assertTrue(self.new_post.name,"sheila")
        self.assertTrue(self.new_post.description,"like eating")
    
    def test_save(self):
        self.new_post.save()
        posts = Posts.objects.all()
        self.assertTrue(len(posts)>0)
    
    def test_delete(self):
        post = Posts.objects.filter(id=1)
        post.delete()
        posts = Posts.objects.all()
        self.assertTrue(len(posts)==0)

    def test_update_post(self):
        self.new_post.save()
        self.update_post = Posts.objects.filter(name='sheila').update(name = 'cake')
        self.updated_post = Posts.objects.get(name='cake')
        self.assertTrue(self.updated_post.name,'cake')


    
    def test_get_post_by_id(self):
        self.new_post.save()
        posts = Posts.objects.get(id=1)
        self.assertTrue(posts.name,'sheila')
