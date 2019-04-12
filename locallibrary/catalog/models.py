from django.db import models
from django.core.files.base import ContentFile

# Create your models here.

class Section(models.Model):
    name = models.CharField(max_length = 50,  help_text = "Section", blank = True, null = True, default = "Null")
    def __str__(self):
        return "{}".format(self.name)

class Project(models.Model):
    name = models.CharField(max_length = 300, help_text = "Project Name")
    description = models.TextField(max_length = 100000, help_text = "Write Project description")
    start_date = models.DateField(help_text = "Enter the project start date", null = True)
    end_date = models.DateField(help_text = "Enter the project end date (leave blank if no end date)", null = True, blank =True)
    published_choices = (
        ("Yes", "Yes"),
        ("No", "No")
    )
    published = models.CharField(max_length = 3, choices = published_choices, default = 'No')
    section = models.ForeignKey("Section",on_delete=models.SET_NULL, null=True, blank = True, verbose_name= "Section of Newspaper Published")
    peoples = models.ManyToManyField('People', through = 'People_Project', verbose_name = "contributors", help_text = "Select all individuals who contributed to the project. (Hold down 'Control', or 'Command' on a Mac, to select more than one)",  blank = True, default= "None" )

    BACKEND_PROGRESS = (
        ('None', 'None'),
        ('Data Collection', 'Data Collection'),
        ('Data Cleaning', 'Data Cleaning'),
        ('Data Analysis', 'Data Analysis'),
        ('Insight Report', 'Insight Report'),
      )
    backend_progress = models.CharField(max_length = 100, choices = BACKEND_PROGRESS , default = 'None' ,
        help_text = "Backend Progress Stages: (1) Data Collection, (2) Data Cleaning, (3) Data Analysis, (4) Insight Report. Please select the stage of the project last completed. If none of the stages are completed please select None.")

    class Meta:
        ordering = ['start_date', 'end_date']
    def __str__(self):
        return "{}".format(self.name)

class Major(models.Model):
    name = models.CharField(max_length = 100, help_text = "Major Name")
    peoples = models.ManyToManyField('People', through = 'People_Major', blank = True, default= "None")
    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name

class Minor(models.Model):
    name = models.CharField(max_length = 100, help_text = "Minor Name")
    peoples = models.ManyToManyField('People', through = 'People_Minor', blank = True, default= "None")

    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name

class People(models.Model):
    first_name = models.CharField(max_length = 20, help_text = "Enter your first name")
    last_name = models.CharField(max_length = 20, help_text = "Enter your last name")
    start_date = models.DateField(help_text = "Enter the date you started working for the Data Engineering team")
    end_date = models.DateField(null = True, blank = True, help_text = "Enter the date you stopped working for the Data Engineering team (do not enter anything if you still work for the team)")
    email = models.EmailField(help_text = "Enter your Umich email")
    umich_id = models.IntegerField(help_text = "Enter your umichid")
    phone_number = models.IntegerField(help_text = "Enter your Phone Number")

    # picture ="{}_{}".format(self.first_name, self.last_name)
    # name_of_picture = (
    #     (picture, picture),
    #     )
    # picture =  models.CharField(max_length = 2, choices = name_of_picture, default = 'samantha_cohen.jpg' )
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    YEAR_IN_SCHOOL_CHOICES = (
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
      )
    year_in_school = models.CharField(max_length =2, choices = YEAR_IN_SCHOOL_CHOICES, default = 'FR')
    member = "MEM"
    senior_editor = "SRE"
    ROLE_CHOICES = (
        (member, 'Member'),


        (senior_editor, 'Senior Editor'),
    )
    role = models.CharField(max_length=3, choices = ROLE_CHOICES, default= member)
    date_of_birth = models.DateField(null = True, help_text= "Enter Your Birthday")
    picture = models.ImageField(upload_to = 'pictures/',max_length = 400, default = 'pictures/no-photo.jpg')
    projects = models.ManyToManyField('Project', through = 'People_Project', help_text = "Select all Projects you have worked on.(Hold down 'Control', or 'Command' on a Mac, to select more than one)", blank = True,verbose_name='Project(s)' )
    majors = models.ManyToManyField('Major', through = 'People_Major', help_text = "Select your major(s).(Hold down 'Control', or 'Command' on a Mac, to select more than one)", blank = True,verbose_name='Major(s)', default = "Undeclared")
    minors = models.ManyToManyField('Minor', through = 'People_Minor', help_text = "Select your minor(s).(Hold down 'Control', or 'Command' on a Mac, to select more than one)", blank = True, verbose_name='Minor(s)')

    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = "People"

    def is_upperclass(self):
        return self.year_in_school in (self.JUNIOR, self.SENIOR)

    def picture_name(self):
         file_name = "{}_{}.jpg".format(self.first_name, self.last_name)
         return file_name

    def __str__(self):
        return "{},{}".format(self.last_name, self.first_name)

class People_Project(models.Model):
    people = models.ForeignKey('People', on_delete= models.CASCADE)
    project = models.ForeignKey('Project', on_delete= models.CASCADE)

    class Meta:
        auto_created = True

    def __str__(self):
        return "Person "+ str(self.people) + "<--> Project "+ str(self.project)


class People_Major(models.Model):
    people = models.ForeignKey('People', on_delete= models.CASCADE)
    major = models.ForeignKey('Major', on_delete= models.CASCADE)
    class Meta:
        auto_created = True
    def __str__(self):
        return "Person "+ str(self.people) + "<--> Major "+ str(self.major)

class People_Minor(models.Model):
    people = models.ForeignKey('People', on_delete= models.CASCADE)
    minor = models.ForeignKey('Minor', on_delete= models.CASCADE)
    class Meta:
        auto_created = True
    def __str__(self):
        return "Person "+ str(self.people) + "<--> Minor "+ str(self.minor)



# class Published(models.Model):
#     published_id = models.AutoField(primary_key = True)
#     project_id = models.ForeignKey("Project",on_delete=models.SET_NULL, null=True)
#     person_id = models.ForeignKey("People",on_delete=models.SET_NULL, null=True)
#     published_choices = (
#         ("Yes", "Yes"),
#         ("No", "No")
#     )
#     published = models.CharField(max_length =2, choices = published_choices, default = 'No')
#     def __str__(self):
#         return "{}".format(self.published)
