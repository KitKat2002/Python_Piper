from django.db import models

# Create your models here.
class DjangoClasses(models.Model):
    Title = models.CharField(max_length=60, blank = True, null = False),
    Course_Number = models.IntegerField(default = 0, blank = True, null = False),
    Instructor_Name = models.CharField(max_length=60, blank = True, null = False),
    Duration = models.FloatField(),

    objects = models.Manager()
    def __init__(self):
        pass

    def __str__(self):
            return self.Title

    def instructors(self):
        self.instructor1 = DjangoClasses("Johann", "Bach", 21, "Programming"),
        self.instructor2 = DjangoClasses("Christine", "Little", 30, "Programming"),
        self.instructor3 = DjangoClasses("Hanna", "Rochelle", 25, "History")

    def sources(self):
        self.firstcourse = DjangoClasses("American History", "Joe Terrif"),
        self.secondcourse = DjangoClasses("Learning JavaScript", "Katlin Venice"),
        self.thirdcourse = DjangoClasses("Project Python", "Kent Clark")

    def coursetimes(self):
        self.time1 = DjangoClasses("six weeks", "150 hours"),
        self.time2 = DjangoClasses("twelve weeks", "180 hours"),
        self.time3 = DjangoClasses("ten weeks", "200 hours")


