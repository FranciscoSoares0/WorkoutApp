from django.db import models

# Create your models here.



class Exercise(models.Model):
    name=models.CharField(max_length=50)
    repetitions=models.IntegerField()
    sets=models.IntegerField()
    rest=models.IntegerField()
    weight = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.name} {self.sets}sets, {self.repetitions}reps, {self.rest}rest'
        
class Workout(models.Model):
    name=models.CharField(max_length=50)
    date=models.DateField()
    exercises=models.ManyToManyField(Exercise)

    def __str__(self):
        return f'{self.name} {self.date}'

class User(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    

    def __str__(self):
        return f'Nome:{self.name} Idade:{self.age}'

class Split(models.Model):
    name=models.CharField(max_length=50)
    inicial_date=models.DateField()
    final_date=models.DateField()
    user=models.ForeignKey(User,on_delete=models.CASCADE,
        related_name = 'users'
        )
    workouts=models.ManyToManyField(Workout)

    def __str__(self):
        return f'Split {self.pk} {self.name}'