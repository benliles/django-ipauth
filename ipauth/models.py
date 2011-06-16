from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models



class Range(models.Model):
    user = models.ForeignKey(User, related_name='+')
    lower = models.IPAddressField(db_index=True, unique=True)
    upper = models.IPAddressField(db_index=True, blank=True)
    
    def clean(self):
        others = Range.objects.exclude(pk=self.pk)
        
        if others.filter(lower__lt=self.lower, 
                         upper__gte=self.lower).count() > 0:
            raise ValidationError('%s is captured by an existing range.' % 
                                  (self.lower,))
        
        if self.upper:
            if others.filter(lower__range=(self.lower, self.upper)):
                raise ValidationError('%s-%s contains an existing range.' % 
                                      (self.lower, self.upper,))
            if others.filter(lower__lte=self.upper, 
                             upper__gte=self.upper).count() > 0:
                raise ValidationError('%s is captured by an existing range.' % 
                                      (self.upper,))
            if self.lower >= self.upper:
                raise ValidationError('Lower end of the range must be less than '
                                      'the upper end')
    
    def __unicode__(self):
        if self.upper:
            return u'%s %s-%s' % (self.user.get_full_name(), self.lower,
                                  self.upper)
        return u'%s %s' % (self.user.get_full_name(), self.lower)
    
    class Meta:
        ordering = ['lower',]
