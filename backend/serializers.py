from .models import MapsCrseCatalog, MapsInstitutions, MapsDmapsLists, MapsAcadPlan, MapsDmapsMeta
from rest_framework import serializers

class CampusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MapsInstitutions
        fields = ['institute_id', 'descr']

class DegreesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MapsAcadPlan
        fields = ['degree', 'level', 'institute_id', 'degree_descr', 'level_descr']

class MapSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MapsDmapsLists
        fields = ['map', 'semester_num', 'course1', 'course2', 'course3', 'course4', 'course5', 'course6', 'course7']

class MapDmapMetaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MapsDmapsMeta
        fields = ['map_id', 'map_name','degree', 'start_year', 'institute','submit_time','last_update_time']

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MapsCrseCatalog
        fields = ['course_id', 'eff_date', 'status', 'subject', 'catalog', 'descr', 'min_units', 'max_units', 'designation']