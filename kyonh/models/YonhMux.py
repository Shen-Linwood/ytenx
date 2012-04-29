# coding=utf-8
from django.db import models
from SieuxYonh import SieuxYonh

#韻母
class YonhMux(models.Model):
  #韻母名稱
  mjeng = models.CharField(max_length=3, unique=True)
  #所屬韻系
  gheh = models.ForeignKey('YonhGheh', db_index=True)
  #等
  tongx = models.SmallIntegerField(db_index=True)
  #開合口呼
  ho = models.BooleanField(db_index=True)
  #促舒
  tshyuk = models.BooleanField(db_index=True)
  #同位對立入聲/舒聲
  tuaih = models.ForeignKey('YonhMux')
  #擬音
  ngix = models.ForeignKey('NgixQim')
  #拼音
  preng = models.ForeignKey('PrengQim')
  
  class Meta:
    app_label = 'kyonh'
  
  def __unicode__(self):
      return self.mjeng

  #小韻
  def sieuxYonh(self):
      return SieuxYonh.objects.filter(yonh=self)
