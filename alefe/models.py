from django.db import models

# HOME SECTION

class Inicio(models.Model):
    nome = models.CharField(max_length=50)
    saudacao = models.CharField(max_length=20)
    foto = models.ImageField(upload_to='Perfil/')
    # save time when modified
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome


# ABOUT SECTION

class Sobre(models.Model):
    cabecalho = models.CharField(max_length=50)
    carreira = models.CharField(max_length=50)
    descricao = models.TextField(blank=False)
    perfil_img = models.ImageField(upload_to='Perfil/')
    
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.carreira


class Perfil(models.Model):
    sobre = models.ForeignKey(Sobre,
                                on_delete=models.CASCADE)
    rede_social = models.CharField(max_length=20)
    link = models.URLField(max_length=200)



# SKILLS SECTION

class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Habilidade'
        verbose_name_plural = 'Habilidades'

    def __str__(self):
        return self.nome

class Habilidades(models.Model):
    categoria = models.ForeignKey(Categoria,
                                on_delete=models.CASCADE)
    habilidade_nome = models.CharField(max_length=50)

    

# PORTFOLIO SECTION

class Projeto(models.Model):
    nome_projeto = models.CharField(max_length=50,default='')
    imagem = models.ImageField(upload_to='projetos/')
    link = models.URLField(max_length=200)

    def __str__(self):
        return f'{self.id}'


