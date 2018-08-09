from onadata.apps.logger.models import Project
from rest_framework import serializers
from rest_framework.fields import SkipField


class ProjectRelatedField(serializers.RelatedField):
    """A custom field to represent the content_object generic relationship"""

    def get_attribute(self, instance):
        # xform is not an attribute of the MetaData object
        if instance and isinstance(instance.content_object, Project):
            return instance.content_object

        raise SkipField()

    def to_internal_value(self, data):
        try:
            return Project.objects.get(pk=data)
        except ValueError:
            raise Exception("project id should be an integer")

    def to_representation(self, instance):
        """Serialize project object"""
        return instance.pk
