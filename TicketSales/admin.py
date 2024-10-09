from django.contrib import admin
from TicketSales.models import (
    Concert,
    Location,
    TimeSlot,
    Ticket,
)


class ConcertAdmin(admin.ModelAdmin):
    list_display = ("name", "singer_name", "length", "Concert_picture")


admin.site.register(Concert, ConcertAdmin)
admin.site.register(Location)
admin.site.register(TimeSlot)
admin.site.register(Ticket)
