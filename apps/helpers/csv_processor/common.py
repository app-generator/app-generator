# -*- encoding: utf-8 -*-

# Pandas Type
django_fields = {
    'int'           : 'models.IntegerField(blank=True, null=True)',
    'integer'       : 'models.IntegerField(blank=True, null=True)',
    'string'        : "models.TextField(blank=True, null=True)",
    'string_unique' : "models.TextField(blank=True, null=False, unique=True)",
    'object'        : "models.TextField(blank=True, null=True)",
    'object_unique' : "models.TextField(blank=True, null=False, unique=True)",
    'int64'         : 'models.IntegerField(blank=True, null=True)',
    'float64'       : 'models.FloatField(blank=True, null=True)',
    'bool'          : 'models.BooleanField(null=True)',
}
