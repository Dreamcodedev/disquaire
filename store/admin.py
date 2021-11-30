from django.contrib import admin
from .models import Booking, Contact, Album, Artist

# Register your models here.
@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):

    search_fields = ['reference', 'title']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_filter = ['created_at', 'contacted']
    readonly_fields = ["created_at", "contact", 'album', 'contacted']
    def has_add_permission(self, request):
        return False


class BookingInline(admin.TabularInline):
    model = Booking
    fieldsets = [
        (None, {'fields': ['album', 'contacted']})
        ] # list columns
    verbose_name = "Réservation"
    verbose_name_plural = "Réservations"
    readonly_fields = ["created_at", "contacted", "album"]
    def has_add_permission(self, request):
        return False
    extra = 0

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    inlines = [BookingInline,] # list of bookings made by a contact


class AlbumArtistInline(admin.TabularInline):
    model = Album.artists.through # the query goes through an intermediate table.
    verbose_name = "Disque"
    verbose_name_plural = "Disques"
    extra = 1

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    inlines = [AlbumArtistInline,]