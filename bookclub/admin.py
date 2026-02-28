from django.contrib import admin
from .models import Genre, Book


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):

    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "author",
        "genre",
        "publication_year",
        "created_on",
        "updated_on",
    )
    list_filter = ("genre", "publication_year")
    search_fields = ("title", "author")
