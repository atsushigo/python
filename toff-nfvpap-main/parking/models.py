from django.db import models

# Create your models here.
class County(models.Model):
    name = models.CharField('縣市', max_length=10)

    def __str__(self) -> str:
        return self.name

# class Area(models.Model):
#     name = models.CharField('區', max_length=10)
#     county = models.ForeignKey(County, on_delete=models.CASCADE)

class Port(models.Model):
    name = models.CharField('港口', max_length=10)
    county = models.ForeignKey(County, on_delete=models.CASCADE)
    # area = models.ForeignKey(Area, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

class VesselOwner(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=30, blank=True)
    id_no = models.CharField(verbose_name='身分證字號', max_length=30, blank=True)
    passport_no = models.CharField(verbose_name='護照號碼', max_length=30, blank=True)
    address = models.CharField(verbose_name='聯絡地址', max_length=50, blank=True)
    residential_no = models.CharField('市話', max_length=10, blank=True)
    mobile_no = models.CharField('行動電話', max_length=10, blank=True)
    fax_no = models.CharField('傳真', max_length=10, blank=True)
    email = models.EmailField(verbose_name='電子信箱',max_length=100,unique=True,)
    # vessel = models.ForeignKey(Vessel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Vessel(models.Model):
    name_cn = models.CharField('船名(中文)', max_length=100, blank=True)
    name_en = models.CharField('船名(英文)', max_length=100, blank=True)
    nationality = models.CharField('船舶國籍', max_length=100, blank=True)
    ctno = models.CharField('船編', max_length=10, blank=True)
    imo = models.CharField('IMO', max_length=10, blank=True)
    properties = models.CharField('易於辨識特徵', max_length=100, blank=True)
    owner_tax_id_no = models.CharField('船舶所有人統編', max_length=30, blank=True)
    tonnage = models.CharField('噸數', max_length=1, blank=True)
    length = models.PositiveIntegerField('長', default=0, blank=True)
    width = models.PositiveIntegerField('寬',  default=0, blank=True)
    deepest_draft = models.PositiveIntegerField('船舶最深吃水', default=0, blank=True)
    crew_quota = models.PositiveIntegerField('船員配額', default=0, blank=True)
    max_capacity = models.PositiveIntegerField('限載成員人數', blank=True)
    cert_valid_date = models.DateField('檢查證書效期(年月日)', null=True, blank=True)
    license_valid_date = models.DateField('來臺特許文件效期(年月日)', null=True, blank=True)
    ship_kind = models.CharField('船舶種類', max_length=100, blank=True)
    owner = models.ForeignKey(VesselOwner, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self) -> str:
    #     return self.name_cn


class Form(models.Model):
    vessel = models.ForeignKey(Vessel, on_delete=models.CASCADE)
    port = models.ForeignKey(Port, on_delete=models.CASCADE)
    purpose = models.CharField('進港目的', max_length=100)
    scheduled_departure = models.DateTimeField('預定出港日期')
    scheduled_arrival = models.DateTimeField('預定進港日期')
    actual_departure = models.DateTimeField('實際出港日期')
    actual_arrival = models.DateTimeField('實際進港日期')
    signature = models.ImageField('申請人簽章', upload_to='signatures', default='signatures/default.png', blank=True)
    form_filling_date = models.DateTimeField('填表日期')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    

class Passenger(models.Model):
    name = models.CharField('姓名', max_length=10)
    id_no = models.CharField('身分證或護照號碼', max_length=10)
    contact_no = models.CharField('聯絡號碼', max_length=10)
    emergency_contact_person = models.CharField('緊急聯絡人', max_length=10)
    emergency_contact_no = models.CharField('緊急聯絡人聯絡號碼', max_length=10)
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)



