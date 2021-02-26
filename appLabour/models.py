from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
gender=(
         ("male","Male"),
         ("female","Female"),
         ("transgender","Transgender")
         )

age=(
		tuple([x,x])for x in range(1,120)
	  )

country= (
           
           ("india","India"),
           ("america","America"),
           ("unitedKingdom","UnitedKingdom"),
           ("france","France"),
           ("russia","Russia"),
           ("italy","Italy"),
           ("china","China"),
           ("nepal","Nepal"),
           ("brazil","Brazil"),
           ("germany","Germany"),
           ("argentina","Argentina"),
           ("poland","Poland"),
           ("wales","Wales"),
           ("norway","Norway"),
           ("srilanka","Srilanka"),
           ("uae","UAE"),
           ("australia","Australia"),
           ("japan","Japan"),
           ("newsland","Newsland"),
           ("southAfrica","SouthAfrica")

	      )

district=(
  
       ("thiruvandapuram","Thiruvandapuram"),
       ("ernakulam","Ernakulam"),
       ("pathanamthitta","Pathanamthitta"),
       ("palakkad","Palakkad"),
       ("thrissur","Thrissur"),
       ("idduki",'Idduki'),
       ("malppuram","Malppuram"),
       ("kozhikode","Kozhikode"),
       ("wayanad","Wayanad"),
       ("kannur","Kannur"),
       ("kasaragod","Kasaragod")
	    )
edu=(
      

      ("SSLC","SSLC"),
      ("PLUSTWO","PLUSTWO"),
      ("DEGREE","DEGREE"),
      ("BETCH","BETCH"),
      ("OTHERS","OTHERS")
      )

lang=(
    
    ("ENGLISH","ENGLISH"),
    ("HINDI","HINDI"),
    ("MALAYALAM","MALAYALAM")
     )




class Sample(models.Model):
  Phone_regex=RegexValidator(regex=r'^\+?1?\d{9,15}$',message="PhoneNumber must be entered in the format:'+999999999'. up to 15 digits allowed.")
  Firstname=models.CharField(max_length=100)
  Lastname=models.CharField(max_length=100)
  Gender=models.CharField(max_length=100,choices=gender)
  Age=models.IntegerField()
  EducationalQualification=models.CharField(max_length=100,default='')
  LanguageKnown=models.CharField(max_length=100,default='')
  Address=models.CharField(max_length=100)
  Email=models.EmailField()
  Photo=models.ImageField(upload_to="media/",default=0)
  Village=models.CharField(max_length=100)
  District=models.CharField(max_length=100,choices=district)
  Country=models.CharField(max_length=100,choices=country)
  PhoneNumber=models.CharField(validators=[Phone_regex],max_length=17,blank=True)
  Password=models.CharField(max_length=8)
  ConfirmPassword=models.CharField(max_length=8)
  Status=models.BooleanField(default=False)

  
  def __str__(self):
        return self.Firstname

class Images(models.Model):
  Name=models.CharField(max_length=100)
  Color=models.CharField(max_length=100)
  Price=models.IntegerField(default=0)
  Image=models.ImageField(upload_to="media/",default=0)
  Model=models.CharField(max_length=100,default=0)

  def __str__(self):
        return self.Name



