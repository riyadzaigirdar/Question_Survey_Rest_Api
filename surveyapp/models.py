from django.db import models
from django.conf import settings
print('ok 1 2')
answer_choices = (
    ('Yes', 'Yes'),
    ('No', 'No'),
)

class Question(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank= True, null = True)
    title = models.CharField(max_length = 500)
    response = models.ManyToManyField('Answer', blank=True )

    def __str__(self):
        return self.title

class Answer(models.Model):
    ques = models.ForeignKey('Question', on_delete=models.CASCADE, blank= True, null = True )
    candidiate = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank= True, null = True)
    ans = models.CharField(choices=answer_choices, max_length=3)

    def __str__(self):
        return f'{self.ans} from {self.candidiate} in {self.ques}'