from django.db import models

class Category(models.Model):
	category_text = models.CharField(max_length = 20)
	def __str__(self):
		return self.category_text

class Question(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    question_text = models.CharField(max_length=200)
    def __str__(self):
    	return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    answer = models.BooleanField(default=False)
    def __str__(self):
    	return self.choice_text