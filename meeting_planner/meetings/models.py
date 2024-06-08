from django.db import models
from datetime import time

# Create your models here.

class Room(models.Model):  # models.Model django'nun sınıfının kalıtımı  # model modülü djangonun ORM tooludur.
    name = models.CharField(max_length=50)  # CharField sınıfı name'in string objesi olmasını sağladı  # max_lenght= ifadesi max harf sayısını belirler
    floor = models.CharField(max_length=20)  # floor yani kat sayısını max 20 verdik
    room_number = models.IntegerField()  # oda sayısını integer olarak verdik
    capacity = models.IntegerField(default=1)  # oda kapasitesi



    def __str__(self):
        return (f'{self.name}: room'
                f'{self.room_number}: on floor'
                f'{self.floor}'
                f'{self.capacity}')


    class Meta:  # veri tabanının adı yani verilein tutulduğu yer Meta diye geçer yani tablomuz
        verbose_name_plural = 'rooms'



class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()  # date için DateField() sınıfını çağırıyoruz
    start_time = models.TimeField(default=time(9))  # mesai saat 9 da başladığı için 9 yazdık
    duration = models.IntegerField(default=1)  # toplantı süresi en az 1 saat sürecek
    room = models.ForeignKey(Room, on_delete=models.CASCADE)  # room sınıfının yabancıl anahtarıdır. # on_delete=models.CASCADE room bilgilerini silerken bilgileri silme demek


    def __str__(self):
        return (f'{self.title} at'
                f'{self.start_time} on'
                f'{self.date}'
                f'{self.duration}'
                f'{self.room}')


    class Meta:
        verbose_name_plural = 'meetings'  # verbose_name_plural dememizin sebebi ismi değiştirip yerine 'meetings' yazmasını istediğimiz için dedik