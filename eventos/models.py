from django.db import models

class Evento(models.Model):
    nome = models.CharField(max_length=255) 
    descricao = models.CharField(max_length=500,null = True,blank = True) 
    data_inicio = models.DateField()
    data_fim = models.DateField()
    local = models.CharField(max_length=255) 

    def __str__(self):
        return self.nome 
    
class Participante(models.Model):
    nome = models.CharField(max_length=255) 
    email = models.CharField(max_length=255) 
    celular = models.CharField(max_length=12)
    tipo = models.CharField(max_length=20)
    evento = models.ManyToManyField(Evento)

    def __str__(self):
        return self.nome  
    
    
class Atividade(models.Model):
    titulo = models.CharField(max_length=255) 
    descricao = models.CharField(max_length=500,null = True,blank = True) 
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    eventos = models.ForeignKey(Evento,on_delete=models.CASCADE)
    responsavel = models.ForeignKey(Participante,on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo    
    

    