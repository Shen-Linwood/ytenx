# coding=utf-8
from django.db import models
from SieuxYonh import SieuxYonh

#聲類
class CjengLyih(models.Model):
  #脣音 舌頭音 舌上音 齒頭音 正齒音莊組 正齒音章組 牙音 喉音 半舌音 半齒音
  mjeng = models.CharField(max_length = 5, unique = True)
  
  class Meta:
    app_label = 'kyonh'

  def __unicode__(self):
      return self.mjeng

#聲母
class CjengMux(models.Model):
  #代表字
  dzih = models.CharField(max_length = 1, unique = True)
  #聲類
  lyih = models.ForeignKey(CjengLyih)
  #擬音
  ngix = models.ForeignKey('NgixQim')
  #拼音
  preng = models.ForeignKey('PrengQim')
  
  class Meta:
    app_label = 'kyonh'

  def __unicode__(self):
      return self.dzih
  
  #小韻
  def sieuxYonh(self):
      return SieuxYonh.objects.filter(cjeng=self)
