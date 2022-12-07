from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw


# Create your models here.

class Visitas(models.Model):
    nome_morador = models.CharField(max_length=50)
    nome_visita = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=14)
    desc_visita = models.CharField(max_length=100)
    bloco = models.IntegerField(default=0)
    Num_apartamento = models.IntegerField(default=0)
    
    qr_code = models.ImageField(upload_to="qr_codes", blank=True)

    def __str__(self):
        return str(self.nome_visita)

    def save(self,*args,**kwargs):
        informacoes = f'Nome do Morador: {self.nome_morador}\nNome da visita: {self.nome_visita}\nCPF: {self.cpf}\nTelefone: {self.telefone}\nDescrição: {self.desc_visita}\nbloco: {self.bloco}\nNumero do apartamento: {self.Num_apartamento}'
        qrcode_image = qrcode.make(informacoes)
        qrcode_image = qrcode.make(informacoes)
        canvas = Image.new("RGB",(600,600), "white")
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_image)
        fname = f"qr_code-{self.nome_morador,}"+".png"
        buffer = BytesIO()
        canvas.save(buffer,"PNG")
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)


class Servicos(models.Model):
    nome_morador = models.CharField(max_length=50)
    nome_servico = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=14)
    telefone = models.CharField(max_length=14)
    desc_servico = models.CharField(max_length=100)
    bloco = models.IntegerField(default=0)
    Num_apartamento = models.IntegerField(default=0)
    
    qr_code = models.ImageField(upload_to="qr_codes", blank=True)

    def __str__(self):
        return str(self.nome_servico)

    def save(self,*args,**kwargs):
        informacoes = f'Nome do Morador: {self.nome_morador}\nNome da visita: {self.nome_visita}\nCNPJ: {self.cpf}\nTelefone: {self.telefone}\nDescrição: {self.desc_visita}\nbloco: {self.bloco}\nNumero do apartamento: {self.Num_apartamento}'
        qrcode_image = qrcode.make(informacoes)
        canvas = Image.new("RGB",(600,600), "white")
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_image)
        fname = f"qr_code-{self.nome_morador,}"+".png"
        buffer = BytesIO()
        canvas.save(buffer,"PNG")
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)
