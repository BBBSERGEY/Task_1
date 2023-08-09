from django.db import models
from django.contrib.auth import get_user_model



User = get_user_model()

class OnlineShop(models.Model):
    id = models.CharField("id", max_length=64, primary_key=True)
    title = models.CharField('Заголовок', max_length=50)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2) 
    auction = models.BooleanField('Торг', help_text='Отметьте, уместен ли торг')
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE)
    image = models.ImageField('Изображение', upload_to='online_shop/')

    def __str__(self): 
        return f'<Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price})>'

    class Meta:
        db_table = 'advertisement'













