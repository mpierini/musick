from django.db import models

class TagField(models.TextField):
    description = "Stores tags in a single database column."
    __metaclass__ = models.SubfieldBase

    def __init__(self, delimiter="|", *args, **kwargs):
        self.delimiter = delimiter
	super(TagField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        #If it's already a list, leave it
	if isinstance(value, list):
	    return value
	
	#Otherwise, split by delimiter
	return value.split(self.delimiter)

    def get_prep_value(self, value):
        return self.delimiter.join(value)

	#custom field info comes from south tutorial part 4
