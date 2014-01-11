from django import forms
import os.path


class ImageDetected(forms.Form):
    photo = forms.ImageField()

    def is_valid(self):
        """Validates image extension"""
        valid = super(ImageDetected, self).is_valid()
        ext = self.get_extension()
        valid = valid and ext == ".jpeg"
        return valid

    def get_extension(self):
        """Gets file extension"""
        return os.path.splitext(self.cleaned_data['photo'].name)[1]
