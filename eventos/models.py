from django.db import models

class Participante(models.Model):
    nome = models.CharField(max_length=255) 
    email = models.EmailField(max_length=255) 
    celular = models.CharField(max_length=12)
    tipo = models.CharField(max_length=20, choices= [('palestrante', 'Palestrante'),
                                                     ('estudante', 'Estudante'),
                                                     ('convidado', 'Convidado'),])
    
    def __str__(self):
        return self.nome  


class Evento(models.Model):
    nome = models.CharField(max_length=255) 
    descricao = models.CharField(max_length=500,null = True,blank = True) 
    data_inicio = models.DateField()
    data_fim = models.DateField()
    local = models.CharField(max_length=255) 
    participantes = models.ManyToManyField(Participante, blank=True)
    def __str__(self):
        return self.nome 
    

    
class Atividade(models.Model):
    titulo = models.CharField(max_length=255) 
    descricao = models.CharField(max_length=500,null = True,blank = True) 
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    evento = models.ForeignKey(Evento,on_delete=models.CASCADE, related_name='atividades')
    responsavel = models.ForeignKey(Participante,on_delete=models.CASCADE, related_name='responsavel')
    tipo = models.CharField(max_length=255, choices= [('workshop', 'Workshop'),
                                                      ('palestra', 'Palestra'),
                                                      ('mesa redonda', 'Mesa Redonda'),
                                                      ('oficina', 'Oficina'),])

    def __str__(self):
        return self.titulo    
    

    