from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    
    def __str__ (self):
        return self.nome
    

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    data_publicacao = models.DateField()
    autor = models.ForeignKey(Autor, related_name='livros', on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo