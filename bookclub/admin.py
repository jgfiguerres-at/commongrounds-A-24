from django.contrib import admin
from .models import Genre, Book


class GenreAdmin(admin.ModelAdmin):
    model = Genre
    list_display = ("name",)
    search_fields = ("name",)

    fieldsets = [
        ("Details", {
            "fields": [
                "name",
                "description",
            ]
        })
    ]

class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ("title", "author", "genre", "publication_year", "created_on", "updated_on",)
    list_filter = ("genre", "publication_year")
    search_fields = ("title", "author")

    fieldsets = [
        ("Details", {
            "fields": [
                "title",
                "author",
                "genre",
                "publication_year",
            ]
        }),
    ]


admin.site.register(Genre, GenreAdmin)
admin.site.register(Book, BookAdmin)