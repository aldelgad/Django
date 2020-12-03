from django.db import models

# Create your models here.

class Factura(models.Model):
	num = models.AutoField(primary_key=True)
	year = models.IntegerField()
	emission_date = models.DateField(auto_now_add=True)
	customer_name = models.TextField()
	customer_address = models.TextField()

	def __str__(self):
		return f'{self.customer_name} - {self.emission_date}: {self.num}'

class Linea_de_Factura(models.Model):
	id_line = models.AutoField(primary_key=True)
	product_name = models.TextField()
	facture_line = models.ForeignKey(
		Factura,
		on_delete=models.PROTECT,
		default='DEF',
		related_name='linea'
		)
	unit_prize = models.FloatField()
	unit_total = models.IntegerField()

	def __str__(self):
		return f'{self.facture_line}: {self.product_name} - {self.unit_prize}'

	def prize(self):
		prize = float(self.unit_prize) * float(self.unit_total)
		return prize

