from django.db import models
from django.contrib.auth.models import User

class Barang(models.Model):
    tanggal = models.DateField() # tanggal angsuran
    nama = models.CharField(max_length=5)
    harga = models.DecimalField(max_digits=12, decimal_places=2)
    cu = models.ForeignKey(User,related_name='+', on_delete=models.CASCADE,editable=False, null=True, blank=True)
    cdate = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'barang'
        verbose_name = 'Barang'
        verbose_name_plural = verbose_name
        get_latest_by = 'tanggal'

    def __str__(self):
        return '%s' % (self.id)
