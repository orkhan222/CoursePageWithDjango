from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db.models.fields import TextField
from django.db.models.fields.related import ForeignKey
User = get_user_model()


#------------------------------- Homenu Slider ----------------------------------------------
class Slider(models.Model):
    title= models.CharField('Title', max_length=127,null=True)
    yazili = models.CharField('Yazili',max_length=127,null=True)
    image = models.ImageField('Shekili', upload_to='slider_image')
    


    class Meta:
        verbose_name='Slider'
        verbose_name_plural='Sliders'
        # ordering=('-created_at',)


    def __str__(self):
        return self.title


#------------------------------- Homenu About ----------------------------------------------
class About(models.Model):
    title= models.CharField('Title', max_length=127,null=True)
    yazili = models.CharField('Yazili',max_length=127,null=True)
    text= models.CharField('Text',max_length=127,null=True)
    


    class Meta:
        verbose_name='About'
        verbose_name_plural='Abouts'
        # ordering=('-created_at',)


    def __str__(self):
        return self.title

#------------------------------- Homenu Apply ----------------------------------------------
class Apply(models.Model):
    title= models.CharField('Title', max_length=127,null=True)
    time = models.CharField('Time',max_length=127,null=True)
    campus= models.CharField('Campus',max_length=127,null=True)
    hafttime= models.CharField('Hafttime',max_length=127,null=True)
    rc= models.CharField('Rc',max_length=127,null=True)
    


    class Meta:
        verbose_name='Apply'
        verbose_name_plural='Applys'
        # ordering=('-created_at',)


    def __str__(self):
        return self.title


#------------------------------- Homenu Apply ----------------------------------------------
class Fall(models.Model):
    title= models.CharField('Title', max_length=127,null=True)
    text = models.CharField('Text',max_length=127,null=True)



    class Meta:
        verbose_name='Fall'
        verbose_name_plural='Falls'
        # ordering=('-created_at',)


    def __str__(self):
        return self.title


#------------------------------- Homenu Slider ----------------------------------------------
class Featured(models.Model):
    title= models.CharField('Title', max_length=127,null=True)
    span = models.CharField('Span',max_length=127,null=True)
    name = models.CharField('Name',max_length=127,null=True)
    
    image = models.ImageField('Shekili', upload_to='featured_image')
    


    class Meta:
        verbose_name='Featured'
        verbose_name_plural='Featureds'
        # ordering=('-created_at',)


    def __str__(self):
        return self.title


#------------------------------- Homenu Slider ----------------------------------------------
class Teacher(models.Model):
    title= models.CharField('Title', max_length=127,null=True)
    title2 = models.CharField('Title2',max_length=127,null=True)
    text = models.CharField('Text',max_length=127,null=True)
    
    
    


    class Meta:
        verbose_name='Teacher'
        verbose_name_plural='Teachers'
        # ordering=('-created_at',)


    def __str__(self):
        return self.title



#------------------------------- Homenu Slider ----------------------------------------------

class Image(models.Model):
    name= models.CharField('Name', max_length=127,null=True)
    span = models.CharField('Span',max_length=127,null=True)
    image = models.ImageField('Shekili', upload_to='image_image')
    
    
    


    class Meta:
        verbose_name='Image'
        verbose_name_plural='Images'
        # ordering=('-created_at',)


    def __str__(self):
        return self.name




#------------------------------- Homenu Slider ----------------------------------------------
class Store(models.Model):
    title= models.CharField('Title', max_length=127,null=True)
    span = models.CharField('Span',max_length=127,null=True)
    name = models.CharField('Name',max_length=127,null=True)
    span2 = models.CharField('Span2',max_length=127,null=True)
    image = models.ImageField('Shekili', upload_to='Store_image')
    
    


    class Meta:
        verbose_name='Store'
        verbose_name_plural='Stores'
        # ordering=('-created_at',)


    def __str__(self):
        return self.title



#------------------------------- Courses Our ----------------------------------------------
class Our(models.Model):
    title= models.CharField('Title', max_length=127,null=True)
    span = models.CharField('Span',max_length=127,null=True)
    name = models.CharField('Name',max_length=127,null=True)
    image = models.ImageField('Shekili', upload_to='our_image')
    


    class Meta:
        verbose_name='Our'
        verbose_name_plural='Ours'
        # ordering=('-created_at',)


    def __str__(self):
        return self.title

#------------------------------- Courses Our ----------------------------------------------
class Basic(models.Model):
    title= models.CharField('Title', max_length=127,null=True)
    span = models.CharField('Span',max_length=127,null=True)
    name = models.CharField('Name',max_length=127,null=True)
    programming = models.CharField('Prohramming',max_length=127,null=True)
    image = models.ImageField('Shekili', upload_to='basic_image')
    


    class Meta:
        verbose_name='Basic'
        verbose_name_plural='Basics'
        # ordering=('-created_at',)


    def __str__(self):
        return self.title


class Make(models.Model):
    title= models.CharField('Title', max_length=127,null=True)
    image = models.ImageField('Shekili', upload_to='basic_image')
    


    class Meta:
        verbose_name='Make'
        verbose_name_plural='Makes'
        # ordering=('-created_at',)


    def __str__(self):
        return self.title




class Related(models.Model):
    title= models.CharField('Title', max_length=127,null=True)
    span = models.CharField('Span',max_length=127,null=True)
    name = models.CharField('Name',max_length=127,null=True)
    image = models.ImageField('Shekili', upload_to='related_image')
    


    class Meta:
        verbose_name='Related'
        verbose_name_plural='Relateds'
        # ordering=('-created_at',)


    def __str__(self):
        return self.title