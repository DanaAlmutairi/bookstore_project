from django.contrib import admin
from .models import Book, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "book_count")
    search_fields = ("name",)
    ordering = ("name",)

    def book_count(self, obj):
        return obj.books.count()
    book_count.short_description = "Number of books"


class CategoryInline(admin.TabularInline):
    model = Book.categories.through
    extra = 1


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "price",
        "stock",
        "published_at",
        "display_categories",
    )
    list_filter = ("categories", "published_at")
    search_fields = ("title", "author", "isbn", "description")
    ordering = ("title",)
    list_editable = ("price", "stock") # edit these straight from list view
    list_per_page = 20

    fieldsets = (
        ("Basic information", {
            "fields": ("title", "author", "description")
        }),
        ("Details & Availability", {
            "fields": ("price", "stock", "isbn", "published_at", "categories")
        }),
    )

    def display_categories(self, obj):
        return ", ".join(c.name for c in obj.categories.all())
    display_categories.short_description = "Categories"
